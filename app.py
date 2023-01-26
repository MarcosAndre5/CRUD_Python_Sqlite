import db
import mensagens as msg

def gerenciar_usuarios():
    while True:
        titulo = "USUÁRIOS"
        msg.exibir_cabecalho(titulo)
        msg.exibir_usuarios()
        try:
            # exibe as opções disponíveis
            print("O que deseja fazer?")
            print("1 = Novo Usuário\n2 = Editar dados do Usuário\n3 = Deletar Usuário\n4 = Voltar ao Menu Inicial")
            opcao = int(input("=> "))

            # verifica qual opção o usuário escolheu
            if opcao == 1:
                msg.opcao_novo_usuario()
            elif opcao == 2:
                msg.opcao_atualizar_usuario()
            elif opcao == 3:
                msg.opcao_deletar_usuario()
            elif opcao == 4:
                main()
            else:
                print("Opção não reconhecida, por favor informar um número")
        except ValueError as e :
            print("Opção não reconhecida, por favor informar um número")
        except Exception:
            exit(0)

def gerenciar_pacientes():
    while True:
        titulo = "PACIENTES"
        msg.exibir_cabecalho(titulo)
        msg.exibir_pacientes()
        try:
            # exibe as opções disponíveis
            print("O que deseja fazer?")
            print("1 = Nova Paciente\n2 = Editar dados do Paciente\n3 = Deletar Paciente\n4 = Voltar ao Menu Inicial")
            opcao = int(input("=> "))

            # verifica qual opção o usuário escolheu
            if opcao == 1:
                msg.opcao_novo_paciente()
            elif opcao == 2:
                msg.opcao_atualizar_paciente()
            elif opcao == 3:
                msg.opcao_deletar_paciente()
            elif opcao == 4:
                main()
            else:
                print("Opção não reconhecida, por favor informar um número")
        except ValueError as e :
            print("Opção não reconhecida, por favor informar um número")
        except Exception:
            exit(0)

def gerenciar_funcionarios():
    while True:
        titulo = "FUNCIONARIOS"
        msg.exibir_cabecalho(titulo)
        msg.exibir_funcionarios()
        try:
            # exibe as opções disponíveis
            print("O que deseja fazer?")
            print("1 = Novo Funcionario\n2 = Editar dados do Funcionario\n3 = Deletar Funcionario\n4 = Voltar ao Menu Inicial")
            opcao = int(input("=> "))

            # verifica qual opção o usuário escolheu
            if opcao == 1:
                msg.opcao_novo_funcionario()
            elif opcao == 2:
                msg.opcao_atualizar_funcionario()
            elif opcao == 3:
                msg.opcao_deletar_funcionario()
            elif opcao == 4:
                main()
            else:
                print("Opção não reconhecida, por favor informar um número")
        except ValueError as e :
            print("Opção não reconhecida, por favor informar um número")
        except Exception:
            exit(0)

def main():
    while True:
        titulo = "CLINICA ODONTO"
        msg.exibir_cabecalho(titulo)

        try:
            # exibe as opções disponíveis
            print("O que deseja gerenciar?")
            print("1 = Usuarios\n2 = Pacientes\n3 = Funcionarios\n4 = Sair do Sistema")
            opcao = int(input("=> "))

            # verifica qual opção o usuário escolheu
            if opcao == 1:
                gerenciar_usuarios()
            elif opcao == 2:
                gerenciar_pacientes()
            elif opcao == 3:
                gerenciar_funcionarios()
            elif opcao == 4:
                exit()
            else:
                print("Opção não reconhecida, por favor informar um número")    
        except ValueError as e :
            print("Opção não reconhecida, por favor informar um número")
        except Exception:
            exit(0)

if __name__ == "__main__":
    db.criar_tabela_usuarios()
    db.criar_tabela_pacientes()
    db.criar_tabela_funcionarios()

    main()
