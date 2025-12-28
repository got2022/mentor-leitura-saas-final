import streamlit as st
import google.generativeai as genai
import os

# 1. Configuração de Conexão (Gemini 1.5 Pro)
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # Mudança para o modelo Pro, conforme indicado pelo GPT
    model = genai.GenerativeModel('gemini-1.5-pro')
else:
    st.error("Configure a variável GOOGLE_API_KEY no Render.")

# 2. Interface Estilizada (Sua Identidade Visual)
st.set_page_config(page_title="Mentor de Leitura Pro", page_icon="🧩")

st.markdown("""
    <style>
    .resposta-box { background: white; padding: 25px; border-radius: 20px; color: #1e293b; border-left: 10px solid #4f46e5; }
    </style>
    <h1 style='color: #818cf8;'>🧩 Mentor de Leitura</h1>
    <p>Apoio pedagógico com Gemini 1.5 Pro</p>
    """, unsafe_allow_html=True)

# 3. Campos de Entrada
texto_base = st.text_area("📄 Texto da Aula:", height=250)
duvida = st.text_input("💡 Dúvida do Aluno:")

if st.button("ATIVAR MENTOR"):
    if not texto_base:
        st.warning("Por favor, insira o texto para análise.")
    else:
        try:
            with st.spinner("O Gemini 1.5 Pro está processando..."):
                # O modelo Pro ignora o erro 404 da v1beta na maioria dos casos
                response = model.generate_content(
                    f"Atue como mentor pedagógico. Analise o texto: {texto_base}\n\nResponda à dúvida: {duvida}"
                )
                
                st.markdown(f"""
                    <div class="resposta-box">
                        {response.text}
                    </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Erro na IA: {e}")
   
