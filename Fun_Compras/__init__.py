from time import sleep


def ler_arquivo_compras(arquivo):  # Função para ler o arquivo de forma de tabela
    with open(arquivo, 'rt') as a1:
        cont = 1
        for linha in a1:
            dado = linha.split(';')
            dado[1] = dado[1].replace("\n", "")
            print(f"R${dado[1]:-<30}{dado[0]:->3}")
            cont += 1
            sleep(0.5)


def adicionar_compra(arquivo):  # Função para adicionar um elemento no arquivo.txt
    with open(arquivo, 'at') as ar:
        compra = str(input("Digite o nome da Compra: ")).strip()
        compra_normal = compra
        preco = leia_float("Digite o preço da Compra: ")
        ar.write(f'{compra_normal};{preco:.2f} \n')
        sleep(1)
        print(f'A compra {compra} foi colocada na lista!')
        sleep(1)


def rem_compras(_arquivo):  # Função para remover um elemento específico do arquivo.txt
    compra_rem = str(input("Digite o nome da Compra para remove-lá: ")).strip().upper()
    with open(_arquivo, 'r') as arquivo:
        arq_compra = arquivo.readlines()

    with open(_arquivo, 'w') as arquivo:
        for linha in arq_compra:
            nome = linha.split(';')
            if nome[0].upper().strip() != compra_rem:
                arquivo.write(linha)
            elif linha.strip() not in arq_compra:
                print("Tarefa foi removida!!")


def leia_float(msg):  # Função para verificar se o usuário digitou corretamente.
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("Digite o preço correto! Ex:'10.50' ")
        except KeyboardInterrupt:
            print("Nada foi digitado.")
        else:
            return n


def rem_toda_compra(arquivo):  # Função para remover um elemento específico do arquivo.txt
    with open(arquivo, 'w') as remove:
        pass
