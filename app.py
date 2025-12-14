import streamlit as st
import random

# --- DADOS DOS GÊNEROS TEXTUAIS (Base Pedagógica) ---
GENEROS_TEXTUAIS = {
    "Artigo de Opinião": {
        "caracteristicas": [
            "Apresenta uma Tese clara e inconfundível.",
            "Uso de Argumentos e contra-argumentos para embasamento.",
            "Linguagem subjetiva, frequentemente em 1ª ou 3ª pessoa.",
            "Publicado em veículos de grande alcance (jornais, revistas)."
        ],
        "perguntas": [
            {"nivel": "LITERAL", "pergunta": "Qual a principal tese defendida pelo autor no primeiro parágrafo?"},
            {"nivel": "INFERENCIAL", "pergunta": "Qual é a intenção do autor ao citar o dado estatístico 'X' no desenvolvimento?"},
            {"nivel": "CRÍTICO", "pergunta": "O posicionamento do autor é válido para a realidade do seu bairro/cidade? Justifique, baseando-se em fatos atuais."}
        ]
    },
    "Notícia": {
        "caracteristicas": [
            "Linguagem clara, objetiva e impessoal (3ª pessoa).",
            "Estrutura de Pirâmide Invertida: Lide (O quê, Quem, Quando, Onde, Como e Por quê).",
            "Relato de fatos recentes e de interesse público.",
            "Ausência de juízo de valor ou opinião do jornalista."
        ],
        "perguntas": [
            {"nivel": "LITERAL", "pergunta": "Identifique no Lide (primeiro parágrafo) quem são os envolvidos no fato relatado."},
            {"nivel": "INFERENCIAL", "pergunta": "O título da notícia é apelativo ou informativo? Por quê?"},
            {"nivel": "CRÍTICO", "pergunta": "Este fato noticiado é relevante para a comunidade escolar? Que impacto ele pode gerar?"}
        ]
    },
    "Crônica": {
        "caracteristicas": [
            "Linguagem leve e descontraída, próxima à oralidade.",
            "Aborda temas do cotidiano, trivialidades e observações do dia a dia.",
            "Caráter poético, humorístico ou reflexivo.",
            "Publicada em periódicos (jornais, revistas), geralmente em coluna fixa."
        ],
        "perguntas": [
            {"nivel": "LITERAL", "pergunta": "Qual evento trivial do dia a dia o cronista usou como ponto de partida para sua reflexão?"},
            {"nivel": "INFERENCIAL", "pergunta": "Qual é a crítica social implícita na observação feita pelo cronista sobre 'a fila do pão'?"},
            {"nivel": "CRÍTICO", "pergunta": "A crônica utiliza figuras de linguagem (metáfora, ironia)? Se sim, qual o efeito de sentido?"}
        ]
    },
    "Resenha Crítica": {
        "caracteristicas": [
            "Texto descritivo e opinativo sobre uma obra (filme, livro, arte).",
            "Apresenta dados da obra (título, autor, ano) e um resumo.",
            "Contém a avaliação (julgamento de valor) do Resenhista.",
            "Objetivo: guiar ou influenciar o leitor sobre a qualidade da obra."
        ],
        "perguntas": [
            {"nivel": "LITERAL", "pergunta": "Qual é a tese principal (opinião) do resenhista sobre o filme/livro?"},
            {"nivel": "INFERENCIAL", "pergunta": "O tom da resenha é irônico ou sério? Como isso afeta a credibilidade da opinião?"},
            {"nivel": "CRÍTICO", "pergunta": "Se você fosse um produtor, aceitaria o veredito do resenhista? Justifique seu posicionamento."}
        ]
    }
}


# --- FUNÇÕES DE LÓGICA DO APP ---

# A lógica de geração de roteiro permanece a mesma para manter a estrutura, mas o feedback será melhorado
def gerar_roteiro(texto, genero):
    if genero not in GENEROS_TEXTUAIS:
        return None, None

    data = GENEROS_TEXTUAIS[genero]
    
    perguntas_roteiro = []
    niveis = ["LITERAL", "INFERENCIAL", "CRÍTICO"]
    for nivel in niveis:
        perguntas_do_nivel = [p for p in data["perguntas"] if p["nivel"] == nivel]
        if perguntas_do_nivel:
            perguntas_roteiro.append(random.choice(perguntas_do_nivel))
        
    return data["caracteristicas"], perguntas_roteiro

