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
    st.header("¡Viernes de Trivia en AFORE PENSIONISSSTE! 🎉")
    st.markdown("""
        ¡Hola a todos!

        Espero que estén teniendo una excelente semana. Para cerrar con broche de oro, quiero invitarlos a un evento especial este viernes: ¡una Trivia divertida sobre AFORE PENSIONISSSTE!

        📅 Fecha: Este viernes 26/07/2024  
        🕒 Hora: Hasta las 5 pm  
        🏢 Lugar: [Especifica el lugar, puede ser una sala de reuniones o virtualmente si es a través de una videollamada]

        **¿Por qué participar?**
        - Diversión Garantizada: Una excelente oportunidad para relajarnos y divertirnos juntos.
        - Conocimiento: Pondremos a prueba nuestro conocimiento sobre nuestra querida AFORE PENSIONISSSTE.
        - Premios: Habrá premios para los tres primeros ganadores. ¡No te lo puedes perder!

        **Preguntas de la Trivia:**
        1. ¿En qué año fue fundada AFORE PENSIONISSSTE?
        2. ¿Cuál es la misión principal de AFORE PENSIONISSSTE?
        3. ¿Cuántos años de operación tiene actualmente AFORE PENSIONISSSTE?
        4. ¿Qué departamento en AFORE PENSIONISSSTE se encarga de la atención al cliente?
        5. ¿Qué es una SIEFORE y cómo funciona en el contexto de AFORE PENSIONISSSTE?
        6. ¿Quién es el actual director de finanzas de AFORE PENSIONISSSTE?
        7. ¿En qué año alcanzó AFORE PENSIONISSSTE su primer millón de afiliados?

        **¿Cómo participar?**
        - Solo necesitas traer tu entusiasmo y tus ganas de pasar un buen rato.
        - Puedes prepararte revisando un poco de la historia y la estructura de nuestra empresa.
        - No necesitas ser un experto para participar; lo más importante es divertirse y compartir un buen momento con tus compañeros.

        ¡Nos vemos este viernes para una tarde de trivia, risas y premios! 🏆🎉

        Saludos,  
        Javier Horacio Pérez Ricárdez  
        Analista UEAP "B"
        
        © 2024 jahoperi. Todos los derechos reservados.
    """)

# Incrustar el formulario en Streamlit
st.title("Formulario de Perfil Profesional y Preferencias")
components.iframe(form_url, width=800, height=600, scrolling=True)
