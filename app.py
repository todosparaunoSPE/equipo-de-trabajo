# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:20:32 2024

@author: jperezr
"""

import streamlit as st

# URL del Formulario de Google Forms
form_url = 'https://docs.google.com/forms/d/1gVCG45UPELL_UVhMCCPne415MmHYMQgH76xBV2wb2z8/edit'  # Reemplaza con la URL de tu formulario de Google Forms

# URL de la Hoja de Cálculo de Google Sheets
sheet_url = 'https://docs.google.com/spreadsheets/d/1PJFCnpYxmAzjcH3Faav1jDnaJYX7B_mXpllXWQWZ7Ak/edit?resourcekey=&gid=440930739#gid=440930739'  # Reemplaza con la URL de tu hoja de cálculo de Google Sheets

st.title('Registro de Usuarios')

st.write('Por favor, completa el siguiente formulario para registrar tus datos:')
st.markdown(f"[Formulario de Registro]({form_url})", unsafe_allow_html=True)

st.write('Puedes ver los datos recopilados en la siguiente hoja de cálculo:')
st.markdown(f"[Hoja de Cálculo de Google Sheets]({sheet_url})", unsafe_allow_html=True)

# Si quieres permitir la carga de datos adicionales o realizar otras acciones, puedes hacerlo aquí
