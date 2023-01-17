import db

MENU_INICIAL = 99

def exibir_cabecalho(): # imprimi o cabeçalho no terminal utilizando o tamanho maximo de 60 caracteres
    QTD_COLUNAS = 60
    print ("-" * QTD_COLUNAS)
    print ("{:^60}".format("PACIENTES"))
    print ("-" * QTD_COLUNAS)
    print ("{:^60}\n\n".format("tecle 99 volta para o menu inicial, [CTRL+C] sai"))
    print ("-" * QTD_COLUNAS)

def exibir_pacientes(): # exibe a lista de pacientes cadastrados, com algumas formatações básicas
    print(" ID | NOME | CPF | TELEFONE | RUA | CIDADE | ESTADO | INDICACAO")
    print("-" * 60)
    for paciente in db.get_paciente(): # check = \u2713 é o caracter unicode que representa o concluido
        check = u'\u2713' if paciente[2] == 1 else ""
        t = "[{}] | {} | {} | {} | {} | {} | {} | {}".format(paciente[0], paciente[1], paciente[2], paciente[3], paciente[4], paciente[5], paciente[6], paciente[7], check)
        print (t)
    print ("-" * 60)

def opcao_novo_paciente():
    nome = input("Nome do paciente => ")
    cpf = input("CPF do paciente => ")
    telefone = input("Telefone do paciente => ")
    rua = input("Rua que paciente mora => ")
    cidade = input("Cidade que paciente mora => ")
    estado = input("Estado que paciente mora => ")
    indicacao = input("Como ficou sabendo da nossa clinica? => ")

    print ("adicionando Paciente -> " + str(nome))

    if nome != str(MENU_INICIAL):
        db.add_paciente(nome, cpf, telefone, rua, cidade, estado, indicacao)

def opcao_atualizar_paciente():
    id_paciente = int(input("Qual paciente quer atualizar? digite o código => "))

    nome = input("Nome do paciente => ")
    cpf = input("CPF do paciente => ")
    telefone = input("Telefone do paciente => ")
    rua = input("Rua que paciente mora => ")
    cidade = input("Cidade que paciente mora => ")
    estado = input("Estado que paciente mora => ")
    indicacao = input("Como ficou sabendo da nossa clinica? => ")

    print ("Atualizando Paciente -> " + str(id_paciente))
    
    if id_paciente != MENU_INICIAL:
        db.atualizar_paciente(id_paciente, nome, cpf, telefone, rua, cidade, estado, indicacao)

def opcao_deletar_paciente():
    id_paciente = int(input("Qual paciente quer deletar? digite o código => "))

    print ("Deletando Paciente -> " + str(id_paciente))
    
    if id_paciente != MENU_INICIAL:
        db.deletar_paciente(id_paciente)
