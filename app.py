import streamlit as st
import google.generativeai as genai
import os

# 1. DESIGN E PROPRIEDADE (SEM SEEDUC-RJ)
st.set_page_config(page_title="Mentor de Leitura Pro", page_icon="🧩", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;700;800&display=swap');
    .main { background-color: #020617; }
    .header-card { background: linear-gradient(135deg, #1e1b4b 0%, #020617 100%); padding: 50px; border-radius: 0 0 50px 50px; text-align: center; border-bottom: 2px solid #3730a3; margin-bottom: 40px; }
    .logo-main { font-family: 'Sora', sans-serif; font-weight: 800; font-size: 3.5rem; background: linear-gradient(to right, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -3px; }
    .stTextArea textarea, .stTextInput input { background-color: #0f172a !important; color: white !important; border: 1px solid #334155 !important; border-radius: 15px !important; }
    div.stButton > button { background: linear-gradient(90deg, #4f46e5, #9333ea) !important; color: white !important; font-weight: 700 !important; border-radius: 12px !important; border: none !important; padding: 20px !important; width: 100%; text-transform: uppercase; }
    .resposta-box { background: white; padding: 25px; border-radius: 20px; color: #1e293b; border-left: 10px solid #4f46e5; margin-top: 20px; font-size: 18px; line-height: 1.6; }
    </style>
    
    <div class="header-card">
        <div class="logo-main">MENTOR DE LEITURA</div>
        <p style="color: #94a3b8; font-size: 1.1rem;">Especialista em BNCC & Neurodiversidade</p>
    </div>
    """, unsafe_allow_html=True)

# 2. CONEXÃO ESTÁVEL (MATANDO O ERRO 404 V1BETA)
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    # Esta configuração ignora versões v1beta automaticamente
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Chave API não configurada no Render.")

# 3. SIDEBAR DE ACESSIBILIDADE (🧩)
with st.sidebar:
    st.markdown("### 🧩 ACESSIBILIDADE")
    modo_inclusivo = st.toggle("ATIVAR APOIO TDAH / TEA")
    st.markdown("---")
    st.caption("Focado no Currículo 2026")

# 4. INTERFACE PRINCIPAL
c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown("<h4 style='color:#818cf8'>📄 TEXTO DA AULA</h4>", unsafe_allow_html=True)
    texto_base = st.text_area("in_txt", label_visibility="collapsed", height=300, placeholder="Cole o conteúdo aqui...")
with c2:
    st.markdown("<h4 style='color:#818cf8'>💡 DÚVIDA</h4>", unsafe_allow_html=True)
    duvida = st.text_input("in_dv", label_visibility="collapsed", placeholder="Sua pergunta pedagógica...")
    st.write("###")
    if st.button("ATIVAR MENTOR"):
        if texto_base:
            try:
                diretiva = "Responda como mentor para TDAH/TEA." if modo_inclusivo else "Responda como especialista BNCC."
                prompt = f"{diretiva} Analise o texto: {texto_base}. Responda à dúvida: {duvida}"
                
                with st.spinner("🚀 Mentor processando..."):
                    # Chamada direta e estável
                    response = model.generate_content(prompt)
                    st.markdown(f'<div class="resposta-box"><b>Orientação do Mentor:</b><br><br>{response.text}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erro na IA: {e}")
