import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURAÇÃO DE DESIGN (SUPER LEVE PARA CELULAR)
st.set_page_config(page_title="Mentor de Leitura", page_icon="📄", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stTextArea textarea { font-size: 16px !important; } /* Melhora leitura no celular */
    .logo-text { font-size: 1.5rem; font-weight: 800; color: #1e293b; text-align: center; width: 100%; margin-bottom: 20px; }
    </style>
    <div class="logo-text">MENTOR DE LEITURA PRO</div>
    """, unsafe_allow_html=True)

# 2. CONEXÃO IA (MÉTODO BLINDADO)
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # Aqui está o segredo: vamos listar e pegar o modelo disponível de forma dinâmica
    model = genai.GenerativeModel('models/gemini-1.5-flash') 
else:
    st.error("Chave API não configurada no Render.")

# 3. INTERFACE
texto_base = st.text_area("Cole o texto aqui (Toque e segure para colar):", height=250)
duvida_aluno = st.text_input("Qual sua dúvida? (Opcional)")

if st.button("ATIVAR MENTOR"):
    if not texto_base:
        st.warning("Insira um texto primeiro.")
    else:
        try:
            prompt = f"""
            Aja como um mentor pedagógico (Currículo RJ 2026). 
            Explique o gênero do texto e dê 3 dicas curtas para entendê-lo. 
            Use linguagem simples para TDAH/Autistas.
            Texto: {texto_base}
            Dúvida: {duvida_aluno}
            """
            
            with st.spinner("Analisando..."):
                # Removendo qualquer parâmetro de versão que possa causar o 404
                response = model.generate_content(prompt)
                st.markdown("### 👨‍🏫 Sugestão do Mentor")
                st.info(response.text)
        except Exception as e:
            # Se ainda der erro, vamos tentar a versão 'gemini-pro' que é a mais estável de todas
            try:
                model_alt = genai.GenerativeModel('gemini-pro')
                response = model_alt.generate_content(prompt)
                st.success(response.text)
            except:
                st.error(f"Erro técnico: {e}. Professora, verifique se a chave no Render não tem espaços em branco.")


 
            
        
