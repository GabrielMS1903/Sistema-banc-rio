#separar funçoes existentes de saque, deposito e extrato em funções
#cadastrar usuario(cliente) e cadastrar conta bancária.

#função de saque, depositar e visualizar histórico
#e criar user e criar conta corrente


menu = """Selecione o que você deseja fazer:
        [C] Cadastrar
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
cpfs_cadastrados = set()
lista = []

def completar(nome, cpf, conta, agencia):    
    def nomear(nome): 
        cadastro = input("Seu nome")
        result = nome + cadastro
        
        return result
    
    def cadastrar(cpf):
        fisico = input("Seu cpf, por gentileza")
        digitos = cpf + fisico

        cpfs_cadastrados.add(digitos)
        if digitos in cpfs_cadastrados:
            print("Esse CPF já esta cadastrado, reinicie o programa")
        else:
            print("Cpf cadastrado com sucesso")
        return digitos
    
    def contar(conta, agencia):
        banco = input("Sua agência") 
        if banco.startswith("01"):

            sistema =  conta + banco
            numero_conta = input("Número da sua conta")
            agencia_numerada = agencia + numero_conta
            lista.add(sistema)
        else:
            print("O número da agência deve começar com 01")


        
        return sistema, agencia_numerada
    
    result = nomear(nome)
    digitos = cadastrar(cpf)
    sistema, agencia_numerada = contar(conta, agencia)
    
    return result, digitos, sistema, agencia_numerada

def sacar(*,exceder_limite, exceder_saldo,exceder_saques ):
    global numero_saques
    global saldo
    global limite
    global extrato

    valor = float(input("Informe o valor do saque: "))

    limitar_l = exceder_limite 
    limitar_sal = exceder_saldo
    limitar_saq = exceder_saques

    limitar_l = valor >limite
    limitar_sal = valor > saldo
    limitar_saq = numero_saques >= limite_saques
    #exceder_limite = valor > limite
    
    if limitar_sal:
        print("Operação falhou! Valor do saldo insuficiente")

    elif limitar_l:
        print("Operação falhou! Limites máximos atingidos")

    elif limitar_saq:
        print("Operação falhou! Número de saques excedidos")
        
    elif valor > 0:
            #saldo - valor
        saldo -= valor
        extrato +=  f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

def depositar(cair, /):
    global saldo
    global extrato
    valor = float(input("Informe o valor do depósito: "))
    
    

    if valor > 0:
        saldo += valor
        extrato += f"{valor:.2f}\n"
           
    else:
        print("Operação falhou! O depósito informado não é válido.")

def historico(folha):
    info = folha + extrato
    
    print(" ================ EXTRATO ==============")
    if info: 
        print(info)
    else:
        print("Nenhuma movimentação")
    print(f"Olá, {result}, você tem R$ {saldo:.2f} de saldo na conta {agencia_numerada}.")
    print("=========================================")      

ativo = True

while ativo:

    opcao = input(menu)
    if opcao == "D":
        valor = saldo  
        depositar(valor)

    elif opcao == "S":
        sacar(exceder_limite= "", exceder_saldo= "", exceder_saques="")
       
       
    elif opcao == "E":
       historico(folha= extrato)

    elif opcao == "C":
        nome = ""
        cpf = ""
        conta = ""
        agencia = ""
        result, digitos, sistema, agencia_numerada = completar(nome, cpf, conta, agencia)
        

        print(f"Nome cadastrado: {result}")
        print(f"CPF cadastrado: {digitos}")
        print(f"Conta cadastrada: {sistema}")
        print(f"Conta cadastrada: {agencia_numerada}")

    elif opcao == "X":
        break

    else:
        print("Inválido, vamos retornar as opções.")