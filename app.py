import streamlit as st
import random
import time

# --- Dicionário de Gêneros (Base de Conhecimento do App) ---
# Gêneros expandidos e revisados para precisão pedagógica
GENEROS = {
    "Artigo de Opinião": {
        "icone": "✍️",
        "caracteristicas": ["Apresenta uma Tese clara.", "Uso de Argumentos e contra-argumentos.", "Linguagem subjetiva (1ª pessoa)."],
        "literal": ["Qual a principal tese defendida pelo autor?"],
        "inferencial": ["Qual a intenção implícita ao usar determinado termo ou expressão?"],
        "critico": ["O posicionamento do autor é atual ou datado? Justifique, considerando o contexto social."],
        "feedback_literal": "Acertou! Informação explícita identificada.",
        "feedback_inferencial": "Ótima dedução! Sentido implícito capturado.",
        "feedback_critico": "Excelente! Análise da relevância social e contexto do gênero feita com sucesso.",
    },
    "Notícia / Reportagem": {
        "icone": "📰",
        "caracteristicas": ["Informação objetiva e imparcial.", "Estrutura de Lide (o que, quem, quando, onde).", "Linguagem clara e formal."],
        "literal": ["Quem são os envolvidos no fato noticiado e onde ocorreu?"],
        "inferencial": ["Qual é a possível causa não declarada ou subentendida da ocorrência?"],
        "critico": ["O veículo de comunicação demonstrou parcialidade no relato? Justifique com trechos."],
        "feedback_literal": "Localização de fatos dominada.",
        "feedback_inferencial": "Conseguiu ler as entrelinhas da notícia.",
        "feedback_critico": "Avaliação ética do veículo bem fundamentada.",
    },
    "Resenha Crítica": {
        "icone": "🎬",
        "caracteristicas": ["Resumo descritivo da obra.", "Análise e avaliação (juízo de valor).", "Linguagem mista: objetiva (resumo) e subjetiva (crítica)."],
        "literal": ["Qual é o objeto (livro, filme, etc.) da resenha e seu autor/diretor?"],
        "inferencial": ["O crítico assume uma postura de recomendação ou de alerta ao público?"],
        "critico": ["A crítica foi equilibrada, ou o autor dedicou mais espaço à descrição do que à análise?"],
        "feedback_literal": "Identificação de dados da obra correta.",
        "feedback_inferencial": "Análise do público-alvo e intenção dominada.",
        "feedback_critico": "Avaliação da estrutura da crítica bem fundamentada.",
    },
    "Fábula": {
        "icone": "🦊",
        "caracteristicas": ["Personagens animais com características humanas (personificação).", "Narrativa breve e alegórica.", "Finaliza com uma Moral explícita ou implícita."],
        "literal": ["Qual foi a ação principal realizada pelo personagem central da história?"],
        "inferencial": ["Qual vício ou virtude humana o animal representado na fábula simboliza?"],
        "critico": ["A moral da história é relevante para o contexto social atual? Qual adaptação seria necessária?"],
        "feedback_literal": "Acerto! Identificação de fatos narrativos correta.",
        "feedback_inferencial": "Ótima leitura alegórica e simbólica.",
        "feedback_critico": "Conexão da moral com a realidade social realizada com sucesso.",
    },
    "Lenda": {
        "icone": "🔮",
        "caracteristicas": ["Narrativa de origem popular.", "Mistura fatos reais com elementos fantásticos.", "Busca explicar fenômenos da natureza ou eventos históricos."],
        "literal": ["Qual é o fenômeno natural ou cultural que a lenda busca explicar?"],
        "inferencial": ["Qual era o sentimento ou crença predominante da comunidade que criou essa lenda?"],
        "critico": ["Qual o valor cultural e histórico dessa lenda para a identidade regional/nacional?"],
        "feedback_literal": "Identificação do foco da lenda correta.",
        "feedback_inferencial": "Leitura da cosmovisão do povo que criou a lenda.",
        "feedback_critico": "Análise do patrimônio cultural e simbólico da lenda.",
    },
    "Texto Dissertativo-Argumentativo": {
        "icone": "🏛️",
        "caracteristicas": ["Apresentação de Tese clara.", "Desenvolvimento de argumentos com sustentação (repertório).", "Coerência e progressão das ideias."],
        "literal": ["Quais os conectivos (operadores argumentativos) utilizados para ligar os parágrafos?"],
        "inferencial": ["Qual a lacuna de informação que o repertório sociocultural introduzido busca preencher?"],
        "critico": ["Os argumentos apresentados são baseados em fatos concretos, ou são apenas opiniões superficiais?"],
        "feedback_literal": "Identificação e função dos operadores coesivos correta.",
        "feedback_inferencial": "Ótima compreensão da estratégia de uso do repertório.",
        "feedback_critico": "Avaliação da profundidade e solidez dos argumentos.",
    },
}

# --- FUNÇÕES ---

def simular_avaliacao_e_feedback(nivel: str, genero: str, dados_genero):
    """
    Simula a avaliação e gera o feedback na interface, com cores modernas.
    """
    
    # Simula se o aluno acertou ou errou
    acertou = random.choice([True, False]) 
    
    pergunta = dados_genero[nivel][0]

    # Estrutura com expansor para melhor organização
    with st.expander(f"{dados_genero['icone']} **{nivel.upper()}**: {pergunta}"):
        
        if acertou:
            feedback = dados_genero[f'feedback_{nivel}']
            st.markdown(f"**Status:** ✅ **Resposta Satisfatória**")
            st.success(f"**Feedback Pedagógico:** {feedback}")
        else:
            ajuda = dados_genero.get(f'ajuda_{nivel}', "Revise as características do gênero.")
            st.markdown(f"**Status:** ❌ **Necessita de Refinamento**")
            st.error(f"**Dica:** {ajuda}")
            st.warning("Recomendação: Repasse o texto focando nas pistas que definem o gênero.")
    