def simular_correcao(perguntas_roteiro):
    """
    Melhora a simulação de feedback para torná-la menos 'bugada' e mais pedagógica,
    incluindo feedbacks específicos para as 5 Competências do ENEM.
    """
    correcao = "## 📝 ROTEIRO DE CORREÇÃO (Simulação Pedagógica)\n\n"
    
    # Lista de feedbacks baseada no Manual do Corretor ENEM
    for i, item in enumerate(perguntas_roteiro):
        nivel = item["nivel"]
        pergunta = item["pergunta"]
        
        # --- Feedback Específico para o ENEM (5 Competências) ---
        if nivel.startswith("C"):
            if "C1" in nivel:
                feedbacks_acerto = ["✅ Nível 5 (200 pontos)! Domínio excelente da norma culta. Mantenha a atenção à pontuação complexa.", "✅ C1 OK! Apenas desvios pontuais. Quase no nível máximo."]
                feedbacks_erro = ["❌ C1: Atenção! Desvios recorrentes de concordância verbal/nominal ou regência. Revise as regras básicas.", "❌ C1: Erros graves de ortografia ou acentuação. Isso limita sua nota. Consulte o vocabulário ortográfico."]
            
            elif "C2" in nivel:
                feedbacks_acerto = ["✅ Nível 5 (200 pontos)! Abordagem completa do tema e uso estratégico de Repertório Sociocultural produtivo.", "✅ Tema e Repertório OK! Demonstra capacidade de leitura de mundo e conexão de áreas do conhecimento."]
                feedbacks_erro = ["❌ C2: Tangenciamento ou fuga parcial ao tema. Refaça a análise das palavras-chave da proposta.", "❌ C2: O Repertório (citação, dado) foi usado, mas está DESCONECTADO da argumentação. Precisa de produtividade."]
                
            elif "C3" in nivel:
                feedbacks_acerto = ["✅ Nível 5 (200 pontos)! Projeto de texto estratégico e eficiente. As informações se articulam em defesa de um ponto de vista.", "✅ C3 OK! Argumentos desenvolvidos com clareza e progressão textual satisfatória."]
                feedbacks_erro = ["❌ C3: Falha na Progressão Argumentativa. O D2 (segundo argumento) repete o D1. Precisa de ideias novas e articuladas.", "❌ C3: O projeto de texto é confuso. A tese inicial não foi retomada/defendida nos desenvolvimentos."]
                
            elif "C4" in nivel:
                feedbacks_acerto = ["✅ Nível 5 (200 pontos)! Domínio dos mecanismos linguísticos necessários para a construção da argumentação, com repertório coesivo diversificado.", "✅ C4 OK! Uso eficiente de conectivos inter e intraparágrafos."]
                feedbacks_erro = ["❌ C4: Repetição excessiva dos mesmos conectivos (Ex: 'Além disso'). Diversifique seu vocabulário coesivo.", "❌ C4: Uso inadequado de conectivos (Ex: usar 'Portanto' no meio do parágrafo). Revise a função semântica."]
                
            elif "C5" in nivel:
                feedbacks_acerto = ["✅ Nível 5 (200 pontos)! Proposta de Intervenção completa (5 elementos) e com excelente detalhamento.", "✅ C5 OK! A intervenção é válida e apresenta Agente, Ação, Modo/Meio e Efeito."]
                feedbacks_erro = ["❌ C5: A Proposta está incompleta. Verifique se o Agente ou o Detalhamento foram omitidos.", "❌ C5: A intervenção é vaga. Precisa de uma Ação concreta e um Modo/Meio que seja executável."]

        # --- Feedback Genérico para Outros Gêneros (LITERAL/INFERENCIAL/CRÍTICO) ---
        else:
             if nivel == "LITERAL":
                feedbacks_acerto = ["✅ Acerto! Localização de fatos dominada. Você identificou a informação de forma direta no texto.", "✅ Excelente! O primeiro passo da leitura está garantido: você sabe o que o texto diz."]
                feedbacks_erro = ["❌ Atenção! Concentre-se no texto, sem inferências. Qual é o dado EXPLICITADO? **Dica:** Procure por nomes próprios ou datas.", "❌ Revise o nível literal. O erro aqui compromete as próximas etapas de leitura."]
            
             elif nivel == "INFERENCIAL":
                feedbacks_acerto = ["✅ Acerto! Interpretação profunda. Você conseguiu ler as entrelinhas e entender a implicação do autor.", "✅ Muito bom! Sua resposta demonstra a capacidade de conectar ideias e inferir a intenção comunicativa."]
                feedbacks_erro = ["❌ Atenção! Sua resposta precisa de refinamento. **Dica:** Tente conectar o que foi dito com o contexto social ou a intenção do autor (para que ele escreveu?).", "❌ Faltou um pouco de profundidade. A inferência exige que você conecte duas ideias diferentes do texto."]
                
             elif nivel == "CRÍTICO":
                feedbacks_acerto = ["✅ Acerto! Avaliação ética e social do fato noticiado foi bem fundamentada. Seu posicionamento é maduro.", "✅ Excelente argumento! Seu posicionamento está embasado e considera o contexto social e a função do gênero."]
                feedbacks_erro = ["❌ Reflita: Sua crítica está baseada apenas na sua opinião? **Dica:** A crítica deve usar o texto como base e relacioná-lo com o mundo real ou outras referências (Repertório Sociocultural).", "❌ O posicionamento é válido, mas falta JUSTIFICATIVA. Por que o posicionamento do autor é atual ou datado?"]


        # Aplica o feedback (50/50 chance de acerto/erro para simulação)
        if random.random() > 0.5:
            feedback = random.choice(feedbacks_acerto)
        else:
            feedback = random.choice(feedbacks_erro)

        
        correcao += f"### {i+1}. {nivel}\n"
        correcao += f"**Pergunta para o Aluno:** *{pergunta}*\n"
        correcao += f"**💬 Feedback do Mentor:** {feedback}\n\n"
        
    return correcao
   

   

