import streamlit as st  # type: ignore # Importar la librería

# Configuración básica de la ventana de la web
st.set_page_config(page_title="Mi chat de IA", page_icon="🔮", layout="centered")

# Título principal de la aplicación
st.title("Mi Primera Aplicación con Streamlit")
st.subheader("Mi chat de IA")

# Ingreso de dato del usuario
nombre = st.text_input("¿Cuál es tu nombre?")

# Creamos un botón con funcionalidad para saludar al usuario
if st.button("Saludar"):
    if nombre:
        st.write(f"¡Hola {nombre}! Gracias por venir a Talento Tech")
    else:
        st.write("Por favor, ingresa tu nombre.")

# Opciones del modelo
MODELOS = [
    'GPT-3',
    'BERT',
    'T5',
    'LLaMA',
    'DistilBERT'
]

def configurar_pagina():
    # Título en la barra lateral
    st.sidebar.title("Configuración de la IA")
    # Selectbox para elegir un modelo
    elegirModelo = st.sidebar.selectbox(
        "Elige un modelo",  # Título del selectbox
        MODELOS,           # Opciones del menú
        index=0           # Valor por defecto
    )
    return elegirModelo

# Llamamos a la función para configurar la página y guardamos el modelo seleccionado
modelo = configurar_pagina()

# Campo de entrada para el mensaje del usuario
mensaje = st.chat_input("Escribe un mensaje...")
if mensaje:
    st.write(f"Usuario: {mensaje}")  # Mostrar el mensaje en la aplicación
    print(mensaje)  # Imprimir el mensaje en la terminal
