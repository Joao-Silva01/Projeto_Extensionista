from Database import *
from Functions import *


# Função para adicionar um produto no database
def addProduct():
    condicao = True
    while condicao:
        nomeProduto = validacao("Digite o nome do produto: ", 'string')
        precoProduto = validacao("Preço: R$ ", 'float')
        quantidade = validacao("Quantidade: ", 'int')

        # Adiciona os dados
        db.execute(
            f"INSERT INTO ListBuy (nomeProduto, precoProduto, quantidadeProdutos) VALUES ('{nomeProduto}', {precoProduto}, '{quantidade}')")
        db.execute(
            f"INSERT INTO HistoricBuys (historic, data) VALUES ('Adição : {nomeProduto}', datetime('now','-3 "
            f"hours'))")

        # Salvando os dados no database
        conexao.commit()

        cores("\nProduto adicionado\n", 'verde')
        while True:
            op = str(input("Quer adicionar outro produto?[Sim|Não] ")).lower()
            match op[0].lower():
                case 's':
                    break
                case 'n':
                    condicao = False
                    break
                case _:
                    cores("\nOpção inválida\n", 'vermelho')


# Função para editar um produto no database
def productUpdate():
    db.execute('SELECT * FROM ListBuy ')
    produtos = db.fetchall()

    if not produtos:
        cores("\nA lista contém nenhum produto!!\n", 'vermelho')
    else:
        ListProducts(False)
        while True:
            id = validacao("\nId do Produto: ", 'int')
            if validaId(id):
                tab('Edição', ["Nome do produto", "Preço do produto", "Quantidade do produto"])
                modoEdic = validacao(">> ", 'int')

                # Query para guarda as informações antes do update
                db.execute(f'SELECT nomeProduto,precoProduto,quantidadeProdutos FROM ListBuy Where id = {id}')
                produtoshis = db.fetchall()
                produtohis = produtoshis[0]

                match modoEdic:
                    case 1:
                        produtoNome = validacao("Digite o nome do produto:  ", 'string')

                        # Salvando para o histórico
                        Mensagem = f"Modificação {produtohis[0]}: {produtohis[0]} | {produtoNome}"
                        db.execute(
                            f"INSERT INTO HistoricBuys (historic, data) VALUES ('{Mensagem}',"
                            f"datetime('now','-3 hours'))")

                        db.execute('''
                                            UPDATE ListBuy 
                                            SET 
                                                nomeProduto = ?
                                            WHERE id = ?
                                            ''', (produtoNome, id))

                        # Salvando as alterações no database
                        conexao.commit()
                        cores("\nNome alterado\n", 'verde')
                        break

                    case 2:

                        produtoPreco = validacao("Digite o preço do produto:  ", 'float')

                        # Salvando para o histórico
                        Mensagem = f"Modificação {produtohis[0]}: R$ {produtohis[1]:.2f} | R$ {produtoPreco:.2f}"
                        db.execute(
                            f"INSERT INTO HistoricBuys (historic, data) VALUES ('{Mensagem}',"
                            f"datetime('now','-3 hours'))")

                        db.execute(f'''
                                            UPDATE ListBuy 
                                            SET 
                                                precoProduto = ?
                                            WHERE id = ?
                                            ''', (produtoPreco, id))

                        # Salvando as alterações no database
                        conexao.commit()
                        cores("\nPreço alterado\n", 'verde')
                        break

                    case 3:
                        produtoQTS = validacao("Digite a quantidade do produto:  ", 'int')

                        # Salvando para o histórico
                        Mensagem = f"Modificação {produtohis[0]}: {produtohis[2]} unidades | {produtoQTS} unidades"
                        db.execute(
                            f"INSERT INTO HistoricBuys (historic, data) VALUES ('{Mensagem}',"
                            f"datetime('now','-3 hours'))")

                        db.execute(f'''
                                                    UPDATE ListBuy 
                                                    SET 
                                                        quantidadeProdutos = ?
                                                    WHERE id = ?
                                                    ''', (produtoQTS, id))

                        # Salvando as alterações no database
                        conexao.commit()
                        cores("\nUnidades alteradas\n", 'verde')
                        break
                    case _:
                        cores("\nOpção Inválida\n", 'vermelho')


            else:
                cores("\nId inválido\n", 'vermelho')


