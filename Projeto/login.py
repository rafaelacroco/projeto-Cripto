# Você estava mexendo em comprar criptomoedas (Falta armazenar elas e realizar mais testes) e tem que criar arquivos para armazenar todas as informações, tem que arrumar o  consultar saldo
import os 
import random

armazenamento_conta = "conta.txt"
conta = []

# ACESSO 1 - para  entrar na conta:

#Mostra o que você pode acessar
def acessar():
    print("1 - Acessar minha conta")
    print("2 - Criar conta")
    print("0 - Sair")
def processe_acessar(acesso):
    if acesso == 1:
        acessar_conta()
        return True
    elif acesso == 2:
        criar_conta()
        return True
    elif acesso == 0:
        return False
    return False

#criei para quando o cliente já possue uma conta, bloqueia a opção de criar conta
def conta_existente():
    print("1 - Acessar minha conta")
    print("0 - Sair")
    escolha = int(input("Digite uma das opções: "))
    processe_conta_existente(escolha)
    return
def processe_conta_existente(escolha):
    if escolha == 1:
        acessar_conta()
        return True
    elif escolha == 0:
        return False
    return False

def criar_conta():
    if os.path.exists(armazenamento_conta):
        print("[ERRO] Esse aparelho já possui uma conta cadastrada!")
        conta_existente()
        return 
    
    print("\n Realize seu cadastro: \n")
    nome = str(input("Digite seu nome: "))
    #Condições do CPF
    while True:
        cpf = input("Digite seu CPF: ")
        #cpf não pode ter ponto e traço
        if "." in cpf or "-" in cpf:
            print(" O CPF não deve possuir pontos ou traços digitados!")
        elif not cpf.isdigit():
            print("O CPF deve ser composto apenas por números!")
        elif len(cpf) != 11:
            print("O CPF deve obrigatóriamente possuir 11 números!")
        else:
            break
    senha = input("Digite uma senha: ")
    #Dados da conta armazenado:
    with open(armazenamento_conta, "w") as armazenamento:
        armazenamento.write(f"{nome}\n{cpf}\n{senha}")
    print("Sua conta foi criada com sucesso!")

def acessar_conta():
    #se o arquivo não existir
    if not os.path.exists(armazenamento_conta):
        print("Nenhuma conta foi encontrada. \n É necessário criar uma conta antes de poder acessar outras modalidades.")
        return
    #se existir permita o acesso
    print("Acessar Conta: ")
    cpf_acesso = input("Digite seu CPF: ")
    senha_acesso = input("Digite uma senha: ")

    with open(armazenamento_conta, "r") as armazenamento:
        linhas = armazenamento.readlines()
        nome_armazenado = linhas[0].strip()
        cpf_armazenado = linhas[1].strip()
        senha_armazenada = linhas[2].strip()
    if cpf_armazenado == cpf_acesso and senha_acesso == senha_armazenada:
        print(f"Acesso Liberado! \n Seja Bem-vindo {nome_armazenado}")
        #criado para que o 'acessar()' parasse de aparecer junto ao 'exibe_acessos()'
        while True:
            exibe_acessos()
            acessos = int(input("Digite uma das opções: "))
            if not processar_acessos(acessos):
                print("Saindos...")
                break
    else:
        print("Seu CPF ou sua senha está incorreto! \n Acesso negado ")
        return False

# ACESSOS PARTE 2
def exibe_acessos():
    print("1 - Consultar saldo")
    print("2 - Consultar extrato")
    print("3 - Realizar um depósito")
    print("4 - Realizar um saque")
    print("5 - Comprar Criptomoedas")
    print("6 - Vender Criptomoedas")
    print("7 - Atualizar Cotação")
    print("0 - Sair")

def processar_acessos(acessos):
    if acessos == 1:
        consultar_saldo()
        print()
        return True
    elif acessos == 2:
        consultar_extrato()
        print()
        return True
    elif acessos == 3:
        depositar()
        print()
        return True
    elif acessos == 4:
        sacar()
        print()
        return True
    elif acessos == 5:
        comprar_cripto()
        print()
        return True
    elif acessos == 6:
        vender_cripto()
        print()
        return True
    elif acessos == 7:
        atualizar_cotacao()
        print()
        return True
    elif acessos == 0:
        return False
    return False

#Subfunções de ACESSO 2
def verifica_senha():  
    print("Para Acessar é preciso que você digite sua senha.\n")
    with open(armazenamento_conta, "r") as armazenamento:
        linhas = armazenamento.readlines()
        senha_armazenada = linhas[2].strip()

    senha_acessos = input("Digite sua senha: ")
    if senha_acessos == senha_armazenada:
        print("\nSeu acesso foi liberado!")
        return True        
    while senha_acessos != senha_armazenada:
        senha_acessos2 = input("Digite sua senha: ")
        print("Sua senha está errada!")
        with open(armazenamento_conta, "r") as armazenamento:
            linhas = armazenamento.readlines()
            senha_armazenada = linhas[2].strip()
        if senha_acessos2 == senha_armazenada:
                print("\nSeu acesso foi liberado!")
                return True       
            
