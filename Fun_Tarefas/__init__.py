from Fun_Alea import *


def ler_arquivo_tarefas(arquivo):  # Função para ler o arquivo de forma de tabela
    with open(arquivo, 'rt') as a1:
        cont = 1
        for linha in a1:
            dado = linha.split(';')
            dado[0] = dado[0].replace("\n", "")
            print(f"{cont}- {dado[0]:<30}")
            cont += 1
            sleep(0.5)


def adicionar_tarefa(arquivo):  # Função para adicionar um elemento no arquivo.txt
    with open(arquivo, 'at') as a2:
        tarefa = str(input("Digite o nome da tarefa: ")).strip()
        tarefa_normal = tarefa
        a2.write(f'{tarefa_normal} \n')
        sleep(1)
        print(f'A tarefa {tarefa} foi adicionada!')
        sleep(1)


def rem_tarefas(_arquivo):  # Função para remover um elemento específico do arquivo.txt
    tarefa_rem = str(input("Digite o nome da tarefa para remove-lá: ")).strip().upper()
    with open(_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    with open(_arquivo, 'w') as arquivo:
        for linha in linhas:
            if linha.upper().strip() != tarefa_rem:
                arquivo.write(linha)
            elif linha.strip() not in linhas:
                print("Tarefa foi removida!!")


def rem_toda_tarefa(_arquivo):  # Função para remover todos os elementos.txt
    with open(_arquivo, 'w') as arquivo:
        pass
