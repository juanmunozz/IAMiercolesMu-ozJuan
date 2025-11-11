### IMPORTAMOS Streamlit y Groq
# Para instalar: python -m pip install streamlit groq
import streamlit as st
from groq import Groq

# Configuración de la página
st.set_page_config(page_title="El chat de Muñoz ;)", page_icon="🤖")
st.title("Chat IA")

# Modelos actualizados de Groq
MODELOS = ["llama-3.1-8b-instant", "llama-3.3-70b-versatile","deepseek-r1-distill-llama-70b"]

# Crear cliente Groq
def crear_cliente():
    clave_secreta = st.secrets["CLAVE_API"]
    return Groq(api_key= clave_secreta)


# Inicializar historial
def inicializar_historial():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

# Función principal del chat (también imprime en consola)
def chat_con_modelo(cliente, modelo, mensaje_usuario):
    respuesta = cliente.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": mensaje_usuario}],
        stream=False
    )
    contenido = respuesta.choices[0].message.content
    print(f"\n📨 Modelo usado: {modelo}")
    print(f"🧍 Usuario: {mensaje_usuario}")
    print(f"🤖 IA: {contenido}\n")
    return contenido

# Inicialización
cliente = crear_cliente()
modelo = st.sidebar.selectbox("Elegí un modelo:", MODELOS)
inicializar_historial()

# Campo de chat
mensaje = st.chat_input("Escribí tu mensaje...")

if mensaje:
    respuesta = chat_con_modelo(cliente, modelo, mensaje)
    st.session_state.mensajes.append(("🧍‍♂️ Tú", mensaje))
    st.session_state.mensajes.append(("🤖 IA", respuesta))

# Mostrar historial
for remitente, texto in st.session_state.mensajes:
    st.markdown(f"**{remitente}:** {texto}")


