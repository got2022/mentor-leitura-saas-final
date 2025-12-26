import streamlit as st
import google.generativeai as genai
import os

# 1. IDENTIDADE VISUAL CORPORATIVA (Configurações da Aba)
st.set_page_config(
    page_title="Mentor de Redação | Enterprise",
    page_icon="https://cdn-icons-png.flaticon.com/512/2643/2643506.png",
    layout="centered"
)

# Estilização High-End (CSS para retirar o aspeto "pobre")
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    /* Botão de Ação Dark Blue - Estilo Software de Gestão */
    div.stButton > button:first-child {
        background-color: #0f172a;
        color: #ffffff;
        border-radius: 6px;
        border: none;
        padding: 0.8rem 2.5rem;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    div.stButton > button:first-child:hover {
        background-color: #1e293b;
        color: #38bdf8;
        border: none;
    }
    
    /* Títulos e Tipografia Profissional */
    h1 { 
        color: #0f172a; 
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        padding-bottom: 0px;
    }
    .stTextArea label {
        font-weight: 700;
        color: #334155;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM A CHAVE (Configurada no Render)
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# 3. INTERFACE DO UTILIZADOR
st.title("Mentor de Redação Inteligente")
st.markdown("<p style='color: #64748b; font-size: 1.1em;'>Análise Pedagógica Avançada e Devolutivas Académicas</p>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Parâmetros de Avaliação")
    nivel = st.selectbox("Nível de Ensino:", ["Ensino Fundamental II", "Ensino Médio (Modelo ENEM)"])

texto_aluno = st.text_area("Insira a produção textual para análise:", height=350)

if st.button("Executar Análise Profissional"):
    if texto_aluno and api_key:
        with st.spinner("A processar análise de acordo com as competências..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Atue como um corretor especialista. Analise detalhadamente para o nível {nivel} o texto: {texto_aluno}"
            response = model.generate_content(prompt)
            st.markdown("---")
            st.markdown(response.text)
    else:
        st.error("Erro: Certifique-se de que o texto foi inserido corretamente.")
