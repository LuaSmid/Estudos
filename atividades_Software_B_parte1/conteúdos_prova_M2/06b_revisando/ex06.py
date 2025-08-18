'''6. Cadastro de Novo Usuário 
Crie uma função `cadastrar_usuario(lista, novo_usuario, nova_senha)` que 
adicione um novo dicionário à lista de usuários, desde que o nome de usuário 
ainda não exista. Use a estrutura do exercício 5. '''

usuarios = [
    ['luana', '12345'],
    ['pedro', '54321'],
    ['julia', '23456']
]

def cadastrar_usuario(usuarios, novo_usuario, nova_senha):
    for u, s in usuarios:
        if novo_usuario == u:
            return "Usuário já está na lista!"
        else:
            usuarios.append((novo_usuario, nova_senha))
            return "Usuário cadastrado com sucesso!"

novo_usuario = input("Nome do novo usuário: ")
nova_senha = input("Informe uma senha para esse usuário: ")

print(cadastrar_usuario(usuarios, novo_usuario, nova_senha))
print(usuarios)



