# COMANDOS
#----------

import streamlit as st
import pandas as pd
import numpy as np
#pip install openpyxl
#import openpyxl


# DATOS
#------

datos = pd.read_csv('Datos/datos_prueba.csv', sep = ';')

df = pd.DataFrame(datos)
st.dataframe(df)

# DISEÑO DE PÁGINA
#-----------------
st.set_page_config(page_title="Nichos estratégicos - Perú 2023")



# BARRA PARA SELECCIONAR
#st.sidebar.[df('Perfil')]
#with st.sidebar:
#        st.[df('Perfil')]


# MINI BOX
#add_selectbox = st.sidebar.selectbox(
#        "COPEME - Área de Microfinanzas",
#        ("Email", "Teléfono")
#        )
