# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:20:32 2024

@author: jperezr
"""
import streamlit as st
import streamlit.components.v1 as components

# URL del formulario de Google Forms
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfz9RyOoxql_5ULHpthE33PcAVJOAn9wZBSa32SapsBzYkRFQ/viewform?usp=sf_link"

# URL de tu Google Sheet
sheet_url = "https://docs.google.com/spreadsheets/d/1OsShDjCOCM0OgPBMYh1LMKgrLw5qgLg8s2ol6oIr3r0/edit?resourcekey=&gid=132221002#gid=132221002"

# Incrustar el formulario en Streamlit
st.title("Formulario de Google en Streamlit")
components.iframe(form_url, width=800, height=600, scrolling=True)

# Agregar un enlace a Google Sheet
st.markdown(f"[Accede a la hoja de cálculo aquí]({sheet_url})", unsafe_allow_html=True)
