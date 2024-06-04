import streamlit as st
import pandas as pd
import plotly.express as px


tabela = pd.read_excel('Gráfico atualizado.xlsx', sheet_name='Aptidão Física', nrows=350)
tabela = tabela[['Nome', 'Turma', 'Salto horizontal 1', 'Salto horizontal 2', 'Salto vertical', 'Salto vertical 1', 'Salto vertical 2']]


st.set_page_config(page_title="Home", page_icon="", layout="wide")
st.success("Gráfico de força ")


with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


selected_aluno = st.selectbox('Selecione o aluno', tabela['Nome'].unique())
aluno_data = tabela[tabela['Nome'] == selected_aluno]


selected_turma = aluno_data['Turma'].values[0]
turma_data = tabela[tabela['Turma'] == selected_turma]

# Selecionar colunas para exibir
colunas_disponiveis = ['Salto horizontal 1', 'Salto horizontal 2', 'Salto vertical', 'Salto vertical 1', 'Salto vertical 2']
colunas_selecionadas = st.multiselect("Selecione as colunas para exibir", colunas_disponiveis, default=colunas_disponiveis)


st.write("### Todos os Dados")
st.dataframe(tabela[['Nome'] + colunas_selecionadas])


st.write("### Dados do Aluno Selecionado")
st.dataframe(aluno_data[['Nome'] + colunas_selecionadas])


turma_mean = turma_data[colunas_selecionadas].mean().reset_index()
turma_mean.columns = ['Métrica', 'Média da Turma']


aluno_data_selecionadas = aluno_data[colunas_selecionadas].melt(var_name='Métrica', value_name='Valor do Aluno')
aluno_data_selecionadas['Nome'] = selected_aluno


comparacao_df = pd.merge(aluno_data_selecionadas, turma_mean, on='Métrica')


if colunas_selecionadas:
    fig = px.bar(aluno_data, x='Nome', y=colunas_selecionadas, barmode='group', title='Dados de Força do aluno') 
    st.plotly_chart(fig, use_container_width=True)

if colunas_selecionadas:
    fig = px.bar(comparacao_df, x='Métrica', y=['Valor do Aluno', 'Média da Turma'], barmode='group', title=f'Comparação de Força do Aluno ({selected_aluno}) com a Média da Turma ({selected_turma})')
    st.plotly_chart(fig, use_container_width=True)
#usar para rodar > python -m streamlit run Home.py
