# Funções de Menu do Projeto

def title(text):
    cores('-' * 42, 'bold')
    cores(f"{text}".center(42), 'bold')
    cores('-' * 42, 'bold')

# Função para formatar os menus
def tab(text, options):  # Função para subtítulo
    title(text)
    contador = 1
    print()
    for option in options:
        bold = cores(contador, 'bold', False)
        under = cores(f'{option}', "underline", False)
        print(f"{bold}- {under}")
        contador += 1
    print()
    cores('-' * 42, 'bold')


# Função para validar o tipo da variavel
def validacao(info, type):
    match type:
        case 'int':
            while True:
                try:
                    msg = int(input(info))
                except (ValueError, TypeError):
                    cores("\nInválido\n", 'vermelho')
                except KeyboardInterrupt:
                    cores("\nNada foi digitado.\n", 'vermelho')
                else:
                    return msg
        case 'float':
            while True:
                try:
                    user = input(info)

                    user = user.replace(',', '.')

                    msg = float(user)

                except (ValueError, TypeError):
                    cores("\nInválido\n", 'vermelho')
                except KeyboardInterrupt:
                    cores("\nNada foi digitado.\n", 'vermelho')
                else:
                    return msg

        case 'string':
            while True:
                try:
                    msg = str(input(info)).strip()
                    if not msg:
                        raise ValueError(cores("Campo vazio não é permitido.", 'vermelho', False))
                except (ValueError, TypeError):
                    cores("\nInválido\n", 'vermelho')
                except KeyboardInterrupt:
                    cores("\nNada foi digitado.\n", 'vermelho')
                else:
                    return msg


# Função para mudar as cores de algumas variaveis
def cores(texto, cor, mostra=True):
    match cor:
        case 'verde':
            if mostra:
                return print(f'\033[1;32m{texto}\033[m')
            else:
                return f'\033[1;32m{texto}\033[m'

        case 'vermelho':
            if mostra:
                return print(f'\033[1;31m{texto}\033[m')
            else:
                return f'\033[1;31m{texto}\033[m'

        case 'amarelo':
            if mostra:
                return print(f'\033[1;33m{texto}\033[m')
            else:
                return f'\033[1;33m{texto}\033[m'

        case 'bold':
            if mostra:
                return print(f'\033[1m{texto}\033[m')
            else:
                return f'\033[1m{texto}\033[m'

        case 'underline':
            if mostra:
                return print(f'\033[4m{texto}\033[m')
            else:
                return f'\033[4m{texto}\033[m'
