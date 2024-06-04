import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel('Gráfico atualizado.xlsx', sheet_name='Dados Cadastrais', nrows=351)
df = df[['Nome', 'Sexo', 'Turma', 'Idade -Cálculo média']]

st.set_page_config(page_title="Home", page_icon="", layout="wide")
st.success("Outros gráficos ")

with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

idade_counts = df['Idade -Cálculo média'].value_counts().reset_index()
idade_counts.columns = ['Idade', 'Count']

fig = px.pie(idade_counts, values='Count', names='Idade', title='Média Total das Idades',color_discrete_map={'11': 'pink', '12': 'blue','13':''})
fig.update_traces(
    textposition='inside',
    textinfo='percent+label'
)
st.plotly_chart(fig, use_container_width=True)

