import db
import mensagens as msg

def main():
    while True:
        msg.exibir_cabecalho()
        msg.exibir_pacientes()
        try:
            # exibe as opções disponíveis
            opcao = int(input("O que deseja fazer?\n1 = Nova Paciente\n2 = Editar dados do Paciente\n3 = Deletar Paciente\n"))

            # verifica qual opção o usuário escolheu
            if opcao == 1:
                msg.opcao_novo_paciente()
            elif opcao == 2:
                msg.opcao_atualizar_paciente()
            elif opcao == 3:
                msg.opcao_deletar_paciente()
            else:
                print ("Opção não reconhecida, por favor informar um número")    
        except ValueError as e :
            print ("Opção não reconhecida, por favor informar um número")
        except Exception:
            exit(0)

if __name__ == "__main__":
    db.criar_tabela_pacientes()

    main()