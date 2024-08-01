import streamlit as st
import time

st.title('Testes aleatórios... (ATS)')
ultimo_ats = st.text_input('Entre com o valor do ATS da folha de 12/2007')

try:
    ultimo_ats = float(ultimo_ats)
except:
    st.stop()

CONSTANTE = 1 #1.022467733262151
calculo = 0
subsidio_anterior = 24500.00
periodos = [
    ["de 01/2008 a 08/2009", 20, 24500.00],
    ["de 09/2009 a 01/2010",  5, 25725.00],
    ["de 02/2010 a 12/2012", 35, 26723.00],
    ["de 01/2013 a 12/2013", 12, 28059.29],
    ["de 01/2014 a 12/2015", 24, 29462.25],
    ["de 01/2015 a 10/2018", 46, 33763.00],
    ["de 11/2018 a 03/2023", 53, 39293,32],
    ["de 04/2023 a 01/2024", 10, 41650.92],
    ["de 02/2024 a 07/2024",  6, 44008.52]
  ]

indice_correcao_atual = periodos[7][2]/periodos[0][2]
st.header(f'ATS atual: R$ {ultimo_ats * indice_correcao_atual:.2f}')

st.sidebar.header("Acompanhe o cálculo!")
for periodo in periodos:
  st.sidebar.write(f'Calculando valor principal para o periodo {periodo[0]}')
  st.sidebar.write(f'Multiplicando por quantidade de meses: {periodo[1]}')
  st.sidebar.write(f'Valor do subsídio considerado: R$ {periodo[2]:.2f}')
  st.sidebar.write(f'Valor do subsídio anterior: R$ {subsidio_anterior:.2f}')
  indice = periodo[2]/subsidio_anterior
  st.sidebar.write(f'Índice de aumento: {indice}')
  calculo += periodo[1] * indice * ultimo_ats * CONSTANTE
  subsidio_anterior = periodo[2]
  st.sidebar.write(f'Valor principal: R$ {calculo:.2f}')
  st.sidebar.write('---------------------------')
  time.sleep(1)

st.header(f'Valor principal: R${calculo:.2f}')