# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:20:32 2024

@author: jperezr
"""

import streamlit as st
import pandas as pd

st.title('Registro de Usuarios')

# Formulario para ingresar datos
name = st.text_input('Nombre')
dob = st.date_input('Fecha de Nacimiento')

# Botón para enviar datos
if st.button('Registrar'):
    # Cargar datos existentes
    try:
        df = pd.read_csv('usuarios.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Nombre', 'Fecha de Nacimiento'])
    
    # Agregar nuevo registro
    new_row = {'Nombre': name, 'Fecha de Nacimiento': dob}
    df = df.append(new_row, ignore_index=True)
    
    # Guardar datos
    df.to_csv('usuarios.csv', index=False)
    
    st.success('¡Datos registrados exitosamente!')
