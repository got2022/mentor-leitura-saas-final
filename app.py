import streamlit as st
import random
import time

# --- Dicionário de Gêneros (Base de Conhecimento do App) ---
GENEROS = {
    "Artigo de Opinião": {
        "icone": "✍️",
        "caracteristicas": ["Tese clara e explícita.", "Uso de Argumentos e contra-argumentos.", "Linguagem subjetiva (1ª pessoa)."],
        "foco_pedagogico": "Capacidade de argumentação e posicionamento crítico.",
        "linguagem": "Subjetiva e persuasiva. Uso de verbos no presente e modalizadores.",
        "literal": ["Qual a principal tese defendida pelo autor?"],
        "inferencial": ["A qual grupo social o autor parece se dirigir ao usar o termo 'nós'?"],
        "critico": ["O posicionamento do autor é atual ou datado? Justifique, considerando o contexto social."],
        "feedback_literal": "Acertou! A tese é a espinha dorsal do gênero.",
        "feedback_inferencial": "Ótima conexão! Você deduziu a intenção comunicativa.",
        "feedback_critico": "Análise da relevância social e contexto do gênero feita com sucesso.",
    },
    "Notícia / Reportagem": {
        "icone": "📰",
        "caracteristicas": ["Informação objetiva e imparcial.", "Estrutura de Lide (o que, quem, quando, onde).", "Linguagem clara e formal (3ª pessoa)."],
        "foco_pedagogico": "Habilidade de síntese, clareza e factualidade da informação.",
        "linguagem": "Objetiva e denotativa. Uso de verbos no passado para relatar fatos.",
        "literal": ["Quem são os envolvidos no fato noticiado e onde ocorreu?"],
        "inferencial": ["Qual é a possível causa não declarada ou subentendida da ocorrência?"],
        "critico": ["O veículo de comunicação demonstrou parcialidade no relato? Justifique com trechos."],
        "feedback_literal": "Localização de fatos dominada.",
        "feedback_inferencial": "Conseguiu ler as entrelinhas da notícia/reportagem.",
        "feedback_critico": "Avaliação ética e de objetividade bem fundamentada.",
    },
    "Resenha Crítica": {
        "icone": "🎬",
        "caracteristicas": ["Resumo descritivo da obra.", "Análise e avaliação (juízo de valor).", "Linguagem mista: objetiva (resumo) e subjetiva (crítica)."],
        "foco_pedagogico": "Capacidade de sintetizar e emitir juízos de valor embasados.",
        "linguagem": "Combina descrição formal (objeto) com avaliação subjetiva (crítico).",
        "literal": ["Qual é o objeto (livro, filme, etc.) da resenha e seu autor/diretor?"],
        "inferencial": ["O crítico assume uma postura de recomendação ou de alerta ao público?"],
        "critico": ["A crítica foi equilibrada, ou o autor dedicou mais espaço à descrição do que à análise?"],
        "feedback_literal": "Identificação de dados da obra correta.",
        "feedback_inferencial": "Análise da intenção comunicativa do crítico dominada.",
        "feedback_critico": "Avaliação da estrutura da crítica bem fundamentada.",
    },
    "Fábula / Conto": {
        "icone": "🦊",
        "caracteristicas": ["Personagens animais com características humanas (personificação).", "Narrativa breve e alegórica.", "Moral explícita ou implícita no final."],
        "foco_pedagogico": "Compreensão da alegoria e da crítica social/moral da narrativa.",
        "linguagem": "Narrativa simples, mas rica em figuras de linguagem.",
        "literal": ["Qual foi a ação principal realizada pelo personagem central da história?"],
        "inferencial": ["Qual vício ou virtude humana o animal representado na fábula simboliza?"],
        "critico": ["A moral da história é relevante para o contexto social atual? Qual adaptação seria necessária?"],
        "feedback_literal": "Identificação de fatos narrativos correta.",
        "feedback_inferencial": "Ótima leitura alegórica e simbólica.",
        "feedback_critico": "Conexão da moral com a realidade social realizada com sucesso.",
    },
    "Lenda": {
        "icone": "🔮",
        "caracteristicas": ["Narrativa de origem popular.", "Mistura fatos reais com elementos fantásticos.", "Busca explicar fenômenos da natureza ou eventos históricos."],
        "foco_pedagogico": "Análise da cultura popular, origem e função social da narrativa.",
        "linguagem": "Uso de adjetivos descritivos e elementos da cultura local.",
        "literal": ["Qual é o fenômeno natural ou cultural que a lenda busca explicar?"],
        "inferencial": ["Qual era o sentimento ou crença predominante da comunidade que criou essa lenda?"],
        "critico": ["Qual o valor cultural e histórico dessa lenda para a identidade regional/nacional?"],
        "feedback_literal": "Identificação do foco da lenda correta.",
        "feedback_inferencial": "Leitura da cosmovisão do povo que criou a lenda.",
        "feedback_critico": "Análise do patrimônio cultural e simbólico da lenda.",
    },
    "Dissertativo-Argumentativo": {
        "icone": "🏛️",
        "caracteristicas": ["Tese no início e desenvolvimento de argumentos com sustentação (repertório).", "Coerência e progressão das ideias.", "Conectivos (operadores argumentativos) coesivos."],
        "foco_pedagogico": "Estrutura formal, coesão, coerência e uso produtivo do repertório (C1-C5 do ENEM).",
        "linguagem": "Formal, objetiva e referencial. Uso de conectivos e verbos no presente.",
        "literal": ["Quais os conectivos (operadores argumentativos) utilizados para ligar os parágrafos?"],
        "inferencial": ["Qual a lacuna de informação que o repertório sociocultural introduzido busca preencher?"],
        "critico": ["Os argumentos apresentados são baseados em fatos concretos, ou são apenas opiniões superficiais?"],
        "feedback_literal": "Identificação e função dos operadores coesivos correta.",
        "feedback_inferencial": "Ótima compreensão da estratégia de uso do repertório.",
        "feedback_critico": "Avaliação da profundidade e solidez dos argumentos.",
    },
}