# Função para retornar todos os produtos da tabela
def ListProducts(rodape=True):
    db.execute('SELECT * FROM ListBuy ')
    produtos = db.fetchall()
    if not produtos:
        cores("\nA lista contém nenhum produto!!\n", 'vermelho')

    else:
        precoAcumulado = 0
        totalUnidade = 0
        precoTotal = 0

        cores("ID    PRODUTO           PREÇO       UNIDADES", 'bold')
        for produto in produtos:
            preco = f'{produto[2]:.2f}'
            cores(f"{produto[0]:<6}{produto[1]:<15}R$ {preco:<12}{produto[3]:^8}", 'underline')
            totalUnidade += produto[3]
            precoAcumulado += produto[2]
            precoTotal = precoTotal + (produto[2] * produto[3])

        if rodape:
            cores(f"\nPreço Acumulado: R$ {precoAcumulado:.2f}", 'bold')
            cores(f"Unidades Acumuladas: {totalUnidade}", 'bold')
            cores(f"Preço Total: R$ {precoTotal:.2f}", 'bold')

            while True:
                tab('Opções', ["Pesquisa um produto específico", "Retornar para o Menu"])
                option = validacao(">> ", 'int')
                match option:
                    case 1:
                        id = validacao("Digite o ID do produto: ", 'int')
                        ListOneProduct(id)
                    case 2:
                        break
                    case _:
                        cores("\nEssa opção não existe!\n", 'vermelho')


# Função que retornar um produto com base no ID
def ListOneProduct(id):
    if validaId(id):
        db.execute(f'SELECT * FROM ListBuy Where id = {id}')
        produtos = db.fetchall()
        precoTotal = 0
        # Exibe os resultados
        cores("PRODUTO           PREÇO       UNIDADES", 'bold')
        for produto in produtos:
            preco = f"{produto[2]:.2f}"
            cores(f"{produto[1]:<15}R$ {preco:<12}{produto[3]:^8}", 'underline')

            precoTotal = precoTotal + (produto[2] * produto[3])

        cores(f"\nPreço Total: R${precoTotal:.2f}", 'bold')
    else:
        cores("\nID inválido\n", 'vermelho')


# Função que remove o produto pelo ID
def RemoveProducts():
    db.execute('SELECT * FROM ListBuy ')
    produto = db.fetchall()
    if not produto:
        cores("\nA lista contém nenhum produto!!\n", 'vermelho')

    else:
        ListProducts(False)
        while True:
            id = validacao("\nID do produto: ", 'int')

            db.execute(f'SELECT nomeProduto FROM ListBuy WHERE id = {id}')
            produtos = db.fetchall()

            if validaId(id):

                # Salvando para o histórico
                db.execute(
                    f"INSERT INTO HistoricBuys (historic, data) VALUES ('Remoção: {produtos[0][0]}',"
                    f"datetime('now','-3 hours'))")

                db.execute(f"DELETE FROM ListBuy WHERE id = {id}")

                # Salvando as alterações no database
                conexao.commit()
                cores('\nProduto Removido!\n', 'vermelho')
                break
            else:
                cores("\nId inválido\n", "vermelho")


# Função que verifica se o ID existe na tabela
def validaId(id: int):
    db.execute(f'SELECT id FROM ListBuy ')
    produtos = db.fetchall()
    for produto in produtos:
        if produto[0] == id:
            return True


# Função que retorna o historico das ações
def HistoricProducts():
    db.execute(f"SELECT historic, strftime('%H:%M %d/%m/%Y', data) FROM HistoricBuys ")
    produtos = db.fetchall()

    print()
    for produto in produtos:
        match produto[0][:3]:
            case 'Adi':
                date = f"{produto[1][:5]} de {produto[1][6:]}"
                cores(f"- {produto[0]}    [{date}]", 'verde')
            case 'Rem':
                date = f"{produto[1][:5]} de {produto[1][6:]}"
                cores(f"- {produto[0]}    [{date}]", 'vermelho')
            case 'Mod':
                date = f"{produto[1][:5]} de {produto[1][6:]}"
                cores(f"- {produto[0]}    [{date}]", 'amarelo')
    print()
