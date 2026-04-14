import streamlit as st
import pandas as pd
from urllib.parse import urlparse

from seo_scraper import obtener_titulos_seo 


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