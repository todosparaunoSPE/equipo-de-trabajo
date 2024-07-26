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

# Configuración de la barra lateral
with st.sidebar:
    st.header("")
    st.markdown("""
        ## ¡Viernes de Trivia en AFORE PENSIONISSSTE! 🎉

        Hola a todos,

        Espero que estén teniendo una excelente semana. Para cerrar con broche de oro, quiero invitarlos a un evento especial este viernes: ¡una Trivia divertida sobre AFORE PENSIONISSSTE!

        📅 Fecha: Este viernes 26/07/2024
        🕒 Hora: Hasta las 5 pm
       
        
        **Instrucciones:**

        - Completen todos los campos requeridos.
        - Si tienen alguna pregunta o inquietud, no duden en contactarme.

        Agradezco de antemano su colaboración.

        Saludos cordiales,  
        - Javier Horacio Pérez Ricárdez
        - Analista UEAP "B"
        

        © 2024 jahoperi. Todos los derechos reservados.
    """)

# Incrustar el formulario en Streamlit
st.title("Formulario de Perfil Profesional y Preferencias")
components.iframe(form_url, width=800, height=600, scrolling=True)
