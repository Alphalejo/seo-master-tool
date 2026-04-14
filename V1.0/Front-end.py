import streamlit as st
import pandas as pd
from urllib.parse import urlparse

# Import the functions
from seo_scraper import obtener_titulos_seo 
from compliance_checker import get_state_compliance_info, us_states, mls_boards

# Page configuration
st.set_page_config(page_title="SEO Auditor Tool", layout="wide")

st.markdown("# Agent Compliance Hub")
st.markdown("Instant SEO analyzer and compliance verification for States, Brokerages, and MLS.")


# Inyectar CSS para modificar el tamaño de las tabs
st.markdown(
    """
    <style>
    /* Cambiar tamaño de fuente y padding de las tabs */
    .stTabs [role="tab"] {
        font-size: 22px;
        padding: 12px 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# tabs for SEO and compliance
seo_tab, compliance_tab = st.tabs(["SEO Analyzer", "Compliance Checker"])

with seo_tab:

    # App Title
    st.markdown("## 🔍 Website SEO Title Auditor")
    st.markdown("Analyze the SEO titles of your subpages and check their ideal length.")

    # Input bar and button
    col1, col2 = st.columns([3, 1])

    with col1:
        url_input = st.text_input("Enter the website URL:", placeholder="https://example.com")

    with col2:
        st.markdown(
            """
            <style>
            .stButton > button {
                margin-top: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        ) # Spacer to align the button
        boton_audit = st.button("Audit 🚀", use_container_width=True)

    # Color formatting logic for the table
    def color_longitud(val):
        color = 'color: #27ae60;' if 45 <= val <= 60 else 'color: #e74c3c;'
        return color

    if boton_audit:
        if url_input:
            with st.spinner('Scanning the website... this may take a moment.'):
                # Call your original function
                datos = obtener_titulos_seo(url_input, limite_paginas=50)
                
                if datos:
                    # Process the data for the Streamlit table
                    tabla_datos = []
                    for item in datos:
                        # Extract the page name (what follows the last "/")
                        path = urlparse(item['url']).path.rstrip('/')
                        nombre_pagina = path.split('/')[-1] if path else "Home"
                        
                        tabla_datos.append({
                            "Page": nombre_pagina,
                            "SEO Title": item['titulo'],
                            "Characters": item['longitud']
                        })
                    
                    df = pd.DataFrame(tabla_datos)

                    # Show the table with applied style
                    st.subheader(f"Results for: {url_input}")
                    
                    # Apply conditional style to the 'Characters' column
                    st.table(df.style.map(color_longitud, subset=['Characters']))
                    
                    # Option to download the CSV from the web
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download CSV Report",
                        data=csv,
                        file_name='seo_audit_report.csv',
                        mime='text/csv',
                    )
                else:
                    st.error("No pages found or there was an error accessing the site.")
        else:
            st.warning("Please enter a valid URL.")

    # Footer
    st.divider()
    st.caption("Internal tool for quick SEO Titles audit.")

# ===============================================================================================
# COMPLIANCE CHECKER TAB
# ===============================================================================================

with compliance_tab:
    
    st.markdown("## ⚖️ Compliance Checker")
    st.markdown("Verify compliance requirements by State, Brokerage, and MLS.")

    # Input form
    with st.container():
        st.subheader("Query Data")
        
        col1, col2, col3 = st.columns([1, 2, 4])

        with col1:
            # Input for State (convert the set to a list and sort alphabetically)
            # I assume the variable in compliance_checker.py is called us_states
            estado_seleccionado = st.selectbox(
                "Select the State:", 
                options=sorted(list(us_states)),
                index=None,
                placeholder="ex: CA"
            )

        with col2:      
            # Input for Brokerage (for now free text)
            brokerage_input = st.text_input("Enter the Brokerage:", placeholder="Ex: Compass, eXp, etc.")

        with col3:
            # Input for multiple MLS (free text, separated by commas)
            mls_input = st.multiselect("Enter the MLS:", placeholder="Ex: CRMLS, Stellar MLS...", options=sorted(list(mls_boards.keys())))

    # Execution button and results
    if st.button("Verify Compliance", type="primary"):
        
        if not estado_seleccionado:
            st.warning("⚠️ Please select a state before continuing.")
        else:
            st.divider()
            st.subheader("📊 Compliance Results")
            
            # 1. Get backend information for the State
            info_estado = get_state_compliance_info(estado_seleccionado)
            
            # Display the State data in columns for better organization
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    label="High Compliance State", 
                    value="Yes ✅ " if info_estado["high compliance"] else "No ❌"
                )
                
            with col2:
                st.metric(
                    label="Non-Disclosure State", 
                    value="Yes ✅" if info_estado["none-disclosure estate"] else "No ❌"
                )
            
            st.info(f"🔗 **State Documentation:** [View Compliance Link]({info_estado['compliance link']})")
            
            # 2. Placeholders for Brokerage and MLS
            st.divider()
            st.markdown("### 🏢 Brokerage and MLS Information")
            
            if brokerage_input:
                st.write(f"**Entered Brokerage:** {brokerage_input} *(Pending validation)*")
                
            if mls_input:
                for mls in mls_input:
                    st.write(f"{mls}: {mls_boards[mls]}")