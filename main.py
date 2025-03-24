inicio = """

    Seja Bem Vindo ao Gerbi Bank!

    [1] Entrar
    [2] Cadastrar
    [0] Cancelar

"""

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
        extrato += f"Depósito: R${valor_deposito:.2f}\n"
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")
        print(f"Saldo atual: R${saldo:.2f}")
    
    else: 
        print("Operação falhou! Tente novamente")

    return saldo, extrato

def saque(saldo, extrato, valor_saque, numero_saques):

    excedeu_saldo = valor_saque > saldo

    excedeu_limite = valor_saque > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_limite:
        print("Saque negado! O valor de saque excede o limite")
    
    elif excedeu_saldo:
        print("Saque negado! O valor de saque é maior que o saldo")
    
    elif excedeu_saques:
        print("Saque negado! Você excedeu o limite de saques diário")

    elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R${valor_saque:.2f}\n"
            print(f"Saque de R${valor_saque:.2f}\n")
            print(f"Saldo atual: R${saldo:.2f}")
            numero_saques += 1

    return numero_saques, saldo, extrato
        

def mostrar_extrato(extrato, saldo):
    msg = "EXTRATO"
    print(msg.center(34, '='))
    if not extrato:
        print("Não foram realizadas movimentações na conta!")
    else:
        print(extrato)
        print(f"\nSaldo: R${saldo:.2f}")


while True:
    escolha_inicio = input(inicio)

    if escolha_inicio == "1":
        print("Login")
        while True:

            opcao = input(menu)

            if opcao.lower() == "d":
                print("DEPÓSITO:")
                valor_deposito = float(input("Valor do depósito: "))
                saldo, extrato = deposito(saldo=saldo, extrato=extrato, valor_deposito=valor_deposito)
            
            elif opcao.lower() == "s":
                print("SAQUE:")
                valor_saque = float(input("Valor do saque: "))
                numero_saques, saldo, extrato = saque(numero_saques=numero_saques, saldo=saldo, extrato=extrato, valor_saque=valor_saque)
            
            elif opcao.lower() == "e":
                print("EXTRATO:")
                mostrar_extrato(extrato=extrato, saldo=saldo)


            elif opcao.lower() == "q":
                print("Saindo...")
                break

            else:
                print("Operação inválida. Selecione novamente")


    elif escolha_inicio == "2":
        print("Cadastrar")

    elif escolha_inicio == "0":
        print("Cancelando...")
        break

    else:
        print("Valor Inválido!")
