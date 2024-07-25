# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:20:32 2024

@author: jperezr
"""

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Verificar y crear el directorio de fotos si no existe
if not os.path.exists("fotos"):
    os.makedirs("fotos")

# Cargar los perfiles existentes
if os.path.exists('perfiles.csv'):
    perfiles_df = pd.read_csv('perfiles.csv')
    # Asegurarse de que las columnas necesarias están presentes
    if 'Fecha de Nacimiento' not in perfiles_df.columns:
        perfiles_df['Fecha de Nacimiento'] = pd.NaT
else:
    perfiles_df = pd.DataFrame(columns=['Nombre', 'Rol', 'Descripción', 'Fecha de Nacimiento', 'Foto'])

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
        if foto:
            foto_path = os.path.join("fotos", f"{nombre}.jpg")
            with open(foto_path, "wb") as f:
                f.write(foto.getbuffer())
        else:
            foto_path = ""

        nuevo_perfil = pd.DataFrame({'Nombre': [nombre], 'Rol': [rol], 'Descripción': [descripcion], 'Fecha de Nacimiento': [fecha_nacimiento], 'Foto': [foto_path]})
        perfiles_df = pd.concat([perfiles_df, nuevo_perfil], ignore_index=True)
        perfiles_df.to_csv('perfiles.csv', index=False)
        st.sidebar.success("Perfil guardado con éxito!")
    else:
        st.sidebar.error("Por favor, completa todos los campos antes de guardar el perfil.")

# Mostrar los perfiles
st.header("Perfiles del Equipo")
for index, row in perfiles_df.iterrows():
    st.subheader(row['Nombre'])
    st.write(f"**Rol:** {row['Rol']}")
    st.write(f"**Descripción:** {row['Descripción']}")
    
    # Verificar si la fecha de nacimiento es válida antes de formatear
    if pd.notna(row['Fecha de Nacimiento']):
        try:
            fecha_nacimiento = pd.to_datetime(row['Fecha de Nacimiento'])
            st.write(f"**Fecha de Nacimiento:** {fecha_nacimiento.strftime('%d/%m/%Y')}")
        except ValueError:
            st.write("**Fecha de Nacimiento:** No disponible")
    else:
        st.write("**Fecha de Nacimiento:** No disponible")
    
    if pd.notna(row['Foto']) and row['Foto'] != "":
        st.image(row['Foto'], width=200)  # Ajuste del tamaño de la imagen

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
