from time import sleep


def adicionar_carteira(arquivo):  # Função para adicionar um elemento no arquivo.txt
    with open(arquivo, 'at') as a2:
        carteira = float(input("Quanto deseja depositar na carteira: R$"))
        a2.write(f'{carteira:.2f} \n')
        sleep(1)
        print(f'R${carteira} foi depositado!')
        sleep(1)


def remove_carteira(_arquivo):  # Função para remover um elemento específico do arquivo.txt
    carteira_rem = float(input("Digite o nome da Compra para remove-lá: "))
    with open(_arquivo, 'r') as arquivo:
        arq_compra = arquivo.readlines()


