#  Efetuar login
# CPF sem pontos e traços / Senha de 6 dígitos
# if login is true:
# Consultar saldo; Consultar extrato; Depositar; Sacar; Comprar criptomoedas; Vender criptomoedas; Atualizar cotação; Sai
conta = []
# acesso 1
def acessar():
    print("1 - Criar conta")
    print("2 - Acessar minha conta")
    print("0 - Sair")

def processe_acessar(acesso):
    if acesso == 1:
        criar_conta()
        return True
    elif acesso == 2:
        acessar_conta()
        return True
    elif acesso == 0:
        return False
    return False

    
def criar_conta():
    while True:
        nome = str(input("Digite seu nome: "))
        cpf = int(input("Digite seu CPF: "))
        senha = input("Digite uma senha: ")
        if '.'in cpf or '-' in cpf:
            print(" O CPF não deve possuir pontos ou traços digitados, apenas números.")
        else:
            nova_conta = {"nome": nome, "cpf":cpf,"senha":senha}
            print("conta criada com sucesso")
            conta.append(nova_conta)
            break   

def acessar_conta():
    cpf = int(input("Digite seu CPF: "))
    senha = input("Digite uma senha: ")
    for i in range(len(conta)):
        if conta[i].get("cpf") == cpf and conta[i].get("senha") == senha:
            exibe_acessos()
            return True
# acessos
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
        
# acesso 2 depois de acessar conta

def consultar_saldo():
    return
def consultar_extrato():
    return
def depositar():
    return
def sacar():
    return
def comprar_cripto():
    return
def vender_cripto():
    return
def atualizar_cotacao():
    return

while True:
    acessar()
    acesso = int(input("Digite o número sobre qual área você deseja acessar: \n"))
    if(not processe_acessar(acesso)):
        break

