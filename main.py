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
        },
        "conta_corrente": {
            "possui_conta_corrente": False,
            "numero_conta_corrente": None,
            "agencia": ""
        }
    }

    print(f"\n Cliente {nome_cliente} cadastrado com sucesso!")

    return clientes

def login(clientes):

    while True:
        verifica_cpf = int(input("Insira o seu CPF (Apenas números): "))
        if len(str(verifica_cpf)) == 11:
                if verifica_cpf in clientes:
                    nome_cliente = clientes[verifica_cpf]["nome_cliente"]
                    print(f"Seja bem vindo {nome_cliente}")
                    
                    verifica_conta_corrente(clientes= clientes, cpf_cliente= verifica_cpf)
                    exibe_menu_cliente(clientes= clientes)
                    return verifica_cpf
                else:
                    print("CPF não encontrado! Tente novamente ou cadastre-se")
                    break
        else:
                print("CPF inválido! Digite apenas números com 11 dígitos.")

def gerar_numero_conta(clientes):
    """Gera o próximo número de conta baseado no maior número existente."""
    numeros_contas = [
        dados["conta_corrente"]["numero_conta_corrente"]
        for dados in clientes.values()
        if dados["conta_corrente"]["numero_conta_corrente"] is not None
    ]
    
    return max(numeros_contas, default=0) + 1  # Se não houver contas, começa em 1000



def verifica_conta_corrente(clientes, cpf_cliente):

    status_conta_corrente = clientes[cpf_cliente]["conta_corrente"]["possui_conta_corrente"]

    if not status_conta_corrente:
        print("Você ainda não criou sua conta corrente! Deseja criar agora? ")
        escolha = input("""

            [s] Sim
            [n] Não
        
        
        """)

        if escolha.lower() == "s":

            clientes[cpf_cliente]["conta_corrente"]["possui_conta_corrente"] = True
            numero_nova_conta = gerar_numero_conta(clientes)
            clientes[cpf_cliente]["conta_corrente"]["numero_conta_corrente"] = numero_nova_conta
            clientes[cpf_cliente]["conta_corrente"]["agencia"] = "001"

            print(f"Conta corrente criada com sucesso!\nNúmero da conta: {numero_nova_conta}, Agência: 001")


        else:
            print(menu)




def exibe_menu_cliente(clientes):
 while True:

            opcao = input(menu)

            if opcao.lower() == "d":
                print("DEPÓSITO:")
                valor_deposito = float(input("Valor do depósito: "))
                saldo, extrato = deposito(clientes)
            
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

    excedeu_limite = valor_saque > LIMITE_SAQUES

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
        login(clientes= clientes)


    elif escolha_inicio == "2":
        cadastrar_cliente(clientes= clientes)

    elif escolha_inicio == "0":
        print("Cancelando...")
        break

    else:
        print("Valor Inválido!")
