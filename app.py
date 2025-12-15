import streamlit as st
import random
import time

# --- DADOS ---

# Lista de perguntas e competências para o ENEM
perguntas_competencias = [
    {"nivel": "C1 (Demonstrar domínio da norma culta)", "pergunta": "O texto apresenta desvios gramaticais (concordância, regência, colocação pronominal) ou de convenção (acentuação, pontuação, ortografia) que comprometem a compreensão?"},
    {"nivel": "C2 (Compreender a Proposta)", "pergunta": "O texto aborda o tema proposto de forma completa? Apresenta tangenciamento ou fuga parcial/total?"},
    {"nivel": "C3 (Seleção e Organização)", "pergunta": "O texto apresenta argumentos consistentes e bem articulados em torno de um ponto de vista claro?"},
    {"nivel": "C4 (Coesão e Coerência)", "pergunta": "O texto utiliza recursos coesivos interparágrafos (conectivos) e intraparágrafos de maneira diversificada e adequada?"},
    {"nivel": "C5 (Proposta de Intervenção)", "pergunta": "A proposta de intervenção é completa (Ação, Agente, Meio/Modo, Efeito e Detalhamento)? É original e ética?"}
]

# Textos de apoio e feedback
feedbacks = {
    "C1": "Foco na gramática! A precisão da norma culta é o alicerce para a clareza do seu texto.",
    "C2": "Revise o tema! Garanta que todos os aspectos da proposta sejam plenamente desenvolvidos.",
    "C3": "Melhore a argumentação! Desenvolva seus pontos de vista com mais profundidade e evidências.",
    "C4": "Conecte as ideias! O uso eficaz de conectivos (coesão) e a lógica (coerência) são vitais para a fluidez.",
    "C5": "Enriqueça a proposta! Lembre-se de detalhar Ação, Agente, Meio, Efeito e Detalhamento."
}

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Mentor de Gêneros Textuais", layout="wide", initial_sidebar_state="expanded")
st.title("📚 Mentor de Gêneros Textuais")
st.markdown("### Avaliação de Competências (Modelo ENEM)")
st.sidebar.header("Configurações da Análise")

# --- FUNÇÕES ---

def gerar_analise(texto, competencias_selecionadas):
    """Gera uma análise simulada com base nas competências e no texto."""
    st.session_state.analise_concluida = True
    st.subheader("📝 Resultado da Análise de Competências")
    st.markdown("---")

    resultados = []
    
    # Simula o processamento
    with st.spinner('Analisando o texto com base no Manual do Corretor ENEM...'):
        time.sleep(2) # Pausa para simular processamento
        
    for comp in competencias_selecionadas:
        nivel = comp["nivel"]
        
        # Simula uma nota aleatória entre 60 e 200 (em incrementos de 40)
        nota_simulada = random.choice([60, 100, 140, 180, 200])
        feedback = feedbacks.get(nivel.split('(')[0].strip()[1:], "Feedback genérico.") # Busca o feedback pelo C1, C2, etc.
        
        resultados.append({
            "Competência": nivel,
            "Pergunta-Chave": comp["pergunta"],
            "Nota (Simulada)": nota_simulada,
            "Feedback": feedback
        })
    
    # Exibe os resultados
    for resultado in resultados:
        st.info(f"**{resultado['Competência']}**")
        st.markdown(f"**Pergunta-Chave (Critério):** {resultado['Pergunta-Chave']}")
        
        col1, col2 = st.columns([1, 4])
        col1.metric(label="Nota Simulada", value=f"{resultado['Nota (Simulada)']}/200")
        col2.warning(f"**Foco de Correção:** {resultado['Feedback']}")
        st.markdown("---")

    # Sumário da Nota Final Simulada
    st.success("✅ Análise concluída! Role para baixo para ver a Pontuação Global.")
    
    notas = [r['Nota (Simulada)'] for r in resultados]
    if notas:
        media = sum(notas) / len(notas)
        nota_final = int(round(media / 20) * 20) # Arredonda para o múltiplo de 20 mais próximo
        
        st.subheader("🎯 Pontuação Global (Simulada)")
        col_final_1, col_final_2 = st.columns(2)
        col_final_1.metric("Média das Notas Simuladas", f"{int(media)}")
        col_final_2.metric("Pontuação Final Estimada", f"**{nota_final}**", delta=f"{nota_final - 120} pontos")
        
        st.balloons()


# --- INTERFACE DO USUÁRIO ---

# Inicialização do estado
if 'analise_concluida' not in st.session_state:
    st.session_state.analise_concluida = False
    
# Seleção de Competências na Sidebar
st.sidebar.subheader("Competências para Análise")
comp_opcoes = [c["nivel"] for c in perguntas_competencias]
comp_selecionadas_nomes = st.sidebar.multiselect(
    "Selecione as Competências (ENEM):",
    options=comp_opcoes,
    default=comp_opcoes # Seleciona todas por padrão
)

# Filtra as competências baseadas na seleção do usuário
competencias_para_analise = [c for c in perguntas_competencias if c["nivel"] in comp_selecionadas_nomes]

# Área de inserção de texto
texto_digitado = st.text_area(
    "Cole ou digite o texto/redação para análise:",
    height=400,
    placeholder="Ex: A persistência da violência contra a mulher na sociedade brasileira..."
)

# Botão de Análise
if st.button("Analisar Redação (Simulação ENEM)"):
    if not texto_digitado:
        st.error("Por favor, cole um texto na área acima antes de analisar.")
    elif not competencias_para_analise:
        st.error("Selecione pelo menos uma competência para iniciar a análise.")
    else:
        gerar_analise(texto_digitado, competencias_para_analise)

# Mensagem inicial ou de nova análise
if not st.session_state.analise_concluida:
    st.info("Utilize este mentor para simular a correção de uma redação, focando nas 5 competências do ENEM.")

# ==========================================================
# FIM DO CÓDIGO - ARQUIVO LIMPO
# ==========================================================
  
   
 
     



           
       
   
    






