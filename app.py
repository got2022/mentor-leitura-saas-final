import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURAÇÃO DE IDENTIDADE VISUAL
st.set_page_config(page_title="Mentor de Leitura Pro", page_icon="🔵", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Logo Moderna em CSS */
    .logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-bottom: 30px;
    }
    .logo-icon {
        background: linear-gradient(135deg, #0f172a 0%, #2563eb 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 12px;
        font-weight: 800;
        font-size: 1.5rem;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
    }
    .logo-text {
        font-size: 2rem;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -1px;
    }
    
    /* Botão Dinâmico */
    div.stButton > button {
        background: #0f172a !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        font-weight: 700 !important;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: #2563eb !important;
        transform: translateY(-2px);
    }
    </style>
    
    <div class="logo-container">
        <div class="logo-icon">ML</div>
        <div class="logo-text">MENTOR DE LEITURA</div>
    </div>
    """, unsafe_allow_html=True)

# 2. CONEXÃO IA
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# 3. INTERFACE LIMPA
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### Texto Base")
    texto_base = st.text_area("Insira o material para análise profissional:", height=350, label_visibility="collapsed")

with col2:
    st.markdown("### Suporte Pedagógico")
    duvida_aluno = st.text_area("Descreva a dúvida ou o ponto de dificuldade:", height=150, label_visibility="collapsed", placeholder="O que precisa ser esclarecido?")
    st.write("---")
    if st.button("GERAR ESTRATÉGIA DE COMPREENSÃO"):
        if texto_base and api_key:
            try:
                # NOME DO MODELO CORRIGIDO PARA EVITAR ERRO 404
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt_sistema = f"""
                Atue como um Mentor de Língua Portuguesa sênior, especialista no Currículo da Rede Estadual do RJ 2026.
                Sua tarefa é mediar a leitura para um aluno, sem jargões técnicos.
                
                1. Mapeie o gênero e o propósito do texto.
                2. Apresente um plano de voo: o que o aluno deve focar para compreender a fundo (estratégias de leitura).
                3. Se houver dúvida ({duvida_aluno}), responda de forma a estimular o raciocínio, seguindo a lógica do currículo.
                
                TEXTO: {texto_base}
                """
                
                with st.spinner("Processando Matrizes Curriculares..."):
                    response = model.generate_content(prompt_sistema)
                    st.markdown("### Análise do Mentor")
                    st.info(response.text)
            except Exception as e:
                st.error(f"Erro de conexão: {e}")
        else:
            st.warning("Certifique-se de que o texto foi inserido.")
