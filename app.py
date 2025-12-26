import streamlit as st
import google.generativeai as genai
import os

# 1. IDENTIDADE VISUAL HIGH-TECH (Cores Modernas e Vibrantes)
st.set_page_config(
    page_title="Mentor de Redação | Pro AI",
    page_icon="https://cdn-icons-png.flaticon.com/512/2643/2643506.png",
    layout="centered"
)

# Estilização: Gradientes e Cores Vibrantes (Electric Blue & Modern Purple)
st.markdown("""
    <style>
    /* Fundo Moderno */
    .main { background-color: #ffffff; }
    
    /* Título com Gradiente Moderno */
    .titulo-moderno {
        font-size: 42px;
        font-weight: 800;
        background: -webkit-linear-gradient(#6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -2px;
    }

    /* Botão com Gradiente Vibrante e Efeito de Sombra */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%);
        color: #ffffff;
        border-radius: 12px;
        border: none;
        padding: 1rem 2rem;
        font-size: 18px;
        font-weight: 700;
        width: 100%;
        box-shadow: 0 10px 15px -3px rgba(124, 58, 237, 0.3);
        transition: all 0.4s ease;
    }
    
    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        box-shadow: 0 20px 25px -5px rgba(124, 58, 237, 0.4);
        color: #ffffff;
    }

    /* Estilização da Sidebar (Barra Lateral) */
    [data-testid="stSidebar"] {
        background-color: #f1f5f9;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM A CHAVE
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# 3. INTERFACE (Texto Pedagógico Corrigido)
st.markdown('<h1 class="titulo-moderno">Mentor de Redação</h1>', unsafe_allow_html=True)
st.markdown("<p style='color: #475569; font-size: 1.2rem; font-weight: 500;'>Análise Avançada e Devolutivas Pedagógicas</p>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Configurações")
    nivel = st.selectbox("Nível de Ensino:", ["Ensino Fundamental II", "Ensino Médio (Modelo ENEM)"])

st.markdown("---")
texto_aluno = st.text_area("Insira a produção textual do aluno para análise:", height=350)

if st.button("🚀 GERAR DEVOLUTIVA PEDAGÓGICA"):
    if texto_aluno and api_key:
        with st.spinner("O Mentor está processando a análise..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Atue como um mentor pedagógico especialista em língua portuguesa. Analise para o nível {nivel} o seguinte texto, fornecendo uma devolutiva pedagógica clara: {texto_aluno}"
            response = model.generate_content(prompt)
            st.success("Análise Concluída!")
            st.markdown(response.text)
    else:
        st.error("Por favor, insira o texto para análise.")
