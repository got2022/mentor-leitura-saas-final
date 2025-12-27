import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURAÇÃO E IDENTIDADE VISUAL
st.set_page_config(page_title="Mentor de Leitura Pro", page_icon="📖", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background-color: #ffffff; }
    .titulo-principal {
        font-size: 2.5rem; font-weight: 800;
        background: linear-gradient(135deg, #1e40af 0%, #7e22ce 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-align: center;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #2563eb 0%, #9333ea 100%);
        color: white; border-radius: 50px; border: none;
        padding: 0.8rem 2rem; font-weight: 700; width: 100%;
        box-shadow: 0 4px 15px rgba(147, 51, 234, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM A IA
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# 3. INTERFACE DO MENTOR
st.markdown('<h1 class="titulo-principal">Mentor de Leitura</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b;'>Seu apoio pedagógico para interpretação e compreensão de textos</p>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Contexto Pedagógico")
    nivel = st.selectbox("Nível do Aluno:", ["Ensino Fundamental II", "Ensino Médio"])
    genero = st.text_input("Gênero Textual (ex: Crônica, Artigo):")

col1, col2 = st.columns(2)
with col1:
    texto_base = st.text_area("Texto base para leitura:", height=300)
with col2:
    duvida_aluno = st.text_area("Qual sua dúvida ou dificuldade?", height=300, placeholder="Ex: Não entendi a ironia no segundo parágrafo...")

if st.button("Pedir Orientação ao Mentor"):
    if texto_base and duvida_aluno and api_key:
        with st.spinner("O Mentor está analisando os níveis de leitura..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                
                # O PROMPT AGORA É UM MENTOR PEDAGÓGICO
                prompt = f"""
                Atue como um Mentor de Leitura e professor de Língua Portuguesa para o {nivel}.
                Seu objetivo não é dar a resposta pronta, mas auxiliar o aluno a compreender o gênero {genero}.
                Baseie sua resposta nos níveis de leitura:
                1. Compreensão Literal (o que está escrito).
                2. Compreensão Inferencial (o que está nas entrelinhas).
                3. Compreensão Crítica (o posicionamento do texto).
                
                Texto base: {texto_base}
                Dúvida do aluno: {duvida_aluno}
                
                Responda de forma dialógica, incentivando o aluno a pensar, usando uma linguagem acolhedora e pedagógica.
                """
                
                response = model.generate_content(prompt)
                st.markdown("---")
                st.markdown("### 👨‍🏫 Orientação do Mentor")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro: {e}")
    else:
        st.warning("Por favor, preencha o texto base e a sua dúvida.")
