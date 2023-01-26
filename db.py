import sqlite3

# conecta ao banco de dados 'sistemaClinica', caso o banco não exista ele será criado
conn = sqlite3.connect("sistemaClinica.db")

# cria a tabela 'usuarios' caso ela não exista
def criar_tabela_usuarios():
    cursor = conn.cursor()
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT,
            senha TEXT,
            situacao INTEGER
        )"""
    )

# cria a tabela 'pacientes' caso ela não exista
def criar_tabela_pacientes():
    cursor = conn.cursor()
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT UNIQUE,
            telefone TEXT,
            rua TEXT,
            cidade TEXT,
            estado TEXT,
            indicacao TEXT,
            situacao INTEGER
        )"""
    )

# cria a tabela 'funcionarios' caso ela não exista
def criar_tabela_funcionarios():
    cursor = conn.cursor()
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT UNIQUE,
            telefone TEXT,
            rua TEXT,
            cidade TEXT,
            estado TEXT,
            salario REAL,
            funcao TEXT,
            situacao INTEGER
        )"""
    )

ativo = 1
inativo = 0

''' Funções de CRUD de Usuarios:
        Adicionar
        Atualizar
        Listar
        Deletar
'''
# adiciona um novo paciente
def adicionar_usuario(login, senha):
    conn.execute("INSERT INTO usuarios (login, senha, situacao) VALUES (?, ?, ?)", (login, senha, ativo, ))
    conn.commit()

# atualizar dados de paciente
def atualizar_usuario(id_usuario, login, senha):
    conn.execute("UPDATE usuarios SET login = ?, senha = ? WHERE id_usuario = ?", (login, senha, id_usuario, ))
    conn.commit()

# retorna a lista de pacientes cadastros
def listar_usuario():
    return conn.execute("SELECT * FROM usuarios WHERE situacao = ?", (ativo, ))

# remove o paciente da tabela
def deletar_usuario(id_usuario):
    #conn.execute("DELETE FROM usuarios WHERE id_usuario = ?", (id_usuario, ))
    conn.execute("UPDATE usuarios SET situacao = ? WHERE id_usuario = ?", (inativo, id_usuario, ))
    conn.commit()

''' Funções de CRUD de Pacientes:
        Adicionar
        Atualizar
        Listar
        Deletar
'''
# adiciona um novo paciente
def adicionar_paciente(nome, cpf, telefone, rua, cidade, estado, indicacao):
    cursor = conn.execute("SELECT id_paciente FROM pacientes WHERE cpf = ?", (cpf, ))

    cpf_existe = cursor.fetchall()

    if len(cpf_existe) == 0:
        conn.execute("""INSERT INTO pacientes (nome, cpf, telefone, rua, cidade, estado, indicacao, situacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (nome, cpf, telefone, rua, cidade, estado, indicacao, ativo, ))
        conn.commit()
    else:
        print("\n\nO CPF já foi cadastrado! Tente Novamente.\n\n")

# atualizar dados de paciente
def atualizar_paciente(id_paciente, nome, cpf, telefone, rua, cidade, estado, indicacao):
    conn.execute("""UPDATE pacientes
        SET nome = ?, cpf = ?, telefone = ?, rua = ?, cidade = ?, estado = ?, indicacao = ?
        WHERE id_paciente = ?""", (nome, cpf, telefone, rua, cidade, estado, indicacao, id_paciente, ))
    conn.commit()

# retorna a lista de pacientes cadastros
def listar_paciente():
    return conn.execute("SELECT * FROM pacientes WHERE situacao = ?", (ativo, ))

# remove o paciente da tabela
def deletar_paciente(id_paciente):
    #conn.execute("DELETE FROM pacientes WHERE id_paciente = ?", (id_paciente, ))
    conn.execute("UPDATE pacientes SET situacao = ? WHERE id_paciente = ?", (inativo, id_paciente, ))
    conn.commit()

''' Funções de CRUD de Funcionarios:
        Adicionar
        Atualizar
        Listar
        Deletar
'''
# adiciona um novo funcionario
def adicionar_funcionario(nome, cpf, telefone, rua, cidade, estado, salario, funcao):
    cursor = conn.execute("SELECT id_funcionario FROM funcionarios WHERE cpf = ?", (cpf, ))

    cpf_existe = cursor.fetchall()

    if len(cpf_existe) == 0:
        conn.execute("""INSERT INTO funcionarios (nome, cpf, telefone, rua, cidade, estado, salario, funcao, situacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (nome, cpf, telefone, rua, cidade, estado, salario, funcao, ativo, ))
        conn.commit()
    else:
        print("\n\nO CPF já foi cadastrado! Tente Novamente.\n\n")

# atualizar dados de funcionario
def atualizar_funcionario(id_funcionario, nome, cpf, telefone, rua, cidade, estado, salario, funcao):
    conn.execute("""UPDATE funcionarios
        SET nome = ?, cpf = ?, telefone = ?, rua = ?, cidade = ?, estado = ?, salario = ?, funcao = ?
        WHERE id_funcionario = ?""", (nome, cpf, telefone, rua, cidade, estado, salario, funcao, id_funcionario, ))
    conn.commit()

# retorna a lista de funcionario cadastros
def listar_funcionario():
    return conn.execute("SELECT * FROM funcionarios WHERE situacao = ?", (ativo, ))

# remove o funcionario da tabela
def deletar_funcionario(id_funcionario):
    #conn.execute("DELETE FROM funcionarios WHERE id_funcionario = ?", (id_funcionario, ))
    conn.execute("UPDATE funcionarios SET situacao = ? WHERE id_funcionario = ?", (inativo, id_funcionario, ))
    conn.commit()
