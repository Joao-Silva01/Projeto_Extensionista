from time import sleep


# Funções de Menu do Projeto
def menu(op):  # Função para exibir o menu do projeto
    title("Menu do Projeto")
    cont = 1
    for opc in op:
        print(f"{cont}- {opc}")
        cont += 1
        sleep(0.5)
    borda()


def title(txt):  # Função para personalizar o titulo
    sleep(0.5)
    borda()
    sleep(0.5)
    print(txt.center(42))
    sleep(0.5)
    borda()
    sleep(0.5)


def borda(tam=42):  # Função para adicionar bordas
    print("-" * tam)


def tab(op):  # Função para subtítulo
    print('=' * 35)
    print("Opções".center(42))
    print('=' * 35)
    cont = 1
    for opc in op:
        print(f"{cont}- {opc}")
        cont += 1
        sleep(0.5)
    borda()
