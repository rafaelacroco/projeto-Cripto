# Crie uma agenda de telefones que salva os dados de maneira
# permanente.
# A agenda deve funcionar em loop infinito, até que o usuário
# decida sair. Os dados armazenados são: nome, sobrenome,
# telefone e e-mail.
# A agenda deve apresentar o seguinte menu para o usuário:
# ▶ 1- Novo contato (create)
# ▶ 2- Procura (pelo nome) (read)
# ▶ 3- Atualiza contato (update)
# ▶ 4- Apaga 

import os

contatos = []
nome_arquivo = "contatos.txt"
def carregarContatos():
    if not os.path.exists(nome_arquivo):
        return
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            nome, sobrenome, telefone, email = linha.strip().split(";")
            contatos.append({"nome":nome, "sobrenome":sobrenome, "telefone":telefone, "email":email})

def salvarContatos():
    with open(nome_arquivo, "w") as arquivo:
        for c in contatos:
            arquivo.write(f"{c['nome']};{c['sobrenome']};{c['telefone']}; {c['email']}")
    return

def novoContato():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite e-mail: ")

    novo = {"nome":nome, "sobrenome":sobrenome,
            "telefone":telefone, "email":email}

    print("Contato criado com sucesso!")
    contatos.append(novo)

def exibeContato(contato):
    print(f"Nome: {contato["nome"]}\nSobrenome: {contato["sobrenome"]}")
    print(f"Telefone: {contato["telefone"]}\nEmail: {contato["email"]}")

def buscarContato():
    nome = input("Digite o nome a ser buscado: ")
    for i in range(len(contatos)):
        if contatos[i].get("nome") == nome:
            exibeContato(contatos[i])

def exibeMenu():
    print("1 - Novo contato")
    print("2 - Buscar contato (nome)")
    print("3 - Atualizar contato")
    print("4 - Apagar contato")
    print("0 - Sair")

def processaMenu(menu):
    if menu == 1:
        novoContato()
        print(contatos)
        return True
    elif menu == 2:
        buscarContato()
        return True
    elif menu == 3:
        atualizarContato()
        return True
    elif menu == 4:
        apagarContato()
        #contatos.remove()
        return True
    elif menu == 0:
        return False
    return False #significa ou qualquer outra coisa apresentada que seja diferente das infos acima.

carregarContatos()

while True:
    exibeMenu()
    menu = int(input())
    if(not processaMenu(menu)):
       break
salvarContatos()