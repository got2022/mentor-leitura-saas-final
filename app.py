import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURAÇÃO DE DESIGN (CLARO E MODERNO)
st.set_page_config(page_title="Mentor de Leitura", page_icon="🔵", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8fafc; }
    
    .main { background-color: #f8fafc; }
    
    /* Logo com cores vivas mas fundo claro */
    .logo-container {
        display: flex; align-items: center; justify-content: center;
        gap: 12px; padding: 20px; background: white;
        border-bottom: 1px solid #e2e8f0; margin-bottom: 30px;
    }
    .logo-icon {
        background: #2563eb; color: white; padding: 8px 15px;
        border-radius: 10px; font-weight: 800; font-size: 1.2rem;
    }
    .logo-text { font-size: 1.8rem; font-weight: 800; color: #1e293b; }
    
    /* Estilo dos Cards de Resposta */
    .stAlert { background-color: white !important; border: 1px solid #e2e8f0 !important; color: #1e293b !important; border-radius: 12px !important; }
    
    /* Botão Principal */
    div.stButton > button {
        background: #2563eb !important; color: white !important;
        border-radius: 8px !important; font-weight: 700 !important;
        width: 100%; height: 3.5rem; border: none !important;
    }
    </style>
    
    <div class="logo-container">
        <div class="logo-icon">ML</div>
        <div class="logo-text">MENTOR DE LEITURA PRO</div>
    </div>
    """, unsafe_allow_html=True)

# 2. CONEXÃO IA (VERSÃO PARA EVITAR ERRO 404)
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# 3. INTERFACE DE USUÁRIO
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("#### 📄 Texto para análise")
    texto_base = st.text_area("Insira o texto aqui:", height=350, label_visibility="collapsed", placeholder="Cole aqui o texto que o aluno vai ler...")

with col2:
    st.markdown("#### 🧠 Dúvida ou Dificuldade")
    duvida_aluno = st.text_area("O que precisa de ajuda?", height=150, label_visibility="collapsed", placeholder="Ex: Não entendi a ironia do autor...")
    st.write("---")
    botao = st.button("GERAR PLANO DE LEITURA")

# 4. LÓGICA DO MENTOR (CURRÍCULO RJ 2026 + ACESSIBILIDADE)
if botao:
    if not texto_base:
        st.error("Por favor, insira um texto para que o Mentor possa trabalhar.")
    else:
        try:
            # Usando a chamada de modelo mais estável
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Você é um Mentor de Leitura especialista no Currículo 2026 da SEEDUC-RJ.
            Sua missão é criar um 'Mapa de Navegação' para o aluno.
            
            DIRETRIZES PEDAGÓGICAS:
            1. Identifique o Gênero Textual.
            2. Crie um 'Plano de Voo' com 3 passos simples (O que ver na superfície, o que inferir e qual a intenção).
            3. Responda à dúvida: {duvida_aluno} de forma clara.
            4. ACESSIBILIDADE: Use frases curtas, negritos em palavras-chave e uma estrutura organizada (ótimo para TDAH e Autistas).
            
            TEXTO: {texto_base}
            """
            
            with st.spinner("O Mentor está traçando as estratégias..."):
                # Chamada direta para evitar problemas de versão
                response = model.generate_content(prompt)
                st.markdown("### 👨‍🏫 Orientação do Mentor")
                st.success(response.text)
                
        except Exception as e:
            st.error(f"Ocorreu um ajuste necessário na conexão. Erro: {e}")
            st.info("Dica: Verifique se a sua GOOGLE_API_KEY está correta no painel do Render.")
