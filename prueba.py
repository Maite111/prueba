# COMANDOS


import streamlit as st
import pandas as pd
import numpy as np

# Caso de Excel
# df = pd.read_excel('ejemplo.xlsx')
# st.dataframe(df)

# Caso dta
#data = pd.read_stata('../ejemplo.dta')

# Caso handmade
dict = { "Perfil": ['Pobre','MYPE','Independiente','Mujeres','Jovenes','Adultos Mayores','Poblacion Rural','Trabajador Agropecuario','Trabajador Informal'],
        "Pobre": [3869919.1931554,1880253.790052403,929699.1376128423,1630451.399803889,878948.0006935216,422193.8053392285,1127629.840202049,1465313.411609893,3495458.159066423],
        "MYPE": [1880253.790052403,7109947.800366393,3961806.227311958,3134827.50865025,878410.9828212112,1503983.771521388,1792916.917330891,2006105.002334783,5975203.648940774],
        "Independiente": [929699.1376128423,3961806.227311958,3961806.227311958,1741392.912559784,592345.3239370844,836968.8295566433,568795.7486348999,556173.9507537984,3466036.67498944],
        "Mujeres": [1630451.399803889,3134827.50865025,1741392.912559784,7365844.509326616,1544577.470370132,987185.9638096489,1371035.110920291,1501075.525548978,5336047.607775525],
        "Jovenes adultos": [878948.0006935216,878410.9828212112,592345.3239370844,1544577.470370132,3415615.54926902,0,534472.5070395255,542986.8414396249,2430931.429301451],
        "Adultos mayores": [422193.8053392285,1503983.771521388,836968.8295566433,987185.9638096489,0,2334529.787164389,612258.9950082281,809709.6253915974,1813920.35153297],
        "Población rural": [1127629.840202049,1792916.917330891,568795.7486348999,1371035.110920291,534472.5070395255,612258.9950082281,3133246.764851849,2292714.635633172,2935661.182258477],
        "Trabajador agropecuario": [1465313.411609893,2006105.002334783,556173.9507537984,1501075.525548978,542986.8414396249,809709.6253915974,2292714.635633172,3667967.928211046,3412246.10599272],
        "Trabajador informal": [3495458.159066423,5975203.648940774,3466036.67498944,5336047.607775525,2430931.429301451,1813920.35153297,2935661.182258477,3412246.10599272,11586715.45777703]}

df = pd.DataFrame(dict)
st.dataframe(df)
st.data_editor(
        hide_index=True,
)





