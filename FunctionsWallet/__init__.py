from Database import *
from Functions import *


# Função que retorna o saldo total
def TotalCarteira(val=True):  # Retorna o valor total da carteira para transações
    db.execute("SELECT totalMoney FROM TotalMoney WHERE id = 1")
    moneys = db.fetchall()

    total = 0
    for money in moneys:
        total += money[0]

    if val:
        return total
    else:
        return cores(f"R$ {total:.2f}", 'bold')


# Função que mostra todos os movimentos da conta
def Extrato():
    db.execute("SELECT extrato,strftime('%H:%M %d/%m/%Y', data) FROM Money ")
    moneys = db.fetchall()
    cont = 1
    print()
    for money in moneys:
        extrato = f"{money[0]:.2f}"
        date = f"{money[1][:5]} - {money[1][6:]}"
        if money[0] < 0:
            saque = cores(f'R$ {extrato:<10} [{date}]', 'vermelho', False)
            print(f"{cont}° Saque: {saque}")
            cont += 1
        else:
            deposito = cores(f'R$ {extrato:<10} [{date}]', 'verde', False)
            print(f"{cont}° Depósito: {deposito}")
            cont += 1
    print()

# Função que coloca o valor na conta
def Deposito():
    valor = validacao("R$ ", "float")
    deposito = TotalCarteira() + valor
    db.execute(f"UPDATE TotalMoney SET totalMoney = {deposito} Where id = 1")
    db.execute(f"INSERT INTO Money (extrato, data) VALUES ({valor}, datetime('now','-3 hours')) ")
    conexao.commit()
    cores(f"Depósito realizado", 'verde')


# Função que retira valor da conta
def Saque():
    valor = validacao("R$ ", "float")
    if valor <= TotalCarteira():
        saque = TotalCarteira() - valor
        db.execute(f"UPDATE TotalMoney SET totalMoney = {saque} Where id = 1")
        db.execute(f"INSERT INTO Money (extrato, data) VALUES (-{valor}, datetime('now','-3 hours')) ")
        conexao.commit()
        cores(f"Saque realizado", 'verde')
    else:
        cores("Saldo insuficiente", 'vermelho')


# Função que caso não exista o ID 1, ela cria um com o valor totalMoney R$ 0.00
def CreateuserDefault():
    db.execute("SELECT totalMoney FROM TotalMoney WHERE id = 1")
    user = db.fetchall()
    if not user:
        db.execute(f"INSERT INTO TotalMoney (totalMoney) VALUES (0.00) ")
        conexao.commit()


CreateuserDefault()
