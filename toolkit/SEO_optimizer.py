import streamlit as st

# 1. Inicializamos la variable en el estado de la sesión si no existe
if 'seo_draft' not in st.session_state:
    st.session_state['seo_draft'] = ""

# 2. Función que simula la IA y sobrescribe el texto
def generar_seo_ia():
    # En el futuro, aquí enviarías st.session_state['seo_draft'] a la API
    # Por ahora, simplemente sobrescribimos la variable
    st.session_state['seo_draft'] = "This is a functional test of the SEO generator"

st.subheader("Quick SEO Optimizer")

# Estructura de columnas
col_text, col_count, col_ai = st.columns([3, 1, 1], vertical_alignment="bottom")

with col_text:
    # 3. El input está atado directamente a st.session_state['seo_draft'] a través del 'key'
    st.text_input(
        "Draft your SEO Title", 
        key='seo_draft', 
        placeholder="Escribe el contexto, la página y la ubicación aquí..."
    )

with col_count:
    # 4. El contador lee en tiempo real la longitud del texto actual
    largo = len(st.session_state['seo_draft'])
    color_stat = "green" if 20 <= largo <= 60 else "red"
    st.markdown(
        f"<div style='text-align: center; margin-bottom: 8px;'>"
        f"<b>Chars:</b> <span style='color:{color_stat}; font-size:20px;'>{largo}</span>"
        f"</div>", 
        unsafe_allow_html=True
    )

with col_ai:
    # 5. El botón llama a la función mediante 'on_click'
    st.button("Magic AI ✨", on_click=generar_seo_ia, use_container_width=True)