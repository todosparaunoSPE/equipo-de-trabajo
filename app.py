# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:20:32 2024

@author: jperezr
"""

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Verificar y crear el directorio de fotos y usuarios si no existen
if not os.path.exists("fotos"):
    os.makedirs("fotos")
if not os.path.exists("usuarios"):
    os.makedirs("usuarios")

# Cargar los perfiles existentes desde archivos .txt
def cargar_perfiles():
    perfiles = []
    for archivo in os.listdir("usuarios"):
        if archivo.endswith(".txt"):
            with open(os.path.join("usuarios", archivo), "r") as f:
                perfil = f.read().splitlines()
                perfiles.append(perfil)
    return perfiles

perfiles = cargar_perfiles()

# Sección de ayuda en la barra lateral
st.sidebar.header("Ayuda")
st.sidebar.write("""
1. **Nombre**: Introduce el nombre completo de la persona.
2. **Rol**: Especifica el rol o puesto de la persona en el equipo.
3. **Descripción**: Proporciona una breve descripción de la persona.
4. **Fecha de Nacimiento**: Introduce la fecha de nacimiento de la persona.
5. **Foto**: Sube una foto en formato JPG o PNG.
6. **Guardar Perfil**: Haz clic en el botón para guardar el perfil.
""")

# Formulario para crear un perfil
st.sidebar.header("Crear Perfil")
nombre = st.sidebar.text_input("Nombre")
rol = st.sidebar.text_input("Rol")
descripcion = st.sidebar.text_area("Descripción")

# Ajustar el rango de fechas para el campo de fecha de nacimiento
fecha_nacimiento = st.sidebar.date_input(
    "Fecha de Nacimiento",
    min_value=datetime(1930, 1, 1),
    max_value=datetime(2024, 12, 31)
)
foto = st.sidebar.file_uploader("Foto", type=['jpg', 'png'])

if st.sidebar.button("Guardar Perfil"):
    if nombre and rol and descripcion:
        # Guardar la foto
        if foto:
            foto_path = os.path.join("fotos", f"{nombre}.jpg")
            with open(foto_path, "wb") as f:
                f.write(foto.getbuffer())
        else:
            foto_path = ""

        # Guardar los datos en un archivo .txt
        with open(os.path.join("usuarios", f"{nombre}.txt"), "w") as f:
            f.write(f"{nombre}\n{rol}\n{descripcion}\n{fecha_nacimiento}\n{foto_path}")

        st.sidebar.success("Perfil guardado con éxito!")
        # Recargar los perfiles
        perfiles = cargar_perfiles()
    else:
        st.sidebar.error("Por favor, completa todos los campos antes de guardar el perfil.")

# Mostrar los perfiles
st.header("Perfiles del Equipo")
for perfil in perfiles:
    nombre, rol, descripcion, fecha_nacimiento, foto_path = perfil
    st.subheader(nombre)
    st.write(f"**Rol:** {rol}")
    st.write(f"**Descripción:** {descripcion}")

    # Verificar si la fecha de nacimiento es válida antes de formatear
    if fecha_nacimiento != "NaT":
        try:
            fecha_nacimiento = pd.to_datetime(fecha_nacimiento)
            st.write(f"**Fecha de Nacimiento:** {fecha_nacimiento.strftime('%d/%m/%Y')}")
        except ValueError:
            st.write("**Fecha de Nacimiento:** No disponible")
    else:
        st.write("**Fecha de Nacimiento:** No disponible")

    # Verificar si la foto existe antes de intentar mostrarla
    if foto_path and os.path.exists(foto_path):
        try:
            st.image(foto_path, width=200)  # Ajuste del tamaño de la imagen
        except Exception as e:
            st.write("**Foto:** No disponible")
    else:
        st.write("**Foto:** No disponible")

# Agregar el texto de copyright en la parte inferior de la página
st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: white;
        background-color: #333;
        padding: 10px 0;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        &copy; 2024 Javier Horacio Pérez Ricárdez. Todos los derechos reservados.
    </div>
    """, unsafe_allow_html=True)
