from Functions import *
from Database import *

# Função para adicionar um produto no database
def addTarefa():
    condicao = True
    while condicao:
        nome = validacao("Digite o nome da tarefa: ", 'string')

        db.execute(
            f"INSERT INTO HistoricTasks (historic, data) VALUES ('Adição : {nome}', datetime('now','-3 "
            f"hours'))")

        while True:
            des = validacao("Quer Adicionar alguma descrição a tarefa?[SIM|Não] ", 'string')

            match des[0].lower():
                case 's':
                    # Adiciona tarefa com descrição
                    descricao = validacao("Descrição : ", 'string')
                    db.execute(
                        f"INSERT INTO Tasks (nomeTarefa, situacao, descricao) VALUES ('{nome}', 'Pendente', '{descricao}')")

                    # Salvando os dados no database
                    conexao.commit()
                    break
                case 'n':
                    # Adiciona tarefa sem descrição
                    db.execute(
                        f"INSERT INTO Tasks (nomeTarefa, situacao, descricao) VALUES ('{nome}', 'Pendente', '')")

                    # Salvando os dados no database
                    conexao.commit()
                    break
                case _:
                    cores("Opção inválida", 'vermelho')
        cores("Tarefa adicionada com sucesso", 'verde')
        while True:
            op = validacao("Quer adicionar outra tarefa?[Sim|Não] ", 'string')
            match op[0].lower():
                case 's':
                    break
                case 'n':
                    condicao = False
                    break
                case _:
                    cores("\nOpção inválida\n", 'vermelho')


# Função para editar uma tarefa no database
def updateTarefa():
    db.execute('SELECT * FROM Tasks ')
    tasks = db.fetchall()
    if not tasks:
        cores("\nA lista contém nenhum produto!!\n", 'vermelho')

    else:
        ListAllTasks(False)
        while True:
            id = validacao("Digite o Id da tarefa: ", 'int')
            if validaId(id):
                tab('Edição', ["Alterar nome", "Tarefa concluída", "Alterar a descrição"])
                modoEdic = validacao(">> ", 'int')

                # Query para guarda as informações antes do update
                db.execute(f'SELECT nomeTarefa,situacao,descricao FROM Tasks Where id = {id}')
                tasks = db.fetchall()
                task = tasks[0]

                match modoEdic:
                    case 1:
                        tarefa = validacao("Renomeie a tarefa: ", 'string')

                        # Salvando para o histórico
                        Mensagem = f"Modificação {task[0]}: {task[0]} | {tarefa}"
                        db.execute(
                            f"INSERT INTO HistoricTasks (historic, data) VALUES ('{Mensagem}',"
                            f"datetime('now','-3 hours'))")

                        db.execute('''
                                    UPDATE Tasks 
                                    SET 
                                        nomeTarefa = ?
                                    WHERE id = ?
                                    ''', (tarefa, id))

                        # Salvando as alterações no database
                        conexao.commit()
                        cores("\nNome alterado\n", 'verde')
                        break
                    case 2:

                        # Salvando para o histórico
                        Mensagem = f"Modificação {task[0]}: {task[1]} | Concluída"
                        db.execute(
                            f"INSERT INTO HistoricTasks (historic, data) VALUES ('{Mensagem}',"
                            f"datetime('now','-3 hours'))")

                        db.execute(f'''
                                    UPDATE Tasks 
                                    SET 
                                        situacao = 'Concluída'
                                    WHERE id = {id}
                                    ''')

                        # Salvando as alterações no database
                        conexao.commit()
                        cores("\nSituação alterada\n", 'verde')
                        break
                    case 3:
                        descricao = validacao("Descrição: ", 'string')

                        # Salvando para o histórico
                        Mensagem = f"Modificação {task[0]}: {task[2][:10]}... | {descricao[:10]}..."
                        db.execute(
                            f"INSERT INTO HistoricTasks (historic, data) VALUES ('{Mensagem}',"
                            f"datetime('now','-3 hours'))")

                        db.execute(f'''
                                     UPDATE Tasks 
                                     SET 
                                        descricao = ?
                                     WHERE id = ?
                                    ''', (descricao, id))

                        # Salvando as alterações no database
                        conexao.commit()
                        cores("\nDescrição alterada\n", 'verde')
                        break

                    case _:
                        cores("\nOpção Inválida\n", 'vermelho')

            else:
                cores("\nID Inválido\n", 'vermelho')


