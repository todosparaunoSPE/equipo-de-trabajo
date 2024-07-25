# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:20:32 2024

@author: jperezr
"""

import streamlit as st
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import pandas as pd
import io

# Autenticación con Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Abre un navegador para autenticarse
drive = GoogleDrive(gauth)

def save_user_profile(name, role, description, dob):
    file_content = f'Nombre: {name}\nRol: {role}\nDescripción: {description}\nFecha de Nacimiento: {dob}'
    file_drive = drive.CreateFile({'title': f'{name}_profile.txt', 'mimeType': 'text/plain'})
    file_drive.UploadMetadata()
    file_drive.Upload(io.BytesIO(file_content.encode('utf-8')))
    return file_drive['id']

st.title('Registro de Usuarios')

name = st.text_input('Nombre')
role = st.text_input('Rol')
description = st.text_area('Descripción')
dob = st.date_input('Fecha de Nacimiento')

if st.button('Guardar Perfil'):
    if name and role and description:
        file_id = save_user_profile(name, role, description, dob)
        st.success(f'Perfil guardado con éxito! ID del archivo en Google Drive: {file_id}')
    else:
        st.error('Por favor, completa todos los campos antes de guardar el perfil.')
