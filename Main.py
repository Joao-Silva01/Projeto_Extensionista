from FunctionsTasks import *
from FunctionsBuys import *
from FunctionsWallet import *

while True:
    tab("Menu do Projeto", ["Tarefas", "Compras", "Carteira", "Desligar o Sistema"])
    option = validacao(">> ", 'int')

    match option:
        case 1:
            while True:
                tab('Menu Tarefas',
                    ["Listar as tarefas", "Adicionar Tarefa", "Editar Tarefa", "Histórico", "Remover Tarefa",
                     "Retornar ao Menu"])
                optionTask = validacao(">> ", 'int')

                match optionTask:
                    case 1:
                        ListAllTasks()

                    case 2:
                        addTarefa()

                    case 3:
                        updateTarefa()

                    case 4:
                        HistoricTasks()

                    case 5:
                        RemoveTarefas()

                    case 6:
                        cores("\nRetornando ao Menu\n", 'verde')
                        break

                    case _:
                        cores("\nOpção Inválida!\n", 'vermelho')

        case 2:
            while True:
                tab('Menu Compras',
                    ["Listar Produtos", "Adicionar Produto", "Editar Produto", "Remover Produto", "Histórico",
                     "Retornar ao Menu"])
                opc_tarefa = validacao(">> ", 'int')

                match opc_tarefa:
                    case 1:
                        ListProducts()
                    case 2:
                        addProduct()

                    case 3:
                        productUpdate()

                    case 4:
                        RemoveProducts()

                    case 5:
                        HistoricProducts()

                    case 6:
                        cores("\nRetornando ao Menu\n", 'verde')
                        break

                    case _:
                        cores("\nOpção Inválida\n", 'vermelho')

        case 3:
            while True:
                tab('Carteira',
                    ["Saldo da conta", "Depósito", "Saque", "Extrato",
                     "Retornar ao Menu"])
                opc_carteira = validacao(">> ", 'int')

                match opc_carteira:
                    case 1:
                        print()
                        TotalCarteira(False)
                        print()

                    case 2:
                        Deposito()

                    case 3:
                        Saque()

                    case 4:
                        Extrato()

                    case 5:
                        cores("\nRetornando ao Menu\n", 'verde')
                        break

                    case _:
                        cores("\nOpção Inválida\n", 'vermelho')

        case 4:
            print("\nFechando o sistema...\n")
            break

        case _:
            cores("\nOpção Inválida, digite a opção corretamente!!\n", 'vermelho')
