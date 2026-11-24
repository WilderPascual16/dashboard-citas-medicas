import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(
    page_title="Gestión de Citas Médicas",
    page_icon="🏥",
    layout="wide")
# Cargar datos
df = pd.read_csv('citas_medicas.csv')
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month

# Título
st.title('🏥 Dashboard de Gestión de Citas Médicas')
st.write('Análisis de citas médicas - Hospital de Lima Norte')

# Indicadores
total = len(df)
atendidas = (df['estado'] == 'Atendida').sum()
canceladas = (df['estado'] == 'Cancelada').sum()
ausencias = (df['estado'] == 'No asistió').sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de citas", total)
col2.metric("Atendidas", atendidas)
col3.metric("Canceladas", canceladas)
col4.metric("No asistió", ausencias)

st.divider()

# Gráfico 1: Citas por especialidad
st.subheader('📊 Citas por Especialidad')

especialidades = df['especialidad'].value_counts().reset_index()
especialidades.columns = ['especialidad', 'cantidad']

fig1 = px.bar(
    especialidades,
    x='especialidad',
    y='cantidad',
    color='especialidad',
    title='Demanda por especialidad médica'
)

st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Estado de las citas
st.subheader('🥧 Estado de las Citas')

fig2 = px.pie(
    df,
    names='estado',
    title='Distribución de estados de citas',
    hole=0.35
)

st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Citas por mes
st.subheader('📈 Tendencia de Citas por Mes')

citas_mes = df.groupby('mes').size().reset_index(name='cantidad')

fig3 = px.line(
    citas_mes,
    x='mes',
    y='cantidad',
    markers=True,
    title='Tendencia mensual de citas'
)

st.plotly_chart(fig3, use_container_width=True)

# Tabla de datos
st.subheader('📋 Registro de Citas Médicas')
st.dataframe(df, use_container_width=True)

st.caption('Proyecto académico - Business Intelligence and Big Data')
