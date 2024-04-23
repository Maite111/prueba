# COMANDOS


import streamlit as st
import pandas as pd
import numpy as np

# DATOS
# Caso de Excel
# df = pd.read_excel('ejemplo.xlsx')
# st.dataframe(df)

# Caso dta
#data = pd.read_stata('../ejemplo.dta')

# Caso handmade
#dict0 = { "Perfil": ['Pobre','MYPE','Independiente','Mujeres','Jovenes','Adultos Mayores','Poblacion Rural','Trabajador Agropecuario','Trabajador Informal'],
#        "Pobre": [3869919.1931554,1880253.790052403,929699.1376128423,1630451.399803889,878948.0006935216,422193.8053392285,1127629.840202049,1465313.411609893,3495458.159066423],
#        "MYPE": [1880253.790052403,7109947.800366393,3961806.227311958,3134827.50865025,878410.9828212112,1503983.771521388,1792916.917330891,2006105.002334783,5975203.648940774],
#        "Independiente": [929699.1376128423,3961806.227311958,3961806.227311958,1741392.912559784,592345.3239370844,836968.8295566433,568795.7486348999,556173.9507537984,3466036.67498944],
#        "Mujeres": [1630451.399803889,3134827.50865025,1741392.912559784,7365844.509326616,1544577.470370132,987185.9638096489,1371035.110920291,1501075.525548978,5336047.607775525],
#        "Jovenes adultos": [878948.0006935216,878410.9828212112,592345.3239370844,1544577.470370132,3415615.54926902,0,534472.5070395255,542986.8414396249,2430931.429301451],
#        "Adultos mayores": [422193.8053392285,1503983.771521388,836968.8295566433,987185.9638096489,0,2334529.787164389,612258.9950082281,809709.6253915974,1813920.35153297],
#        "Población rural": [1127629.840202049,1792916.917330891,568795.7486348999,1371035.110920291,534472.5070395255,612258.9950082281,3133246.764851849,2292714.635633172,2935661.182258477],
#        "Trabajador agropecuario": [1465313.411609893,2006105.002334783,556173.9507537984,1501075.525548978,542986.8414396249,809709.6253915974,2292714.635633172,3667967.928211046,3412246.10599272],
#        "Trabajador informal": [3495458.159066423,5975203.648940774,3466036.67498944,5336047.607775525,2430931.429301451,1813920.35153297,2935661.182258477,3412246.10599272,11586715.45777703]}

#df = pd.DataFrame(dict0)
#st.dataframe(df)

dict = { "Perfil": ['Pobre','MYPE','Independiente','Mujeres','Jovenes','Adultos Mayores','Poblacion Rural','Trabajador Agropecuario','Trabajador Informal'],
        "Pobre": [1,.2644539513996866,.2346654743494694,.2213529484283051,.2573322401233436,.1808474698676008,.3598918070710487,.3994891559274241,.301678087444554],
        "MYPE": [.4858638375131828,1,1,.4255896937114187,.2571750157915756,.6442341321967818,.572223336330698,.5469254479859118,.5156943458838635],
        "Independiente": [.2402373515336368,.5572201566807278,1,.2364145632391284,.173422715581633,.3585170916038121,.1815355735831405,.1516299928568507,.2991388446208049],
        "Mujeres": [.4213140684403993,.4409072466732744,.4395452005085318,1,.4522105746651401,.4228628691042419,.4375764865698723,.4092389996117244,.460531513630462],
        "Jovenes adultos": [.2271230888355726,.1235467555438233,.1495139565013467,.2096945527989887,1,0,.1705810448877292,.1480347844002148,.2098033250371921],
        "Adultos mayores": [.1090962845131105,.2115323225641522,.2112594058201876,.134022101954457,0,1,.1954072056744557,.2207515554222721,.1565517301381094],
        "Población rural": [.2913833038675462,.2521701941663337,.1435698052857122,.1861341369865043,.1564791175499563,.2622622330092013,1,.6250639810668637,.2533643976117542],
        "Trabajador agropecuario": [.3786418626522087,.2821546737982245,.1403839357209442,.2037886522921193,.1589718847473423,.346840562859171,.7317376535268137,1,.2944964099987813],
        "Trabajador informal": [.9032380224498553,.8404004947311788,.8748627459604728,.7244312041910514,.7117110793753406,.7769960192867054,.9369390292491965,.9302824268850554,1]}

df = pd.DataFrame(dict)
st.dataframe(df)

# BARRA PARA SELECCIONAR
st.sidebar.[df]
with st.sidebar:
        st.[df('Perfil')]


# MINI BOX
add_selectbox = st.sidebar.selectbox(
        "COPEME - Área de Microfinanzas",
        ("Email", "Teléfono")
        )


