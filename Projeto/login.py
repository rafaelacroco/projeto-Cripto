#  Efetuar login
# CPF sem pontos e traços / Senha de 6 dígitos
# if login is true:
# Consultar saldo; Consultar extrato; Depositar; Sacar; Comprar criptomoedas; Vender criptomoedas; Atualizar cotação; Sai
import os

armazenamento_conta = "conta.txt"
conta = []

# ACESSO 1 - para  entrar na conta:

#Mostra o que você pode acessar
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
    if os.path.exists(armazenamento_conta):
        print("[ERRO] Esse aparelho já possui uma conta cadastrada!")
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
        exibe_acessos()
    else:
        print("Seu CPF ou sua senha está incorreto! \n Acesso negado ")
        return False

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

