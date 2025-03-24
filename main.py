from datetime import datetime

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



clientes = {}
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def cadastrar_cliente(clientes):

    print("Cadastrar Cliente:")
    nome_cliente = input("Nome do cliente: ")

    while True:
        try:
            data_nasc_cliente = input("Data de nascimento (DD/MM/AAAA): ")
            data_nasc_cliente = datetime.strptime(data_nasc_cliente, "%d/%m/%Y").date()
            break 
        except ValueError:
            print("Formato inválido! Digite a data no formato correto (DD/MM/AAAA).")

    while True:        
        cpf_cliente = int(input("Insira seu CPF (Apenas Números) "))
        if len(str(cpf_cliente)) == 11:
            if cpf_cliente in clientes:
                print("CPF já cadastrado! Tente novamente.")
            else:
                break
        else:
            print("CPF inválido! Digite apenas números com 11 dígitos.")

    print("\n Informações de Endereço: ")
    rua_cliente = input("Rua: ")
    numero_cliente = int(input("Número: "))
    bairro_cliente = input("Bairro: ")
    cidade_cliente = input("Cidade: ")
    while True:
        estado_cliente = input("Sigla do Estado: ")
        if len(estado_cliente) == 2:
            break
        else:
            print("Valor inválido, apenas siglas são permitidas")

    clientes[cpf_cliente] = {
        "nome_cliente": nome_cliente,
        "data_nasc_cliente": data_nasc_cliente,
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0,
        "endereco_cliente": {
            "rua_cliente": rua_cliente,
            "numero_cliente": numero_cliente,
            "bairro_cliente": bairro_cliente,
            "cidade_cliente": cidade_cliente,
            "estado_cliente": estado_cliente,
        }
    }

    print(f"\n Cliente {nome_cliente} cadastrado com sucesso!")


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
        cadastrar_cliente(clientes= clientes)

    elif escolha_inicio == "0":
        print("Cancelando...")
        break

    else:
        print("Valor Inválido!")
