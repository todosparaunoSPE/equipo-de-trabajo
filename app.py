# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:20:32 2024

@author: jperezr
"""

import streamlit as st

# URL del Formulario de Google Forms
form_url = 'https://docs.google.com/forms/d/1BLmlBVkSTSxBxtaGruUhmPHAm_UgGRJxLNJFCMWIjtA/edit'  # Reemplaza con la URL de tu formulario de Google Forms

# URL de la Hoja de Cálculo de Google Sheets
sheet_url = 'https://docs.google.com/spreadsheets/d/1MErVayHDLtzedSj0Xg9JaplH9jHegkYA4_03yY7xrno/edit?resourcekey=&gid=73643069#gid=73643069'  # Reemplaza con la URL de tu hoja de cálculo de Google Sheets

st.title('Registro de Usuarios')

st.write('Por favor, completa el siguiente formulario para registrar tus datos:')
st.markdown(f"[Formulario de Registro]({form_url})", unsafe_allow_html=True)

st.write('Puedes ver los datos recopilados en la siguiente hoja de cálculo:')
st.markdown(f"[Hoja de Cálculo de Google Sheets]({sheet_url})", unsafe_allow_html=True)

# Si quieres permitir la carga de datos adicionales o realizar otras acciones, puedes hacerlo aquí