def renderizar_analise(texto: str, genero_escolhido: str):
    """
    Gera as perguntas e o fluxo de interação na interface Streamlit.
    """
    genero = GENEROS.get(genero_escolhido)

    st.header(f"✨ Análise de Leitura para: {genero_escolhido.upper()} {genero['icone']}")
    
    st.markdown("---")
    
    st.markdown("### 📝 Características Essenciais")
    
    # Exibe as características em colunas para design wide
    cols = st.columns(len(genero["caracteristicas"]))
    for i, carac in enumerate(genero["caracteristicas"]):
        cols[i].metric(label=f"Característica {i+1}", value=carac, delta_color="off")
    
    st.markdown("---")
    st.subheader("🧠 Roteiro de Leitura Guiada (Níveis de Complexidade)")

    # Simulação para cada nível
    simular_avaliacao_e_feedback('literal', genero_escolhido, genero) 
    simular_avaliacao_e_feedback('inferencial', genero_escolhido, genero) 
    simular_avaliacao_e_feedback('critico', genero_escolhido, genero) 
    
    st.balloons()
    st.success("✅ Roteiro Concluído! O aluno pode agora passar para a próxima fase.")


def renderizar_dashboard_interativo():
    """
    Renderiza a aba principal do dashboard com os inputs e a análise.
    """
    st.markdown("### Ferramenta Interativa para Prática de Níveis de Leitura")

    # Área de Seleção e Input
    col_select, col_info = st.columns([2, 1])

    with col_select:
        # Seleção de Gênero
        genero_opcoes = sorted(list(GENEROS.keys()))
        genero_selecionado = st.selectbox(
            "1. Selecione o Gênero Textual para Análise:",
            options=genero_opcoes,
            index=genero_opcoes.index("Dissertativo-Argumentativo") if "Dissertativo-Argumentativo" in genero_opcoes else 0,
            key="selected_genero"
        )
        
        # Área de inserção de texto
        texto_digitado = st.text_area(
            "2. Cole ou digite o texto/fragmento:",
            height=300,
            placeholder=f"Cole aqui o(a) {genero_selecionado} para iniciar a análise guiada."
        )

        # Botão de Análise
        if st.button(f"Analisar Texto - Iniciar Roteiro", type="primary", use_container_width=True):
            if not texto_digitado:
                st.error("Por favor, cole um texto para iniciar a análise.")
            else:
                with st.spinner('Analisando as características e gerando o roteiro...'):
                    time.sleep(1) 
                
                # Armazena o resultado no estado da sessão para renderização
                st.session_state['analise_data'] = (texto_digitado, genero_selecionado)
                st.session_state['analise_iniciada'] = True

    with col_info:
        st.info(f"""
        **Gênero em Foco:** {genero_selecionado}
        
        * **Nível Literal:** O que o texto diz.
        * **Nível Inferencial:** O que o texto implica (entrelinhas).
        * **Nível Crítico:** Opinião sobre o texto (com embasamento).
        """)

    # Renderiza o resultado da análise se o botão foi pressionado
    if st.session_state.get('analise_iniciada'):
        st.markdown("---")
        texto, genero = st.session_state['analise_data']
        renderizar_analise(texto, genero)
        
    st.markdown("---")


def renderizar_manual_pedagogico():
    """
    Renderiza a aba com o manual e a base de conhecimento.
    """
    st.header("📚 Manual do Mentor: Base de Conhecimento Pedagógico")
    st.markdown("Aqui você pode revisar as características e os focos de análise para cada gênero.")
    
    for genero_nome, dados in GENEROS.items():
        st.subheader(f"{dados['icone']} {genero_nome}")
        
        st.markdown("**Características Principais:**")
        st.markdown(f"* {'; '.join(dados['caracteristicas'])}")
        
        st.markdown("**Foco de Análise (Níveis):**")
        st.markdown(f"- **Literal:** {dados['literal'][0]}")
        st.markdown(f"- **Inferencial:** {dados['inferencial'][0]}")
        st.markdown(f"- **Crítico:** {dados['critico'][0]}")
        st.markdown("---")


# --- ESTRUTURA PRINCIPAL DO APP ---

# Inicialização do estado de sessão (necessário para re-renderização organizada)
if 'analise_iniciada' not in st.session_state:
    st.session_state['analise_iniciada'] = False

# Configuração da página (Design profissional e wide)
st.set_page_config(
    page_title="Mentor de Gêneros Textuais | Professora", 
    layout="wide", 
    initial_sidebar_state="collapsed", 
    menu_items={'About': 'Aplicativo desenvolvido para prática de leitura em 3 níveis.'}
)

st.title("📚 Mentor de Gêneros Textuais")

# Criação das abas (Dashboard Interativo)
tab_dashboard, tab_manual = st.tabs(["🚀 Dashboard Interativo", "📖 Manual Pedagógico"])

with tab_dashboard:
    renderizar_dashboard_interativo()

with tab_manual:
    renderizar_manual_pedagogico()
