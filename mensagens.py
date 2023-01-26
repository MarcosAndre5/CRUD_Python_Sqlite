import db

# imprimi o cabeçalho no terminal
def exibir_cabecalho(titulo):
    print("-" * 60)
    print("{:^60}".format(titulo))
    print("-" * 60)
    print("{:^60}".format("Tecle os números correspondentes a cada opção do sistema."))
    print("-" * 60)

# exibe a lista de usuarios cadastrados, com algumas formatações básicas
def exibir_usuarios():
    print(" ID | LOGIN | SENHA")
    print("-" * 60)
    
    for usuario in db.listar_usuario(): # check = \u2713 é o caracter unicode que representa o concluido
        check = u'\u2713' if usuario[2] == 1 else ""
        print("[{}] | {} | {}".format(usuario[0], usuario[1], usuario[2], check))

    print ("-" * 60)

# exibe o formulario para cadastrar usuário
def opcao_novo_usuario():
    login = input("Login do usuário => ")
    senha = input("Senha do usuário => ")

    print ("Adicionando Usuário -> " + str(login))

    db.adicionar_usuario(login, senha)

# exibe o formulario para atualizar usuário
def opcao_atualizar_usuario():
    id_usuario = int(input("Qual Usuário quer atualizar? digite o ID => "))

    login = input("Login do usuário => ")
    senha = input("Senha do usuário => ")

    print ("Atualizando Usuário -> " + str(id_usuario))

    db.atualizar_usuario(id_usuario, login, senha)

# exibe o formulario para deletar o usuário
def opcao_deletar_usuario():
    id_usuario = int(input("Qual Usuário quer deletar? digite o ID => "))

    print ("Deletando Usuário -> " + str(id_usuario))

    db.deletar_usuario(id_usuario)

# exibe a lista de pacientes cadastrados, com algumas formatações básicas
def exibir_pacientes():
    print(" ID | NOME | CPF | TELEFONE | RUA | CIDADE | ESTADO | INDICACAO")
    print("-" * 60)

    for paciente in db.listar_paciente(): # check = \u2713 é o caracter unicode que representa o concluido
        check = u'\u2713' if paciente[2] == 1 else ""
        print("[{}] | {} | {} | {} | {} | {} | {} | {}".format(paciente[0],paciente[1],paciente[2],paciente[3],paciente[4],paciente[5],paciente[6],paciente[7],check))

    print ("-" * 60)

# exibe o formulario para cadastrar paciente
def opcao_novo_paciente():
    nome = input("Nome do paciente => ")
    cpf = input("CPF do paciente => ")
    telefone = input("Telefone do paciente => ")
    rua = input("Rua que paciente mora => ")
    cidade = input("Cidade que paciente mora => ")
    estado = input("Estado que paciente mora => ")
    indicacao = input("Como ficou sabendo da nossa clinica? => ")

    print ("Adicionando Paciente -> " + str(nome))

    db.adicionar_paciente(nome, cpf, telefone, rua, cidade, estado, indicacao)

# exibe o formulario para atualizar paciente
def opcao_atualizar_paciente():
    id_paciente = int(input("Qual Paciente quer atualizar? digite o ID => "))

    nome = input("Nome do paciente => ")
    cpf = input("CPF do paciente => ")
    telefone = input("Telefone do paciente => ")
    rua = input("Rua que paciente mora => ")
    cidade = input("Cidade que paciente mora => ")
    estado = input("Estado que paciente mora => ")
    indicacao = input("Como ficou sabendo da nossa clinica? => ")

    print ("Atualizando Paciente -> " + str(id_paciente))

    db.atualizar_paciente(id_paciente, nome, cpf, telefone, rua, cidade, estado, indicacao)

# exibe o formulario para deletar o paciente
def opcao_deletar_paciente():
    id_paciente = int(input("Qual Paciente quer deletar? digite o ID => "))

    print ("Deletando Paciente -> " + str(id_paciente))

    db.deletar_paciente(id_paciente)

# exibe a lista de funcionarios cadastrados, com algumas formatações básicas
def exibir_funcionarios():
    print(" ID | NOME | CPF | TELEFONE | RUA | CIDADE | ESTADO | SALARIO | FUNCAO")
    print("-" * 60)

    for funcionario in db.listar_funcionario(): # check = \u2713 é o caracter unicode que representa o concluido
        check = u'\u2713' if funcionario[2] == 1 else ""
        print("[{}] | {} | {} | {} | {} | {} | {} | {}".format(funcionario[0],funcionario[1],funcionario[2],funcionario[3],funcionario[4],funcionario[5],funcionario[6],funcionario[7],funcionario[8],check))

    print ("-" * 60)

# exibe o formulario para cadastrar funcionário
def opcao_novo_funcionario():
    nome = input("Nome do funcionário => ")
    cpf = input("CPF do funcionário => ")
    telefone = input("Telefone do funcionário => ")
    rua = input("Rua que funcionário mora => ")
    cidade = input("Cidade que funcionário mora => ")
    estado = input("Estado que funcionário mora => ")
    salario = float(input("Salário do funcionário => "))
    funcao = input("Função do funcionário => ")

    print ("Adicionando Funcionário -> " + str(nome))

    db.adicionar_funcionario(nome, cpf, telefone, rua, cidade, estado, salario, funcao)

# exibe o formulario para atualizar funcionário
def opcao_atualizar_funcionario():
    id_funcionario = int(input("Qual Funcionário quer atualizar? digite o ID => "))

    nome = input("Nome do funcionário => ")
    cpf = input("CPF do funcionário => ")
    telefone = input("Telefone do funcionário => ")
    rua = input("Rua que funcionário mora => ")
    cidade = input("Cidade que funcionário mora => ")
    estado = input("Estado que funcionário mora => ")
    salario = float(input("Salário do funcionário => "))
    funcao = input("Função do funcionário => ")

    print ("Atualizando Funcionário -> " + str(id_funcionario))

    db.atualizar_funcionario(id_funcionario, nome, cpf, telefone, rua, cidade, estado, salario, funcao)

# exibe o formulario para deletar o funcionário
def opcao_deletar_funcionario():
    id_funcionario = int(input("Qual Paciente quer deletar? digite o ID => "))

    print ("Deletando Funcionário -> " + str(id_funcionario))

    db.deletar_funcionario(id_funcionario)
