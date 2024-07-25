# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:20:32 2024

@author: jperezr
"""

import streamlit as st
import pandas as pd
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
from datetime import datetime

# Autenticación con Google Drive
gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.json")
if gauth.credentials is None:
    # No hay credenciales guardadas
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Las credenciales han expirado
    gauth.Refresh()
else:
    # Las credenciales son válidas
    gauth.Authorize()
gauth.SaveCredentialsFile("credentials.json")

drive = GoogleDrive(gauth)

# ID de la carpeta de Google Drive donde se almacenarán los archivos
FOLDER_ID = '1fSi9Pi01wn1zKD_sWm67ZOMjIE4Xr0-g'

# Cargar los perfiles existentes desde Google Drive
def cargar_perfiles():
    perfiles = []
    file_list = drive.ListFile({'q': f"'{FOLDER_ID}' in parents and mimeType='text/plain'"}).GetList()
    for file in file_list:
        file_content = file.GetContentString()
        perfil = file_content.splitlines()
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
            foto_path = f"{nombre}.jpg"
            foto_file = drive.CreateFile({'title': foto_path, 'parents': [{'id': FOLDER_ID}]})
            foto_file.SetContentFile(foto_path)
            foto_file.Upload()
            foto_id = foto_file['id']
        else:
            foto_id = ""

        # Guardar los datos en un archivo .txt
        perfil_path = f"{nombre}.txt"
        perfil_content = f"{nombre}\n{rol}\n{descripcion}\n{fecha_nacimiento}\n{foto_id}"
        perfil_file = drive.CreateFile({'title': perfil_path, 'parents': [{'id': FOLDER_ID}]})
        perfil_file.SetContentString(perfil_content)
        perfil_file.Upload()

        st.sidebar.success("Perfil guardado con éxito!")
        # Recargar los perfiles
        perfiles = cargar_perfiles()
    else:
        st.sidebar.error("Por favor, completa todos los campos antes de guardar el perfil.")

# Mostrar los perfiles
st.header("Perfiles del Equipo")
for perfil in perfiles:
    nombre, rol, descripcion, fecha_nacimiento, foto_id = perfil
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
    if foto_id:
        foto_url = f"https://drive.google.com/uc?id={foto_id}"
        try:
            st.image(foto_url, width=200)  # Ajuste del tamaño de la imagen
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
