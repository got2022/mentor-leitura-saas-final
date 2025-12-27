import streamlit as st
import google.generativeai as genai
import os

# 1. DESIGN E PROPRIEDADE (LIMPO E SEM INFORMAÇÕES IRRELEVANTES)
st.set_page_config(page_title="Mentor de Leitura Pro", page_icon="🧩", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;700;800&display=swap');
    .main { background-color: #020617; }
    .header-card { background: linear-gradient(135deg, #1e1b4b 0%, #020617 100%); padding: 50px; border-radius: 0 0 50px 50px; text-align: center; border-bottom: 2px solid #3730a3; margin-bottom: 40px; }
    .logo-main { font-family: 'Sora', sans-serif; font-weight: 800; font-size: 3.5rem; background: linear-gradient(to right, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -3px; }
    .stTextArea textarea, .stTextInput input { background-color: #0f172a !important; color: white !important; border: 1px solid #334155 !important; border-radius: 15px !important; }
    div.stButton > button { background: linear-gradient(90deg, #4f46e5, #9333ea) !important; color: white !important; font-weight: 700 !important; border-radius: 12px !important; padding: 20px !important; width: 100%; text-transform: uppercase; }
    .resposta-box { background: white; padding: 25px; border-radius: 20px; color: #1e293b; border-left: 10px solid #4f46e5; margin-top: 20px; min-height: 100px; font-size: 18px; }
    </style>
    
    <div class="header-card">
        <div class="logo-main">MENTOR DE LEITURA</div>
        <p style="color: #94a3b8; font-size: 1.1rem;">Especialista em BNCC & Neurodiversidade</p>
    </div>
    """, unsafe_allow_html=True)

# 2. CONEXÃO BLINDADA CONTRA ERRO 404 (V1BETA)
api_key = os.getenv("GOOGLE_API_KEY")
model = None

if api_key:
    try:
        # Configuração para ignorar a versão v1beta
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Erro na configuração da chave: {e}")
else:
    st.error("Chave API não configurada no Render.")

# 3. BARRA LATERAL (APENAS O QUE IMPORTA)
with st.sidebar:
    st.markdown("### 🧩 ACESSIBILIDADE")
    modo_inclusivo = st.toggle("ATIVAR APOIO TDAH / TEA")

# 4. ÁREA DE TRABALHO
c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown("<h4 style='color:#818cf8'>📄 TEXTO DA AULA</h4>", unsafe_allow_html=True)
    texto_base = st.text_area("txt_area", label_visibility="collapsed", height=300)
with c2:
    st.markdown("<h4 style='color:#818cf8'>💡 DÚVIDA</h4>", unsafe_allow_html=True)
    duvida = st.text_input("dv_input", label_visibility="collapsed")
    st.write("###")
    
    if st.button("ATIVAR MENTOR"):
        if not texto_base:
            st.warning("Por favor, cole um texto para análise.")
        elif not model:
            st.error("O modelo de IA não foi carregado corretamente.")
        else:
            try:
                # Prompt direto para evitar processamento longo
                instrucao = "Aja como mentor pedagógico. "
                if modo_inclusivo: instrucao += "Use linguagem clara para TDAH/TEA. "
                
                with st.spinner("🚀 Mentor processando..."):
                    # Chamada simplificada para evitar o erro v1beta
                    response = model.generate_content(f"{instrucao}\nTexto: {texto_base}\nPergunta: {duvida}")
                    st.markdown(f'<div class="resposta-box"><b>Orientação:</b><br><br>{response.text}</div>', unsafe_allow_html=True)
            except Exception as e:
                # Exibe o erro de forma mais limpa
                st.error(f"Ocorreu um problema na resposta: {e}")
