menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(saldo, extrato, valor_deposito):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")
        print(f"Saldo atual: R${saldo:.2f}")
    
    else: 
        print("Operação falhou! Tente novamente")

    return saldo, extrato
        

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        print("DEPÓSITO:")
        valor_deposito = float(input("Valor do depósito: "))
        saldo, extrato = deposito(saldo=saldo, extrato=extrato, valor_deposito=valor_deposito)
    
    elif opcao.lower() == "s":
        print("Saque")
    
    elif opcao.lower() == "e":
        print("Extrato")

    elif opcao.lower() == "q":
        print("Saindo...")
        break

    else:
        print("Operação invália. Selecione novamente")
