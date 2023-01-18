import sqlite3

# conecta ao banco de dados 'sistemaClinica', caso o banco não exista ele será criado
conn = sqlite3.connect("sistemaClinica.db")

# cria a tabela 'usuarios' caso ela não exista
def criar_tabela_usuarios():
    cursor = conn.cursor()
    
    conn.execute("""CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT,
        senha TEXT)"""
    )

# cria a tabela 'pacientes' caso ela não exista
def criar_tabela_pacientes():
    cursor = conn.cursor()
    
    conn.execute("""CREATE TABLE IF NOT EXISTS pacientes (
        id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf TEXT,
        telefone TEXT,
        rua TEXT,
        cidade TEXT,
        estado TEXT,
        indicacao TEXT)"""
    )

# cria a tabela 'funcionarios' caso ela não exista
def criar_tabela_funcionarios():
    cursor = conn.cursor()
    
    conn.execute("""CREATE TABLE IF NOT EXISTS funcionarios (
        id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf TEXT,
        telefone TEXT,
        rua TEXT,
        cidade TEXT,
        estado TEXT,
        salario REAL,
        funcao TEXT)"""
    )

''' Funções de CRUD de Usuarios:
        Adicionar
        Atualizar
        Listar
        Deletar
'''
# adiciona um novo paciente
def adicionar_usuario(login, senha):
    conn.execute("INSERT INTO usuarios (login, senha) VALUES (?, ?)", (login, senha, ))
    conn.commit()

# atualizar dados de paciente
def atualizar_usuario(id_usuario, login, senha):
    conn.execute("UPDATE usuarios SET login = ?, senha = ? WHERE id_usuario = ?", (login, senha, id_usuario, ))
    conn.commit()

# retorna a lista de pacientes cadastros
def listar_paciente():
    return conn.execute("SELECT * FROM usuarios")

# remove o paciente da tabela
def deletar_paciente(id_usuario):
    conn.execute("DELETE FROM usuarios WHERE id_usuario = ?", (id_usuario, ))
    conn.commit()

''' Funções de CRUD de Pacientes:
        Adicionar
        Atualizar
        Listar
        Deletar
'''
# adiciona um novo paciente
def adicionar_paciente(nome, cpf, telefone, rua, cidade, estado, indicacao):
    conn.execute("INSERT INTO pacientes (nome, cpf, telefone, rua, cidade, estado, indicacao) VALUES (?, ?, ?, ?, ?, ?, ?)", (nome, cpf, telefone, rua, cidade, estado, indicacao, ))
    conn.commit()

# atualizar dados de paciente
def atualizar_paciente(id_paciente, nome, cpf, telefone, rua, cidade, estado, indicacao):
    conn.execute("UPDATE pacientes SET nome = ?, cpf = ?, telefone = ?, rua = ?, cidade = ?, estado = ?, indicacao = ? WHERE id_paciente = ?", (nome, cpf, telefone, rua, cidade, estado, indicacao, id_paciente, ))
    conn.commit()

# retorna a lista de pacientes cadastros
def listar_paciente():
    return conn.execute("SELECT * FROM pacientes")

# remove o paciente da tabela
def deletar_paciente(id_paciente):
    conn.execute("DELETE FROM pacientes WHERE id_paciente = ?", (id_paciente, ))
    conn.commit()

''' Funções de CRUD de Funcionarios:
        Adicionar
        Atualizar
        Listar
        Deletar
'''
# adiciona um novo funcionario
def adicionar_funcionario(nome, cpf, telefone, rua, cidade, estado, indicacao):
    conn.execute("INSERT INTO funcionarios (nome, cpf, telefone, rua, cidade, estado, salario, funcao) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nome, cpf, telefone, rua, cidade, estado, salario, funcao, ))
    conn.commit()

# atualizar dados de funcionario
def atualizar_funcionario(id_funcionario, nome, cpf, telefone, rua, cidade, estado, salario, funcao):
    conn.execute("UPDATE funcionarios SET nome = ?, cpf = ?, telefone = ?, rua = ?, cidade = ?, estado = ?, salario = ?, funcao = ? WHERE id_funcionario = ?", (nome, cpf, telefone, rua, cidade, estado, salario, funcao, id_funcionario, ))
    conn.commit()

# retorna a lista de funcionario cadastros
def listar_funcionario():
    return conn.execute("SELECT * FROM funcionarios")

# remove o funcionario da tabela
def deletar_funcionario(id_funcionario):
    conn.execute("DELETE FROM funcionarios WHERE id_funcionario = ?", (id_funcionario, ))
    conn.commit()