# --- CONFIGURAÇÃO INICIAL E ESTÉTICA (Novo Dashboard) ---
st.set_page_config(
    page_title="Mentor de Gêneros Textuais",
    page_icon="📚",
    layout="wide",
)

# Estilos CSS customizados para o dashboard moderno
st.markdown("""
<style>
/* Fundo mais claro e profissional */
.main {
    background-color: #f8f9fa; /* Cinza bem claro */
}
/* Estilo do título principal */
.big-font {
    font-size:36px !important;
    font-weight: 700;
    color: #007bff; /* Azul primário */
    text-shadow: 1px 1px 2px #adb5bd;
}
/* Estilo dos containers de resultado (cards) */
.result-card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    border-left: 5px solid #007bff; /* Linha azul destacada */
}
/* Estilo para botões */
div.stButton > button:first-child {
    background-color: #28a745; /* Verde de sucesso */
    color: white;
    font-weight: bold;
    border: none;
    padding: 10px 30px;
    border-radius: 8px;
    transition: background-color 0.3s ease;
}
div.stButton > button:first-child:hover {
    background-color: #1e7e34;
}
/* Ajuste de espaçamento para o texto */
.stTextArea label {
    font-weight: bold;
    color: #343a40;
}
</style>
""", unsafe_allow_html=True)


# --- ESTRUTURA PRINCIPAL DO STREAMLIT (Dashboard) ---

st.markdown('<p class="big-font">📚 Mentor de Gêneros Textuais</p>', unsafe_allow_html=True)
st.markdown('### Ferramenta de apoio para professores de Língua Portuguesa e Redação.')

# Botão para limpar o cache (Solução para o problema do menu incompleto)
if st.sidebar.button("Limpar Cache e Recarregar App"):
    st.cache_data.clear() # Limpa o cache de dados do streamlit
    st.experimental_rerun() # Força o recarregamento completo

st.sidebar.title("Configurações Pedagógicas")
genero_selecionado = st.sidebar.selectbox(
    "1. Selecione o Gênero Textual:",
    list(GENEROS_TEXTUAIS.keys()), # Agora deve mostrar todos os gêneros
    index=0
)
st.sidebar.info(f"Gênero escolhido: **{genero_selecionado}**")

# --- COLUNA PRINCIPAL (INPUT e Processamento) ---

st.header("Passo 2: Cole o Texto para Análise")

# Coloca o text_area dentro de um container para dar estilo
with st.container():
    st.text_area(
        "Cole o texto completo aqui:",
        key="texto_aluno", # Usa chave para gerenciamento de estado
        height=300,
        placeholder="Ex: Cole aqui um Artigo de Opinião, uma Notícia, Crônica, etc."
    )

if st.button("GERAR ROTEIRO E CORREÇÃO SIMULADA"):
    texto_aluno = st.session_state["texto_aluno"]
    
    if len(texto_aluno) < 50:
        st.error("⚠️ Por favor, cole um texto completo (com pelo menos 50 caracteres) para iniciar a análise.")
    else:
        # --- EXECUÇÃO E RESULTADOS ---
        st.success(f"Análise do Gênero **{genero_selecionado}** em andamento...")
        
        caracteristicas, perguntas_roteiro = gerar_roteiro(texto_aluno, genero_selecionado)
        
        if not perguntas_roteiro:
            st.error("Erro: Não foi possível gerar o roteiro para este gênero.")
        else:
            
            # Novo layout com colunas para o Dashboard
            st.markdown("---")
            st.markdown("## 📊 Dashboard de Análise de Gêneros")

            col1, col2 = st.columns([1, 2]) # Colunas para melhor visualização

            with col1:
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.subheader("Características do Gênero")
                st.info(f"O Mentor considera estas características-chave do **{genero_selecionado}**:")
                for char in caracteristicas:
                    st.markdown(f"- **{char}**")
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.subheader("Roteiro de Leitura Gerado")
                st.warning("Este roteiro de perguntas guia a interpretação do texto:")
                for i, item in enumerate(perguntas_roteiro):
                    st.markdown(f"**{i+1}. Nível {item['nivel']}:** {item['pergunta']}")
                st.markdown('</div>', unsafe_allow_html=True)

            # Simulação de correção (Feedback Melhorado)
            st.markdown("---")
            st.markdown("## 📝 Simulação de Correção Pedagógica")
            
            # Coloca o resultado em um container estilizado
            with st.container():
                st.markdown('<div class="result-card" style="border-left: 5px solid #28a745;">', unsafe_allow_html=True) # Borda verde
                correcao_final = simular_correcao(perguntas_roteiro)
                st.markdown(correcao_final, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            st.balloons()
