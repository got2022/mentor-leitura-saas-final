import streamlit as st
import google.generativeai as genai
import os

# 1. DESIGN MANTIDO (EXATAMENTE COMO VOCÊ GOSTOU)
st.set_page_config(page_title="Mentor de Leitura Pro", page_icon="🧩", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;700;800&display=swap');
    .main { background-color: #020617; background-image: radial-gradient(#1e293b 0.5px, transparent 0.5px); background-size: 30px 30px; }
    .header-card { background: linear-gradient(135deg, #1e1b4b 0%, #020617 100%); padding: 50px; border-radius: 0 0 50px 50px; text-align: center; border-bottom: 2px solid #3730a3; margin-bottom: 40px; }
    .logo-main { font-family: 'Sora', sans-serif; font-weight: 800; font-size: 3.5rem; background: linear-gradient(to right, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -3px; }
    .stTextArea textarea { background-color: #0f172a !important; color: #f1f5f9 !important; border: 1px solid #334155 !important; border-radius: 15px !important; }
    div.stButton > button { background: linear-gradient(90deg, #4f46e5, #9333ea) !important; color: white !important; font-weight: 700 !important; border-radius: 12px !important; border: none !important; padding: 25px !important; width: 100%; text-transform: uppercase; }
    </style>
    <div class="header-card">
        <div class="logo-main">MENTOR DE LEITURA</div>
        <p style="color: #94a3b8; font-size: 1.1rem;">Especialista em BNCC & Neurodiversidade • SEEDUC-RJ</p>
    </div>
    """, unsafe_allow_html=True)

# 2. CONEXÃO ESTÁVEL (CORREÇÃO DO ERRO 404)
api_key = os.getenv("GOOGLE_API_KEY")

# Esta é a forma correta e atualizada de inicializar o modelo
if api_key:
    genai.configure(api_key=api_key)
    # Usamos apenas o nome do modelo, sem prefixos v1beta
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Chave API não encontrada.")

# 3. BARRA LATERAL
with st.sidebar:
    st.markdown("### 🧩 ACESSIBILIDADE")
    modo_inclusivo = st.toggle("ATIVAR APOIO TDAH / TEA")
    if modo_inclusivo:
        st.info("🌈 MODO INCLUSIVO ATIVO")

# 4. ÁREA DE TRABALHO
c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown("<h4 style='color:#818cf8'>📄 TEXTO DA AULA</h4>", unsafe_allow_html=True)
    texto_base = st.text_area("input_texto", label_visibility="collapsed", height=300)
with c2:
    st.markdown("<h4 style='color:#818cf8'>💡 DÚVIDA</h4>", unsafe_allow_html=True)
    duvida = st.text_input("input_duvida", label_visibility="collapsed")
    st.write("###")
    if st.button("ATIVAR MENTOR"):
        if texto_base:
            try:
                # Prompt simplificado para evitar erros de processamento
                contexto = "Aja como Mentor Inclusivo (TDAH/TEA)." if modo_inclusivo else "Aja como Mentor BNCC RJ."
                prompt = f"{contexto} Analise: {texto_base}. Responda: {duvida}"
                
                with st.spinner("🚀 Mentor processando..."):
                    # Chamada simplificada
                    response = model.generate_content(prompt)
                    st.markdown(f"""<div style="background: white; padding: 20px; border-radius: 15px; color: #1e293b; border-left: 8px solid #4f46e5;">{response.text}</div>""", unsafe_allow_html=True)
            except Exception as e:
                # Se der erro aqui, a chave tem algum bloqueio no Google Cloud
                st.error(f"Erro na IA: {e}")
