# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:20:32 2024

@author: jperezr
"""

import streamlit as st
import streamlit.components.v1 as components

# URL del formulario de Google Forms
form_url = "https://docs.google.com/forms/d/e/19kNQjVtZYu1WphrcqwWU0byg3zvpBmM5DrMcbLFwVIw/viewform"

# Incrustar el formulario en Streamlit
st.title("Formulario de Google en Streamlit")
components.iframe(form_url, width=800, height=600, scrolling=True)
