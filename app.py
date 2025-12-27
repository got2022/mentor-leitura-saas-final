import streamlit as st
import google.generativeai as genai
import os

# 1. DESIGN CLARO E ACESSÍVEL (PEDAGÓGICO)
st.set_page_config(page_title="Mentor de Leitura", page_icon="📖")

st.markdown("""
    <style>
    /* Fundo claro para não cansar a vista */
    .main { background-color: #ffffff; }
    
    /* Título elegante e sério */
    .titulo { 
        color: #1e3a8a; 
        font-size: 32px; 
        font-weight: 800; 
        text-align: center;
        padding: 20px;
        border-bottom: 2px solid #e5e7eb;
    }
    
    /* Botão de Ativação */
    div.stButton > button {
        background-color: #1e3a8a !important;
        color: white !important;
        height: 3em;
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    <div class="titulo">📚 MENTOR DE LEITURA PRO</div>
    """, unsafe_allow_html=True)

# 2. CONEXÃO SEGURA COM A IA (SEM ERRO 404)
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # Mudança estratégica para evitar o erro 404 de versão
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Chave API não configurada no Render.")

# 3. BARRA LATERAL DA INCLUSÃO (CORES DA NEURODIVERSIDADE)
with st.sidebar:
    st.markdown("### 🌈 ACESSIBILIDADE")
    modo_inclusivo = st.toggle("Ativar Apoio TDAH / TEA")
    if modo_inclusivo:
        st.info("Modo Inclusivo: Linguagem Simples e Visual Estruturado.")
    st.markdown("---")
    st.write("Focado no Currículo RJ 2026")

# 4. ENTRADA DE DADOS
texto_base = st.text_area("📄 Texto da Folha (Cole aqui):", height=250)
duvida = st.text_input("❓ Qual a dúvida do aluno?")

if st.button("ATIVAR MENTOR"):
    if not texto_base:
        st.warning("Por favor, insira o texto.")
    else:
        try:
            # Lógica Pedagógica
            perfil = "Aja como mentor para TDAH/Autismo: frases curtas, sem metáforas, lista de passos." if modo_inclusivo else "Foco em descritores da BNCC e análise crítica."
            
            prompt = f"{perfil} \nTexto: {texto_base} \nDúvida: {duvida}"
            
            with st.spinner("Analisando..."):
                # Forçamos a geração sem metadados de versão beta
                response = model.generate_content(prompt)
                st.markdown("### 👨‍🏫 Orientação:")
                st.success(response.text)
        except Exception as e:
            st.error(f"Erro de conexão. Verifique sua chave API. (Detalhe: {e})")
