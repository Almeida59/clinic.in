import sqlite3

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect("clinic.db")

# Criar a tabela de pacientes
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            nome TEXT,
            cpf TEXT,
            exame TEXT,
            data_hora TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS arquivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            arquivo_nome TEXT,
            caminho_arquivo TEXT
        )
    """)
    conexao.commit()
    conexao.close()

# Salvar paciente no banco de dados
def salvar_paciente(user_id, nome=None, cpf=None, exame=None, data_hora=None):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO pacientes (user_id, nome, cpf, exame, data_hora) VALUES (?, ?, ?, ?, ?)",
                   (user_id, nome, cpf, exame, data_hora))
    conexao.commit()
    conexao.close()

# Salvar arquivo no banco de dados
def salvar_arquivo_paciente(user_id, arquivo_nome, caminho_arquivo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO arquivos (user_id, arquivo_nome, caminho_arquivo) VALUES (?, ?, ?)",
                   (user_id, arquivo_nome, caminho_arquivo))
    conexao.commit()
    conexao.close()

# Criar tabelas no banco de dados ao rodar este script
if __name__ == "__main__":
    criar_tabela()
    print("Banco de dados e tabelas criados com sucesso!")
