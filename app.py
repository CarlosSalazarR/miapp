import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Para la morena más chula",
    layout="centered"
)

# Un poco de estilo "aesthetic"
st.markdown(
    """
    <style>
    body {
        background-color: #ffe4e1; /* Rosa clarito */
        color: #d6336c;           /* Rosa intenso */
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
    }
    h1 {
        font-size: 2.5em;
        margin-top: 2em;
    }
    .stButton button {
        background-color: #ffa6c9; /* Color de fondo del botón */
        color: white;             /* Color de letra del botón */
        border-radius: 15px;
        font-size: 1.2em;
        padding: 0.5em 1.5em;
        margin: 0.5em;
        border: none;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #ff84af; /* Color al pasar el ratón */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Mensaje principal
st.title("Mady me gustas mucho y te extraño.\n¿Qué dices, Seguimos?")

# Botones de Sí y No
col1, col2 = st.columns(2)

if col1.button("Chi"):
    # Efecto visual (globitos)
    st.balloons()
    st.success("¡Me encanta que sigamos juntos, Mady!")

if col2.button("Talvez"):
    # Efecto visual (copos de nieve)
    st.snow()
    st.error("Oh... ¿por qué, Mady? ¿No te gusto?")