# Função para retornar todos as tarefas da tabela
def ListAllTasks(rodape=True):
    db.execute('SELECT * FROM Tasks ')
    tasks = db.fetchall()

    if not tasks:
        cores("\nA lista contém nenhum produto!!\n", 'vermelho')

    else:
        concluida = 0
        pendente = 0
        cores("ID     TAREFAS                  SITUAÇÃO", 'bold', )

        for task in tasks:

            if task[2].lower() == 'pendente':
                pendente += 1
                corpendente = cores(f'{task[2]}', 'amarelo', False)
                cores(f"{task[0]:<7}{task[1]:<25}{corpendente:<13}", 'underline')

            else:
                concluida += 1
                corpendente = cores(f'{task[2]}', 'verde', False)
                cores(f"{task[0]:<7}{task[1]:<25}{corpendente:<13}", 'underline')

        if rodape:
            print(f"\n{cores(f'Tarefas concluídas: {concluida}', 'verde', False)} "
                  f"| {cores(f'Tarefas pendentes: {pendente}', 'amarelo', False)}")

            while True:
                tab('Opções', ["Pesquisa uma tarefa específica", "Retornar para o Menu"])
                option = validacao(">> ", 'int')

                match option:
                    case 1:
                        id = validacao("Digite o ID da tarefa: ", 'int')
                        ListOneTask(id)

                    case 2:
                        break

                    case _:
                        cores("\nEssa opção não existe!\n", 'vermelho')

        else:
            return tasks


# Função que retornar uma tarefa com base no ID
def ListOneTask(id: int):
    if validaId(id):
        db.execute(f'SELECT * FROM Tasks WHERE id = {id}', )
        tasks = db.fetchall()

        cores("ID     TAREFAS                  SITUAÇÃO", 'bold')
        for task in tasks:
            if task[2].lower() == 'pendente':
                corpendente = cores(f'{task[2]}', 'amarelo', False)
                cores(f"{task[0]:<7}{task[1]:<25}{corpendente:<13}", 'underline')

                print(f"\nDescrição: ")

                # Quebra de linha para a descrição
                cont = 0
                for va in task[3]:
                    if cont < 60:
                        print(va, end='')
                        cont += 1
                    else:
                        print()
                        print(va, end='')
                        cont = 1
                print("\n")

            else:
                corpendente = cores(f'{task[2]}', 'verde', False)
                cores(f"{task[0]:<7}{task[1]:<25}{corpendente:<13}", 'underline')
                print(f"\nDescrição: {task[3]}")

    else:
        cores("\nID inválido\n", 'vermelho')

# Função que remove a tarefa pelo ID
def RemoveTarefas():
    db.execute('SELECT * FROM Tasks ')
    tasks = db.fetchall()
    if not tasks:
        cores("\nA lista contém nenhuma tarefa!!\n", 'vermelho')

    else:
        while True:
            id = validacao("ID da tarefa: ", 'int')

            db.execute(f'SELECT nomeTarefa FROM Tasks WHERE id = {id}')
            tasks = db.fetchall()

            if validaId(id):
                db.execute(
                    f"INSERT INTO HistoricTasks (historic, data) VALUES ('Remoção: {tasks[0][0]}',"
                    f"datetime('now','-3 hours'))")
                db.execute(f"DELETE FROM Tasks WHERE id = {id}")
                conexao.commit()
                cores("\nTarefa Removida\n", 'vermelho')
                break

            else:
                cores("\nId inválido\n", 'vermelho')


# Função que verifica se o ID existe na tabela
def validaId(id: int):
    db.execute(f'SELECT id FROM Tasks ')
    tasks = db.fetchall()
    for task in tasks:
        if task[0] == id:
            return True


# Função que retorna o historico das ações
def HistoricTasks():
    db.execute(f"SELECT historic, strftime('%H:%M %d/%m/%Y', data) FROM HistoricTasks ")
    tasks = db.fetchall()

    print()
    for task in tasks:
        match task[0][:3]:
            case 'Adi':
                date = f"{task[1][:5]} de {task[1][6:]}"
                cores(f"- {task[0]}    [{date}]", 'verde')
            case 'Rem':
                date = f"{task[1][:5]} de {task[1][6:]}"
                cores(f"- {task[0]}    [{date}]", 'vermelho')
            case 'Mod':
                date = f"{task[1][:5]} de {task[1][6:]}"
                cores(f"- {task[0]}    [{date}]", 'amarelo')
    print()
