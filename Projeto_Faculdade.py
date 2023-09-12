from Fun_Compras import *
from Fun_Tarefas import *
from Fun_Carteira import *
from time import sleep

while True:
    menu(["Lista de Tarefas", "Lista de Compra", "Carteira", "Fechar o Sistema"])
    sleep(0.5)
    op = input("Digite a opção desejada: ").strip()
    match op:
        case "1":
            adt = "Arquivo_De_Tarefas"
            title("Lista de Tarefas")
            ler_arquivo_tarefas(adt)
            while True:
                tab(["Adicionar Tarefa", "Remover Tarefa", "Remover Todas as tarefas","Retornar ao Menu"])
                opc_tarefa = input(">> ").strip()
                match opc_tarefa:
                    case "1":
                        adicionar_tarefa(adt)
                    case "2":
                        rem_tarefas(adt)
                    case "3":
                        print("Removendo todos os elementos...")
                        rem_toda_tarefa(adt)
                        sleep(2)
                        print("elementos removidos com sucesso!")
                    case "4":
                        print("Retornando ao Menu")
                        break
                    case _:
                        print("Opção Inválida")
                        sleep(1)
                        print("Digite a opção corretamente!")
                        sleep(0.5)
        case "2":
            adc = "Arquivo_De_Compras"
            title("Lista de Compras")
            ler_arquivo_compras(adc)
            while True:
                tab(["Adicionar Compra", "Remover Compra", "Remover Todas as Compras", "Retornar ao Menu"])
                opc_tarefa = input(">> ").strip()
                match opc_tarefa:
                    case "1":
                        adicionar_compra(adc)

                    case "2":
                        rem_compras(adc)

                    case "3":
                        print("Removendo todos os elementos...")
                        rem_toda_compra(adc)
                        sleep(2)
                        print("elementos removidos com sucesso!")
                    case "4":
                        print("Retornando ao Menu")
                        break
                    case _:
                        print("Opção Inválida")
                        sleep(1)
                        print("Digite a opção corretamente!")
                        sleep(0.5)
        case "3":
            ac = "Arquivo_Carteira"
            title("Carteira")
            while True:
                tab(["Depositar na Carteira", "Retirar valor da Carteira","Retornar ao Menu"])
                opc_carteira = input(">> ").strip()
                match opc_carteira:
                    case "1":
                        adicionar_carteira(ac)

                    case "2":
                        print()
                    case "3":
                        print("Retornando ao Menu")
                        break
                    case _:
                        print("Opção Inválida")
                        sleep(1)
                        print("Digite a opção corretamente!")
                        sleep(0.5)
        case "4":
            print("Fechando o sistema...")
            sleep(1)
            break
        case _:
            print("Opção Inválida")
            sleep(1)
            print("Digite a opção corretamente!")
            sleep(0.5)