#valor inicial
bitcoin = 420920.00
ethereum = 3600.27
ripple = 722.09
saldo_atual = 0
saldo_bitcon = 0
saldo_ethereum = 0
saldo_ripple = 0

#Faz parte das funções de saque, depósito, consultar saldo e consultar extrato
def verifica_saldo(inserir_reais, sacar_reais):
    saldo_atualizado = 0
    global saldo_atual
    saldo_atual = saldo_atual + inserir_reais
    saldo_atual = saldo_atual - sacar_reais
    if saldo_atual >= saldo_atualizado or saldo_atual <= saldo_atualizado:
        saldo_atualizado = saldo_atual
    return
#parte de vendas e compras de criptomoedas
def tipos_criptomoedas():
    print("1 - Bitcoin")
    print("2 - Ethereum")
    print("3 - Ripple")
    print("0 - Sair")

# acesso 2 depois de acessar conta

def consultar_saldo():
    verifica_senha()
    with open(armazenamento_conta, "r") as armazenamento: 
        linhas = armazenamento.readlines()
        nome_armazenado = linhas[0].strip()
        cpf_armazenado = linhas[1].strip()
        verifica_saldo()
    print(f"Nome: {nome_armazenado} \n CPF: {cpf_armazenado} \n Reais: {saldo_atual}")
    return

def consultar_extrato():
    return

def depositar():
    print("Acesso ao grid de depósito")
    verifica_senha()
    global saldo_atual
    inserir_reais = float(input("Digite o valor que deseja depositar: "))
    #mostrar saldo atual
    verifica_saldo(inserir_reais, 0) 
    return

def sacar():
    print("Acesso ao grid de saque")
    verifica_senha()
    global saldo_atual
    sacar_reais = float(input("Digite o valor que deseja sacar: "))
    if sacar_reais > saldo_atual:
        print("O saldo atual é menor que o valor a ser resgatado.")
    else:
        #mostra saldo atual
        verifica_saldo(0, sacar_reais)
    return

def comprar_cripto():
    atualizar_cotacao()
    tipos_criptomoedas()
    criptomoedas = int(input("Escolha uma das criptomoedas:"))
    if criptomoedas == 1:
        print("Você escolheu comprar Bitcoin!")
        print(f"A cotação do Bitcoin é de {bitcoin}")
        taxa = bitcoin + (bitcoin * 0.02)
        print(f"A taxa de compra é de 2%. \nO valor do Bitcoin é {taxa} ")
        valor_comprar = float(input("Digite o valor que deseja investir para comprar: "))
        if valor_comprar > saldo_atual:
            print("Saldo insuficiente!") 
        elif valor_comprar < saldo_atual:
            comprado = valor_comprar / taxa
            print(f"Você comprou {comprado} de Bitcoin")
        else:
            print("Algo deu errado!\nTente novamente.")
            return False
    elif criptomoedas == 2:
        print("Você escolheu comprar Ethereum!")
        print(f"A cotação do Ethereum é de {ethereum}")
        taxa = ethereum + (ethereum * 0.01)
        print(f"A taxa de compra é de 1%. \nO valor do Ethereum é {taxa} ")            
        valor_comprar = float(input("Digite o valor que deseja investir para comprar: "))
        if valor_comprar > saldo_atual:
            print("Saldo insuficiente!") 
        elif valor_comprar < saldo_atual:
            comprado = valor_comprar / taxa
            print(f"Você comprou {comprado} de Ethereum")
        else:
            print("Algo deu errado!\nTente novamente.")
            return False
    elif criptomoedas == 3:
            print("Você escolheu comprar Ripple!")
            print(f"A cotação do Ripple é de {ripple}")
            taxa = ripple + (ripple * 0.01)
            print(f"A taxa de compra é de 1%. \nO valor do Ripple é {taxa} ")
            valor_comprar = float(input("Digite o valor que deseja investir para comprar: "))
            if valor_comprar > saldo_atual:
                print("Saldo insuficiente!") 
            elif valor_comprar < saldo_atual:
                comprado = valor_comprar / taxa
                print(f"Você comprou {comprado} de Ripple")
            else:
                print("Algo deu errado!\nTente novamente.")
                return False
    elif criptomoedas == 0:
        print("Saindo...")
        return False
    return False

def vender_cripto():
    return
def atualizar_cotacao():
    global bitcoin, ripple, ethereum
    print("Atualização de cotação das criptomoedas: \n")
    variaçao = random.uniform(-0.05, 0.05)
    bitcoin = bitcoin + (bitcoin * variaçao)
    ethereum = ethereum + (ethereum * variaçao)
    ripple = ripple + (ripple * variaçao)
    porcentagem = variaçao * 100
    print(f"A variação foi de {porcentagem:.2f}\n")
    print(f"Bitcoin: {bitcoin:.2f} \nEthereum: {ethereum:.2f}\nRipple: {ripple:.2f}")
    return bitcoin, ethereum, ripple

while True:
    acessar()
    acesso = int(input("Digite o número sobre qual área você deseja acessar: \n"))
    if(not processe_acessar(acesso)):
        break

