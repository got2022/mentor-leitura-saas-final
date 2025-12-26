import sqlite3
import streamlit as st
import nltk

# Configuração da página para ficar com cara de App Profissional
st.set_page_config(page_title="Mentor de Leitura", page_icon="📚")

# Configuração inicial do NLTK
@st.cache_resource
def setup_nltk():
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)

setup_nltk()

# --- CONFIGURAÇÃO DO BANCO DE DADOS (SQLite) ---
def init_db():
    conn = sqlite3.connect('educacao.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS progresso_leitura (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_nome TEXT NOT NULL,
            texto_analisado TEXT NOT NULL,
            perguntas_geradas TEXT NOT NULL,
            data_acesso TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- LÓGICA DO MENTOR DE LEITURA ---
def gerar_perguntas_pedagogicas(texto):
    sentencas = nltk.sent_tokenize(texto, language='portuguese')
    tema_inicial = sentencas[0] if sentencas else "o texto"
    
    perguntas = [
        f"1. [TEMA] Com base na introdução ('{tema_inicial[:50]}...'), qual o assunto principal?",
        "2. [INFERÊNCIA] O que o autor deixa implícito nas entrelinhas deste texto?",
        "3. [NORMA CULTA] Identifique um conectivo ou palavra formal e explique sua função.",
        "4. [PROPOSTA] Como o conteúdo lido se relaciona com um problema social atual?"
    ]
    return perguntas

# --- INTERFACE VISUAL (STREAMLIT) ---
st.title("📚 Mentor de Leitura Inteligente")
st.subheader("Análise pedagógica para alunos de Língua Portuguesa")

with st.form("formulario_leitura"):
    nome_aluno = st.text_input("Nome do Aluno:", placeholder="Digite seu nome completo")
    texto = st.text_area("Cole seu texto ou redação aqui:", height=200)
    botao_enviar = st.form_submit_button("Analisar e Gerar Mentorias")

if botao_enviar:
    if not texto or not nome_aluno:
        st.error("⚠️ Por favor, preencha o nome e o texto antes de continuar.")
    else:
        # 1. Gera as perguntas
        lista_perguntas = gerar_perguntas_pedagogicas(texto)
        string_perguntas = " | ".join(lista_perguntas)

        # 2. Salva no Banco de Dados
        try:
            conn = sqlite3.connect('educacao.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO progresso_leitura (aluno_nome, texto_analisado, perguntas_geradas) VALUES (?, ?, ?)",
                (nome_aluno, texto, string_perguntas)
            )
            conn.commit()
            conn.close()
            
            # 3. Mostra o resultado na tela para o aluno
            st.success(f"Excelente, {nome_aluno}! O Mentor analisou seu texto.")
            st.markdown("### 🧭 Suas Perguntas Orientadoras:")
            for p in lista_perguntas:
                st.info(p)
                
        except Exception as e:
            st.error(f"Erro ao salvar progresso: {e}")

# Rodapé Pedagógico
st.markdown("---")
st.caption("Ferramenta desenvolvida para apoio ao SAEB e competências da BNCC.")


