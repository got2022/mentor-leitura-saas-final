import streamlit as st
import random
import time

# --- Dicionário de Gêneros e Características (Base de Conhecimento do App) ---
GENEROS = {
    "Artigo de Opinião": {
        "caracteristicas": ["Apresenta uma Tese clara.", "Uso de Argumentos e contra-argumentos.", "Linguagem subjetiva (1ª pessoa)."],
        "literal": ["Qual a principal tese defendida pelo autor?"],
        "inferencial": ["A qual grupo social o autor parece se dirigir ao usar o termo 'nós'?"],
        "critico": ["O posicionamento do autor é atual ou datado? Justifique, considerando o contexto social do RJ."],
        "feedback_literal": "Acertou! Você identificou a informação no texto, que é o primeiro passo para a leitura.",
        "feedback_inferencial": "Ótima conexão! Você conseguiu deduzir o sentido implícito. Prossiga para o senso crítico.",
        "feedback_critico": "Excelente argumento! Seu posicionamento está embasado e considera o contexto do gênero. Continue a construir seu repertório.",
        "ajuda_literal": "Revise o primeiro parágrafo. A resposta é explícita.",
        "ajuda_inferencial": "Leia as entrelinhas. Qual a intenção do autor ao usar essa palavra? Tente conectar duas ideias diferentes.",
        "ajuda_critico": "Lembre-se das características do Artigo de Opinião: sua resposta deve ter uma TESE. Qual é a sua tese sobre o assunto?"
    },
    "Notícia": {
        "caracteristicas": ["Informação objetiva (3ª pessoa).", "Estrutura de Lide (o que, quem, quando, onde).", "Linguagem clara e formal."],
        "literal": ["Quem são os envolvidos no fato noticiado?"],
        "inferencial": ["Qual a possível causa não declarada para a omissão de um nome na notícia?"],
        "critico": ["O veículo de comunicação demonstrou parcialidade? Justifique."],
        "feedback_literal": "Acerto! Localização de fatos dominada.",
        "feedback_inferencial": "Conseguiu ler as entrelinhas da notícia.",
        "feedback_critico": "Avaliação ética e social do fato noticiado foi bem fundamentada.",
        "ajuda_literal": "Busque o Lide: Onde, quem, o quê.",
        "ajuda_inferencial": "O que a notícia implica, mas não diz abertamente?",
        "ajuda_critico": "Pense no viés. O texto é neutro ou favorece uma parte?"
    }
}

# --- FUNÇÕES PARA GERAÇÃO DA ANÁLISE ---

def simular_avaliacao_e_feedback(nivel: str, genero: str, resposta_aluno_esta_correta: bool):
    """
    Simula a avaliação de uma resposta e gera o feedback construtivo na interface.
    """
    dados_genero = GENEROS.get(genero)
    
    # Simula se o aluno acertou ou errou (para fins de demonstração)
    acertou = random.choice([True, False]) 
    
    # Exibe a pergunta
    st.markdown(f"**NÍVEL {nivel.upper()}:** {dados_genero[nivel][0]}")

    if acertou:
        st.success(f"✅ Feedback: {dados_genero[f'feedback_{nivel}']}")
    else:
        st.error(f"❌ Atenção! Sua resposta precisa de refinamento.")
        st.info(f"💡 Dica: {dados_genero[f'ajuda_{nivel}']}")
    st.markdown("---")


def analisar_texto_e_gerar_roteiro(texto: str, genero_escolhido: str):
    """
    Gera as perguntas e o fluxo de interação na interface Streamlit.
    """
    genero = GENEROS.get(genero_escolhido)

    st.subheader(f"✨ Gênero Selecionado: {genero_escolhido.upper()}")
    
    st.markdown("### Características Essenciais para Leitura")
    for carac in genero["caracteristicas"]:
        st.markdown(f"- {carac}")

    st.markdown("---")
    st.header("📚 Roteiro de Leitura Guiada")

    # Aplica a simulação para cada nível
    simular_avaliacao_e_feedback('literal', genero_escolhido, True) 
    simular_avaliacao_e_feedback('inferencial', genero_escolhido, False) 
    simular_avaliacao_e_feedback('critico', genero_escolhido, True) 
    
    st.balloons()
    st.success("Análise de Gênero Concluída!")
    
# --- CONFIGURAÇÃO DA INTERFACE STREAMLIT ---

st.set_page_config(page_title="Mentor de Gêneros Textuais", layout="wide")

st.title("📚 Mentor de Gêneros Textuais")
st.markdown("### Análise de Níveis de Leitura (Literal, Inferencial, Crítico)")

# Seleção de Gênero
genero_opcoes = list(GENEROS.keys())
genero_selecionado = st.sidebar.selectbox(
    "1. Selecione o Gênero Textual",
    options=genero_opcoes,
    index=0 
)

# Área de inserção de texto
texto_digitado = st.text_area(
    "2. Cole ou digite o texto/fragmento para análise:",
    height=300,
    placeholder="Cole aqui o Artigo de Opinião, a Notícia, etc., para iniciar a análise guiada."
)

# Botão de Análise
if st.button(f"Analisar Texto ({genero_selecionado})"):
    if not texto_digitado:
        st.error("Por favor, cole um texto para iniciar a análise.")
    else:
        # Simula o processamento
        with st.spinner('Analisando as características e gerando o roteiro...'):
            time.sleep(1) 
        
        analisar_texto_e_gerar_roteiro(texto_digitado, genero_selecionado)
        
st.sidebar.markdown("---")
st.sidebar.info("Este aplicativo gera um roteiro de perguntas para que o aluno pratique a leitura em 3 níveis de complexidade, conforme o gênero textual selecionado.")
