import streamlit as st
import random 

# ----------------------------------------------------------------------------------
# 1. Base de Conhecimento e Funções (O CÉREBRO)
# ----------------------------------------------------------------------------------

# Dicionário de Gêneros e Características (Base de Conhecimento do App)
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

def simular_avaliacao_e_feedback(nivel: str, genero: str, resposta_aluno_esta_correta: bool):
    """ Simula a avaliação de uma resposta e gera o feedback construtivo. (Adaptada para Streamlit) """
    dados_genero = GENEROS.get(genero)

    if dados_genero:
        st.subheader(f"--- FEEDBACK NÍVEL {nivel.upper()} ---")

        if resposta_aluno_esta_correta:
            st.success(f"✅ Acerto! {dados_genero[f'feedback_{nivel}']}")
        else:
            st.error(f"❌ Atenção! Sua resposta precisa de refinamento.")
            st.info(f"💡 Dica: {dados_genero[f'ajuda_{nivel}']}")

def analisar_texto_e_gerar_roteiro(texto: str, genero_escolhido: str):
    """ Gera as perguntas e o fluxo de interação, agora com feedback. (Adaptada para Streamlit) """
    st.header("--- MENTOR DE GÊNEROS: ROTEIRO GERADO ---")
    genero = GENEROS.get(genero_escolhido)

    if not genero:
        st.warning(f"O gênero '{genero_escolhido}' não está cadastrado na base de dados.")
        return

    st.markdown(f"#### Gênero Detectado: **{genero_escolhido.upper()}**")
    st.write("Características Essenciais para Leitura:")
    for carac in genero["caracteristicas"]:
        st.markdown(f"- **{carac}**")

    st.markdown("---")
    st.subheader("ROTEIRO DE LEITURA GUIADA")

    # Simulando o fluxo de interação com perguntas (em um app real, o aluno responderia)
    st.markdown("##### 1. NÍVEL LITERAL (O QUE O TEXTO DIZ)")
    st.markdown(f"**Pergunta:** {genero['literal'][0]}")
    simular_avaliacao_e_feedback('literal', genero_escolhido, True) # Simula acerto

    st.markdown("##### 2. NÍVEL INFERENCIAL (O QUE O TEXTO IMPLICA)")
    st.markdown(f"**Pergunta:** {genero['inferencial'][0]}")
    simular_avaliacao_e_feedback('inferencial', genero_escolhido, False) # Simula erro

    st.markdown("##### 3. NÍVEL CRÍTICO (POSICIONAMENTO E CONTEXTO)")
    st.markdown(f"**Pergunta:** {genero['critico'][0]}")
    simular_avaliacao_e_feedback('critico', genero_escolhido, True) # Simula acerto

# ----------------------------------------------------------------------------------
# 2. INTERFACE STREAMLIT (O FRONT-END)
# ----------------------------------------------------------------------------------

st.set_page_config(page_title="Mentor de Gêneros Textuais", layout="wide")

st.title("📚 Mentor de Gêneros Textuais")
st.markdown("##### Ferramenta de apoio para professores de Língua Portuguesa e Redação.")

# Seleção do Gênero
generos_disponiveis = list(GENEROS.keys())
genero_selecionado = st.selectbox(
    "1. Selecione o Gênero Textual para a análise:",
    options=generos_disponiveis
)

# Área de Texto para Colar o Conteúdo
texto_colado = st.text_area(
    "2. Cole o Texto a ser analisado aqui:",
    height=300,
    placeholder="Cole seu Artigo de Opinião, Notícia ou outro Gênero aqui..."
)

# Botão de Ação
if st.button("🚀 GERAR ROTEIRO DE LEITURA"):
    if texto_colado and genero_selecionado:
        analisar_texto_e_gerar_roteiro(texto_colado, genero_selecionado)
    else:
        st.warning("Por favor, cole um texto e selecione um gênero para começar.")
