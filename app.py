import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURAÇÃO DE ALTO NÍVEL (DESIGN E FAVICON)
st.set_page_config(
    page_title="Mentor de Leitura Pro", 
    page_icon="🧩", 
    layout="wide"
)

# CSS Customizado para Design Elegante
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;700;800&display=swap');
    
    .main {
        background-color: #020617;
        background-image: radial-gradient(#1e293b 0.5px, transparent 0.5px);
        background-size: 30px 30px;
    }
    
    .header-card {
        background: linear-gradient(135deg, #1e1b4b 0%, #020617 100%);
        padding: 50px;
        border-radius: 0 0 50px 50px;
        text-align: center;
        border-bottom: 2px solid #3730a3;
        margin-bottom: 40px;
    }

    .logo-main {
        font-family: 'Sora', sans-serif;
        font-weight: 800;
        font-size: 3.5rem;
        background: linear-gradient(to right, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -3px;
    }

    /* Estilo dos Inputs */
    .stTextArea textarea {
        background-color: #0f172a !important;
        color: #f1f5f9 !important;
        border: 1px solid #334155 !important;
        border-radius: 15px !important;
        font-size: 16px !important;
    }

    /* Botão de Ativação Premium */
    div.stButton > button {
        background: linear-gradient(90deg, #4f46e5, #9333ea) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 25px !important;
        width: 100%;
        transition: 0.4s;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    div.stButton > button:hover {
        box-shadow: 0 0 25px rgba(139, 92, 246, 0.5);
        transform: translateY(-2px);
    }
    </style>
    
    <div class="header-card">
        <div class="logo-main">MENTOR DE LEITURA</div>
        <p style="color: #94a3b8; font-size: 1.1rem;">Especialista em BNCC & Neurodiversidade • SEEDUC-RJ</p>
    </div>
    """, unsafe_allow_html=True)

# 2. CONEXÃO BLINDADA (SEM V1BETA)
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        # Forçamos a configuração sem passar versão beta no model_name
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Chave API ausente no Render.")
except Exception as e:
    st.error(f"Erro na Inicialização: {e}")

# 3. BARRA LATERAL (MENU DA INCLUSÃO)
with st.sidebar:
    st.markdown("### 🧩 ACESSIBILIDADE")
    st.write("Configurações para alunos neurodivergentes.")
    
    # Toggle colorido para inclusão
    modo_inclusivo = st.toggle("ATIVAR APOIO TDAH / TEA")
    
    if modo_inclusivo:
        st.info("🌈 MODO INCLUSIVO ATIVO: O Mentor usará linguagem simplificada e visual adaptado.")
    
    st.markdown("---")
    st.markdown("🔒 **Versão Beta Aberta 2026**")

# 4. ÁREA DE TRABALHO
c1, c2 = st.columns(2, gap="large")

with c1:
    st.markdown("<h4 style='color:#818cf8'>📄 TEXTO DA AULA</h4>", unsafe_allow_html=True)
    texto_base = st.text_area("input_texto", label_visibility="collapsed", height=350, placeholder="Cole aqui o conteúdo da folha ou livro...")

with c2:
    st.markdown("<h4 style='color:#818cf8'>💡 O QUE VOCÊ PRECISA?</h4>", unsafe_allow_html=True)
    duvida = st.text_input("input_duvida", label_visibility="collapsed", placeholder="Sua dúvida para o Mentor...")
    st.write("###") # Espaçador
    if st.button("ATIVAR MENTOR"):
        if not texto_base:
            st.error("Por favor, insira o texto primeiro.")
        else:
            try:
                # Personalização baseada na BNCC e Inclusão
                diretriz = (
                    "Aja como Mentor Inclusivo para TDAH/TEA. Use frases curtas, "
                    "sem metáforas e linguagem denotativa (literal)." 
                    if modo_inclusivo else 
                    "Aja como Mentor Pedagógico da Rede RJ. Foco em descritores BNCC, inferência e análise."
                )
                
                prompt = f"{diretriz}\n\nTexto: {texto_base}\nDúvida: {duvida}"
                
                with st.spinner("🚀 Mentor processando..."):
                    # Chamada direta e estável
                    response = model.generate_content(prompt)
                    st.markdown("---")
                    st.markdown(f"""
                        <div style="background: white; padding: 25px; border-radius: 20px; color: #1e293b; border-left: 8px solid #4f46e5;">
                            <h3 style="margin-top:0">👨‍🏫 Orientação do Mentor:</h3>
                            {response.text}
                        </div>
                    """, unsafe_allow_html=True)
            except Exception as e:
                st.error("Erro na resposta da IA. Verifique se a chave API no Render está correta e sem espaços.")
