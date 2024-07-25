# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:20:32 2024

@author: jperezr
"""

import streamlit as st
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
import os

# Autenticación en Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Esto abrirá una ventana del navegador para autenticar
drive = GoogleDrive(gauth)

# Configura el archivo de texto para guardar la información del usuario
def save_user_info(name, role, description, dob, photo_id):
    file_name = f"{name}.txt"
    file_content = f"Nombre: {name}\nRol: {role}\nDescripción: {description}\nFecha de Nacimiento: {dob}\nFoto ID: {photo_id}"
    
    # Guarda el archivo en Google Drive
    file_drive = drive.CreateFile({'title': file_name})
    file_drive.Upload(content=file_content)
    return file_drive['id']

# Formulario de Streamlit
st.title('Formulario de Registro de Usuarios')

# Campos del formulario
name = st.text_input("Nombre")
role = st.text_input("Rol")
description = st.text_area("Descripción")
dob = st.date_input("Fecha de Nacimiento", min_value=datetime(1930, 1, 1), max_value=datetime(2024, 12, 31))
photo = st.file_uploader("Foto", type=['jpg', 'png'])

if st.button("Guardar Perfil"):
    if name and role and description:
        photo_id = ""
        if photo:
            photo_id = photo.name  # Aquí solo guardamos el nombre del archivo; podrías guardar la foto también si lo deseas

        file_id = save_user_info(name, role, description, dob, photo_id)
        st.success(f"Perfil guardado con éxito! ID del archivo en Google Drive: {file_id}")
    else:
        st.error("Por favor, completa todos los campos antes de guardar el perfil.")

# Mostrar los perfiles almacenados (opcional, si quieres ver la lista de archivos en Google Drive)
if st.checkbox("Mostrar Archivos Guardados"):
    file_list = drive.ListFile({'q': "trashed=false"}).GetList()
    for file in file_list:
        st.write(f'Título: {file["title"]}, ID: {file["id"]}')

