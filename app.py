# =================================================================
# FERRAMENTA: MENTOR DE LEITURA INTEGRADO (FLASK + SQLITE)
# OBJETIVO: Analisar texto, gerar perguntas e salvar progresso.
# =================================================================

import sqlite3
from flask import Flask, request, jsonify
import nltk

# Configuração inicial do NLTK (executado no deploy/inicialização)
nltk.download('punkt', quiet=True)

app = Flask(__name__)

# --- CONFIGURAÇÃO DO BANCO DE DADOS (SQLite) ---

def init_db():
    """Cria a tabela de progresso se ela não existir."""
    # Conecta ao arquivo de banco de dados (será criado na raiz do projeto)
    conn = sqlite3.connect('educacao.db')
    cursor = conn.cursor()
    # Tabela estruturada para atenção individualizada (BNCC/SAEB)
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

# Inicializa o banco ao rodar o app
init_db()

# --- LÓGICA DO MENTOR DE LEITURA ---

def gerar_perguntas_pedagogicas(texto):
    """Gera perguntas baseadas nos descritores de leitura SAEB."""
    sentencas = nltk.sent_tokenize(texto, language='portuguese')
    tema_inicial = sentencas[0] if sentencas else "o texto"
    
    # Lista de perguntas com foco em competências específicas
    perguntas = [
        f"1. [TEMA] Com base na introdução ('{tema_inicial[:50]}...'), qual o assunto principal?",
        "2. [INFERÊNCIA] O que o autor deixa implícito nas entrelinhas deste texto?",
        "3. [NORMA CULTA] Identifique um conectivo ou palavra formal e explique sua função.",
        "4. [PROPOSTA] Como o conteúdo lido se relaciona com um problema social atual?"
    ]
    return " | ".join(perguntas) # Salva como string única separada por pipe para o banco

# --- ROTAS DA API ---

@app.route('/analisar_leitura', methods=['POST'])
def analisar_leitura():
    """
    Endpoint que recebe o texto e o nome do aluno, 
    gera as perguntas e salva no banco de dados.
    """
    data = request.json
    nome_aluno = data.get('aluno_nome', 'Anônimo')
    texto = data.get('texto', '')

    if not texto:
        return jsonify({"erro": "O texto não pode estar vazio"}), 400

    # 1. Gera as perguntas usando a lógica pedagógica
    perguntas = gerar_perguntas_pedagogicas(texto)

    # 2. Salva o progresso no SQLite para acompanhamento individualizado
    try:
        conn = sqlite3.connect('educacao.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO progresso_leitura (aluno_nome, texto_analisado, perguntas_geradas) VALUES (?, ?, ?)",
            (nome_aluno, texto, perguntas)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        return jsonify({"erro": f"Erro ao salvar no banco: {str(e)}"}), 500

    # 3. Retorna para o front-end (HTML/JS) mostrar ao aluno
    return jsonify({
        "aluno": nome_aluno,
        "perguntas": perguntas.split(" | ")
    })

