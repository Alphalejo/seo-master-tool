import streamlit as st
import pandas as pd
from urllib.parse import urlparse
from toolkit.SEO_scraper2 import get_seo_data
from toolkit.SEO_dashboard import show_analytics_dashboard
from toolkit.SEO_AI import generate_seo_title

from toolkit.compliance_checker import get_state_compliance_info, get_brokerage_compliance_info, us_states, mls_boards, partnerships_brokerage, non_partnerships_brokerage

st.set_page_config(page_title="SEO Master Optimizer", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    @media (min-width: calc(736px + 8rem)) {
    .st-emotion-cache-zy6yx3 {
        padding-top: 2rem;
        padding-left: 10rem;
        padding-right: 10rem;
    }
    .st-emotion-cache-r7ut5z h1{
            font-size: 3.2rem;}
    
    @media (min-width: calc(736px + 8rem)) {
    .st-emotion-cache-zy6yx3 {
        max-width: 1200px;
    }
}
    </style>
    """, unsafe_allow_html=True)

# Session State Initialization
if 'seo_results' not in st.session_state:
    st.session_state['seo_results'] = []
if 'seo_draft' not in st.session_state:
    st.session_state['seo_draft'] = ""
if 'broken_links' not in st.session_state:
    st.session_state['broken_links'] = []
if 'broken_check_was_run' not in st.session_state:
    st.session_state['broken_check_was_run'] = False
if 'is_running' not in st.session_state:
    st.session_state['is_running'] = False
if 'ai_error' not in st.session_state:
    st.session_state['ai_error'] = ""

# --- APP LAYOUT ---
st.title("SEO Master Tool")
st.caption("Professional Website Auditor & AI-Powered Title Optimizer")

# Increasing tabs size
st.markdown(
    """
    <style>
    #tabs-bui2-tab-0 > div > p, #tabs-bui2-tab-1 > div > p{
        font-size: 24px;
        padding: 12px 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

tabs = st.tabs(["🎯 SEO Analyzer", "📋 Compliance"])

# ===============================================================================================
# SEO ANALYZER TAB
# ===============================================================================================
with tabs[0]:
    # 1. SCANNER SECTION
    st.markdown("## 🔍 Website Scanner")

    st.markdown("""
    <style>
    [data-testid="column"] { gap: 0rem; padding: 0rem; }
    .st-emotion-cache-zh2fnc{
                width: 100%;}
    </style>
    """, unsafe_allow_html=True)

    col_input, col_brok, col_btn = st.columns([3, 1, 1], vertical_alignment="bottom")
    
    with col_input:
        target_url = st.text_input("Target URL:", placeholder="https://luxurypresence.com")
    with col_brok:
        check_broken = st.checkbox("Check broken links")
    with col_btn:
        run_audit = st.button("Run Audit 🚀")

    results_container = st.container()

    if run_audit:
        st.session_state['seo_results'] = []
        st.session_state['broken_links'] = []
        st.session_state['broken_check_was_run'] = check_broken
        st.session_state['is_running'] = True
        with results_container:
            with st.spinner("Crawling website..."):
                st.session_state['seo_results'], st.session_state['broken_links'] = get_seo_data(target_url, check_broken_links=check_broken)
        st.session_state['is_running'] = False
    
    if st.session_state['seo_results'] and not st.session_state['is_running']:
        # 2. RESULTS TABLE
        df_display = pd.DataFrame(st.session_state['seo_results'][1:])  # Skip the homepage for the table since it's duplicated
        
        # Helper function to extract page name from URL
        def get_page_name(url):
            path = urlparse(url).path.rstrip('/')
            return path.split('/')[-1].capitalize() if path else "Home"
            
        # Apply format and rename columns for better UI
        df_display['url'] = df_display['url'].apply(get_page_name)
        df_display = df_display.rename(columns={'url': 'Page', 'title': 'SEO Title', 'length': 'Chars'})
        
        st.table(df_display.style.map(
            lambda x: 'color: #27ae60;' if 45 <= x <= 60 else 'color: #e74c3c;', 
            subset=['Chars']
        ))

        st.divider()

        # 3. BROKEN LINKS SECTION
        if st.session_state['broken_links']:
            st.subheader("⚠️ Broken Links Detected")
            st.table(pd.DataFrame(st.session_state['broken_links']))
        elif check_broken and not st.session_state['broken_check_was_run'] and st.session_state['seo_results']:
            st.warning("Broken link check was enabled after the audit. Please re-run the audit to check for broken links.")
        elif st.session_state['broken_check_was_run'] and not st.session_state['broken_links']:
            st.success("No broken links found!")

        st.divider()

        # 4. AI OPTIMIZER SECTION
        st.subheader("2. Quick SEO Optimizer")
        
        def run_ai_magic():
            current = st.session_state['seo_draft']
            if not current:
                st.session_state['ai_error'] = "Please paste a current SEO title first."
                return
            st.session_state['ai_error'] = ""
            st.session_state['seo_draft'] = generate_seo_title(current_title=current)

        col_draft, col_stat, col_magic = st.columns([3, 1, 1], vertical_alignment="bottom")

        with col_draft:
            st.text_input("Edit or Generate Title:", key='seo_draft', placeholder="Paste a title or use Magic AI...")

        with col_stat:
            char_len = len(st.session_state['seo_draft'])
            stat_color = "green" if 45 <= char_len <= 60 else "red"
            st.markdown(f"**Length:** <span style='color:{stat_color}; font-size:20px;'>{char_len}</span>", unsafe_allow_html=True)

        with col_magic:
            st.button("Magic AI ✨", on_click=run_ai_magic)

        if st.session_state.get('ai_error'):
            st.warning(st.session_state['ai_error'])

        st.divider()

        # 5. ANALYTICS (Lazy Loading)
        st.subheader("3. Data Insights")
        show_charts = st.toggle("📊 Load Analytics Dashboard")
        
        if show_charts:
            show_analytics_dashboard(
                st.session_state['seo_results'],
                broken_links=st.session_state['broken_links'] if st.session_state['broken_check_was_run'] else None
            )

    else:
        pass
# ===============================================================================================
# COMPLIANCE CHECKER TAB
# ===============================================================================================
with tabs[1]:
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
            # Input for multiple Brokerages
            all_brokerages = sorted(list(partnerships_brokerage.keys()) + list(non_partnerships_brokerage.keys()))
            brokerage_input = st.selectbox("Select Brokerage (optional):", options=[""] + all_brokerages, index=0, placeholder="Ex: Compass...")

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

            info_estado = get_state_compliance_info(estado_seleccionado, brokerage_input)

            col1, col2 = st.columns(2)
            with col1:
                st.metric("High Compliance State", "Yes ✅" if info_estado["high compliance"] else "No ❌")
            with col2:
                st.metric("Non-Disclosure State", "Yes ✅" if info_estado["non_disclosure"] else "No ❌")

            if info_estado["non_disclosure_link"]:
                    st.info(f"🔗 **Non-Disclosure Documentation:** [View Link]({info_estado['non_disclosure_link']})")

            if info_estado["compliance_link"]:
                if info_estado["required_brokerage"]:
                    st.warning(f"⚠️ This compliance link applies specifically to **{info_estado['required_brokerage']}** brokerage.")
                st.info(f"🔗 **State Documentation:** [View Compliance Link]({info_estado['compliance_link']})")

            # MLS Section
            if mls_input:
                st.divider()
                st.markdown("### 🏢 MLS Information")
                for mls in mls_input:
                    st.write(f"**{mls}:** [View Link]({mls_boards[mls]})")
            
            if brokerage_input:
                    brokerage_info = get_brokerage_compliance_info(brokerage_input)
                    st.divider()
                    st.markdown("### 🏢 Brokerage Compliance")
                    if brokerage_info["url"]:
                        badge = "🤝 Partnership" if brokerage_info["partnership"] else "📋 No Partnership"
                        st.info(f"**{brokerage_input}** — {badge}")
                        st.info(f"🔗 **Brokerage Documentation:** [View Link]({brokerage_info['url']})")
                    else:
                        st.warning(f"⚠️ **{brokerage_input}** is not a registered high compliance brokerage.")