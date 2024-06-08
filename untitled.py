import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(

page_title="Empresa 1",
)

st.header("Dados da empresa 1")

arquivo = "https://raw.githubusercontent.com/joseagnaldo26/feito_em_aula/main/empresa1.csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe.head(3)) 

st.write("Gráfico de linhas dos indicadores ao longo do tempo")
fig, ax = plt.subplots()
dfe.plot()
st.pyplot(fig)

fig, ax = plt.subplots()
dfe.plot(kind = 'scatter', x = 'EBITDA', y = 'Lucro operacional', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
dfe["Lucro do período"].plot(kind = 'hist', ax=ax)
st.pyplot(fig)

st.write(dfe.groupby('Ano').mean())