# --- FUNÇÕES ---

def simular_detecao_genero(texto: str):
    """
    Simula a detecção do gênero com base no tamanho do texto ou na primeira palavra.
    Em um app real, aqui entraria um modelo de IA.
    """
    # Exemplo simples: se o texto for muito curto, simula Fábula. Se for longo, Dissertativo.
    if len(texto) < 300:
        return random.choice(["Fábula / Conto", "Lenda"])
    elif "proposta de intervenção" in texto.lower() or "tese" in texto.lower():
        return "Dissertativo-Argumentativo"
    else:
        return random.choice(list(GENEROS.keys())) # Simula uma detecção aleatória para outros casos

def simular_avaliacao_e_feedback(nivel: str, genero: str, dados_genero):
    """
    Simula a avaliação e gera o feedback na interface.
    """
    
    # Simula se o aluno acertou ou errou
    acertou = random.choice([True, False]) 
    
    pergunta = dados_genero[nivel][0]

    # Estrutura com expansor para melhor organização
    with st.expander(f"✨ **NÍVEL {nivel.upper()}**: {pergunta}", expanded=False):
        
        # Simula um breve tempo de processamento para o aluno refletir antes do feedback
        time.sleep(0.5) 
        
        if acertou:
            feedback = dados_genero[f'feedback_{nivel}']
            st.markdown(f"**Status:** ✅ **Resposta Satisfatória**")
            st.success(f"**Feedback Pedagógico:** {feedback}")
        else:
            ajuda = dados_genero.get(f'ajuda_{nivel}', "Revise as características do gênero.")
            st.markdown(f"**Status:** ❌ **Necessita de Refinamento**")
            st.warning(f"**Dica de Mentoria:** {ajuda}")
            st.info("Recomendação: Concentre-se no foco do gênero para identificar a resposta.")

