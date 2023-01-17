import sqlite3 # https://medium.com/@francisco_51376/crud-na-pr%C3%A1tica-com-python-sqlite-8e15d11bbac9

conn = sqlite3.connect("sistemaClinica.db") # conecta ao banco de dados 'sistemaClinica', caso o banco não exista ele será criado

def criar_tabela_pacientes(): # cria a tabela 'pacientes' caso ela não exista
    cursor = conn.cursor()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome text,
            cpf text,
            telefone text,
            rua text,
            cidade text,
            estado text,
            indicacao text
        )"""
    )

def add_paciente(nome, cpf, telefone, rua, cidade, estado, indicacao): # adiciona um novo paciente
    conn.execute("INSERT INTO pacientes (nome, cpf, telefone, rua, cidade, estado, indicacao) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome, cpf, telefone, rua, cidade, estado, indicacao, ))
    conn.commit()

def deletar_paciente(id_paciente): # remove o paciente da tabela
    conn.execute("DELETE FROM pacientes WHERE id_paciente = ?", (id_paciente, ))
    conn.commit()

def atualizar_paciente(id_paciente, nome, cpf, telefone, rua, cidade, estado, indicacao): # atualizar dados de paciente
    conn.execute("UPDATE pacientes SET nome = ?, cpf = ?, telefone = ?, rua = ?, cidade = ?, estado = ?, indicacao = ? WHERE id_paciente = ?", (nome, cpf, telefone, rua, cidade, estado, indicacao, id_paciente, ))
    conn.commit()

def get_paciente(): # retorna um cursor (retorna a lista de pacientes cadastros)
    return conn.execute("SELECT * FROM pacientes")
