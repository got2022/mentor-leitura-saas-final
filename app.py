import streamlit as st
import google.generativeai as genai
import os

# Configuração da Página
st.set_page_config(page_title="Mentor de Redação Pro", page_icon="📝")

# Conexão com a chave que você salvou no Render
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Interface do App
st.title("📚 Mentor de Redação Inteligente")

with st.sidebar:
    st.header("Configurações")
    nivel = st.selectbox("Nível de Ensino:", ["Fundamental (6º ao 9º)", "Ensino Médio (ENEM)"])

# Área de Texto
texto_aluno = st.text_area("Cole a redação do aluno aqui:", height=300)

if st.button("🚀 Analisar Redação"):
    if texto_aluno and api_key:
        with st.spinner("Analisando..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Atue como mentor pedagógico para {nivel}. Analise o texto: {texto_aluno}"
            response = model.generate_content(prompt)
            st.markdown(response.text)
    else:
        st.error("Por favor, cole o texto ou verifique a chave no Render.")