def renderizar_mentoria(genero_detectado: str):
    """
    Renderiza a miniaula detalhada sobre o gênero.
    """
    dados = GENEROS.get(genero_detectado)
    st.header(f"Mentoria {dados['icone']} - Miniaula sobre o Gênero '{genero_detectado.upper()}'")
    
    col_foco, col_linguagem = st.columns(2)
    
    with col_foco:
        st.subheader("🎯 Foco Pedagógico e Estrutura")
        st.info(dados['foco_pedagogico'])
        
        st.markdown("**Características Chave:**")
        for carac in dados['caracteristicas']:
            st.markdown(f"- {carac}")
            
    with col_linguagem:
        st.subheader("🗣️ Linguagem e Estilo")
        st.warning(dados['linguagem'])

        st.markdown("**Exemplos de Verbos/Termos:**")
        if 'dissertativo' in genero_detectado.lower():
            st.markdown("- Verbos no presente, conectivos coesivos (portanto, ademais, contudo).")
        elif 'notícia' in genero_detectado.lower():
            st.markdown("- Verbos no passado (aconteceu, foi relatado), linguagem em terceira pessoa.")
        elif 'opinião' in genero_detectado.lower():
            st.markdown("- Verbos modalizadores (devemos, é fundamental), pronomes na primeira pessoa (eu, nós).")
            
    st.markdown("---")
    st.success("✅ Gênero Internalizado. Prossiga para o Roteiro de Leitura Guiada abaixo!")

def renderizar_roteiro_leitura(genero_detectado: str):
    """
    Renderiza o roteiro de perguntas para o aluno.
    """
    genero = GENEROS.get(genero_detectado)
    st.header("🧠 Roteiro de Leitura Guiada (Prática de Níveis)")
    
    st.markdown("Responda às perguntas abaixo, simulando o exercício de leitura e análise do texto que você colou:")

    # Simulação para cada nível
    simular_avaliacao_e_feedback('literal', genero_detectado, genero) 
    simular_avaliacao_e_feedback('inferencial', genero_detectado, genero) 
    simular_avaliacao_e_feedback('critico', genero_detectado, genero) 
    
    st.success("🎉 Análise Guiada Concluída! Você aplicou os 3 níveis de leitura com sucesso!")

def renderizar_dashboard_interativo():
    """
    Renderiza a aba principal do dashboard com os inputs e a análise.
    """
    st.markdown("### Ferramenta de Análise e Mentoria de Leitura")

    # Área de inserção de texto
    texto_digitado = st.text_area(
        "1. Cole ou digite o texto/fragmento para Análise:",
        height=300,
        placeholder=f"Cole aqui o seu texto. O Mentor irá detectar o gênero textual automaticamente e iniciar a miniaula."
    )

    # Botão de Análise - O aluno só precisa clicar para o app fazer o resto
    def iniciar_analise():
        if texto_digitado:
            genero_detectado = simular_detecao_genero(texto_digitado)
            st.session_state['analise_data'] = (texto_digitado, genero_detectado)
            st.session_state['analise_iniciada'] = True
        else:
            st.session_state['analise_iniciada'] = False


    st.button(f"Detectar Gênero e Iniciar Mentoria", type="primary", use_container_width=True, on_click=iniciar_analise)
    
    st.markdown("---")

    # Renderiza o resultado da análise se o botão foi pressionado
    if st.session_state.get('analise_iniciada') and texto_digitado:
        texto, genero_detectado = st.session_state['analise_data']
        
        with st.spinner(f'🤖 Mentor analisando: Detectando gênero e preparando a miniaula sobre {genero_detectado}...'):
            time.sleep(2) 
        
        # 1. Renderiza a Mentoria (Miniaula)
        renderizar_mentoria(genero_detectado)
        
        # 2. Renderiza o Roteiro de Leitura
        renderizar_roteiro_leitura(genero_detectado)

# --- ESTRUTURA PRINCIPAL DO APP ---

# Inicialização do estado de sessão
if 'analise_iniciada' not in st.session_state:
    st.session_state['analise_iniciada'] = False

# Configuração da página (Design profissional, wide e ÍCONE MODERNO)
st.set_page_config(
    page_title="Mentor de Gêneros Textuais | Professora", 
    layout="wide", 
    initial_sidebar_state="collapsed", 
    menu_items={'About': 'Aplicativo desenvolvido para prática de leitura em 3 níveis.'},
    page_icon="🤖📝" # Ícone: Robô Mentor e Escrita
)

st.title("📚 Mentor de Gêneros Textuais")

# Remoção da aba 'Manual Pedagógico' (as informações estão na Mentoria) para simplificar a interface.
renderizar_dashboard_interativo()
