import sqlite3

conexao = sqlite3.connect("./Database/database.db")

db = conexao.cursor()

# Tabela do arquivo FunctionsTasks
db.execute('''
        CREATE TABLE IF NOT EXISTS Tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeTarefa TEXT,
        situacao TEXT,
        descricao TEXT
        )
        ''')
db.execute('''
        CREATE TABLE IF NOT EXISTS HistoricTasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        historic TEXT,
        data DateTime
        )
        ''')

# Tabela do arquivo FunctionsBuys
db.execute('''
        CREATE TABLE IF NOT EXISTS ListBuy (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeProduto TEXT,
        precoProduto DECIMAL(10,2) DEFAULT 0.00,
        quantidadeProdutos INT
        )
        ''')

db.execute('''
        CREATE TABLE IF NOT EXISTS HistoricBuys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        historic TEXT,
        data DateTime
        )
        ''')

# Tabelas do arquivo FunctionsWallet
db.execute('''
        CREATE TABLE IF NOT EXISTS Money (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        extrato FLOAT DEFAULT 0.00,
        data DateTime
        )
        ''')

db.execute('''
        CREATE TABLE IF NOT EXISTS TotalMoney (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        totalMoney FLOAT DEFAULT 0.00
        )
        ''')
