menu = """Selecione o que você deseja fazer:

        [D] Depositar
        [S] Sacar
        [E] Extrato
        [X] Sair

"""
#print(menu)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

ativo = True

while ativo:

    opcao = input(menu)
    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"{valor:.2f}\n"
           
        else:
            print("Operação falhou! O depósito informado não é válido.")
        
    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        exceder_limite = valor > limite
        exceder_saldo = valor > saldo
        exceder_saques = numero_saques >= limite_saques

        if exceder_saldo:
            print("Operação falhou! Valor do saldo insuficiente")

        elif exceder_limite:
            print("Operação falhou! Limites máximos atingidos")

        elif exceder_saques:
            print("Operação falhou! Número de saques excedidos")
        
        elif valor > 0:
            #saldo - valor
            saldo -= valor
            extrato +=  f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    elif opcao == "E":
        print(" ================ EXTRATO ==============")
        if extrato: 
            print(extrato)
        else:
            print("Nenhuma movimentação")
        print(f"\m Saldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "X":
        break

    else:
        print("Inválido, vamos retornar as opções.")