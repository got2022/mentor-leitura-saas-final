import streamlit as st
from google import genai
import os

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Mentor de Leitura",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Mentor de Leitura")
st.caption("Apoio pedagógico à leitura e interpretação de textos")

# ===============================
# CONEXÃO COM A IA (ESTÁVEL)
# ===============================
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Chave da API não encontrada. Configure GOOGLE_API_KEY.")
    st.stop()

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-1.5-pro"

# ===============================
# INTERFACE
# ===============================
st.subheader("📄 Texto para leitura")
texto = st.text_area(
    "Cole aqui o texto que será analisado",
    height=220
)

st.subheader("❓ Pergunta do aluno (opcional)")
pergunta = st.text_input(
    "Ex: Qual é a ideia principal do texto?"
)

modo_inclusivo = st.checkbox("Ativar linguagem acessível (TEA / TDAH)")

# ===============================
# AÇÃO PRINCIPAL
# ===============================
if st.button("Ativar Mentor"):
    if not texto.strip():
        st.warning("Por favor, insira um texto para análise.")
    else:
        try:
            with st.spinner("O Mentor está analisando o texto..."):
                
                prompt = (
                    "Você é um mentor pedagógico especializado em leitura e interpretação "
                    "de textos para alunos do Ensino Fundamental.\n\n"
                    f"Texto:\n{texto}\n\n"
                )

                if pergunta.strip():
                    prompt += f"Pergunta do aluno:\n{pergunta}\n\n"

                if modo_inclusivo:
                    prompt += (
                        "Responda com linguagem clara, objetiva, organizada em passos curtos, "
                        "adequada para alunos com TDAH ou TEA.\n"
                    )

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

            st.markdown("### 🧩 Orientação do Mentor")
            st.write(response.text)

        except Exception as e:
            st.error(f"Erro ao gerar resposta: {e}")

         
