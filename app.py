import streamlit as st
import google.generativeai as genai
import os

# CONFIGURAÇÃO DA INTERFACE (Limpa e Moderna)
st.set_page_config(page_title="Mentor de Leitura", layout="wide")

st.markdown("""
    <style>
    .titulo { font-size: 2.5rem; font-weight: 800; color: #1e3a8a; text-align: center; }
    .stButton > button { background: #2563eb; color: white; border-radius: 8px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# CONEXÃO COM A IA
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

st.markdown('<h1 class="titulo">📖 Meu Mentor de Leitura</h1>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📄 Texto para leitura")
    texto_base = st.text_area("Cole o texto aqui:", height=300)
    genero_informado = st.text_input("Qual o gênero? (Opcional)", placeholder="Ex: Crônica, Notícia...")

with col2:
    st.subheader("❓ Minha dúvida")
    duvida_aluno = st.text_area("O que você não entendeu ou quer saber?", height=150)
    st.write("---")
    botao = st.button("PEDIR AJUDA AO MENTOR")

if botao and texto_base:
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    # INSTRUÇÕES TÉCNICAS ESCONDIDAS (Baseadas no Currículo RJ 2026 e Matrizes)
    prompt_sistema = f"""
    Você é um Mentor de Leitura. Seu aluno forneceu um texto e talvez uma dúvida.
    Siga o Currículo de Língua Portuguesa da Rede Estadual do RJ (2026).
    
    1. Identifique o texto e o gênero para o aluno.
    2. Liste estratégias de leitura (O que observar no nível Literal, Inferencial e Crítico) sem usar esses nomes técnicos.
    3. Responda à dúvida do aluno de forma mediadora, baseada nos descritores do SAEB e nas características do gênero {genero_informado}.
    
    Texto: {texto_base}
    Dúvida: {duvida_aluno}
    """
    
    with st.spinner("O Mentor está preparando o seu plano..."):
        response = model.generate_content(prompt_sistema)
        st.markdown("### 👨‍🏫 Orientação do Mentor")
        st.write(response.text)


                
           
