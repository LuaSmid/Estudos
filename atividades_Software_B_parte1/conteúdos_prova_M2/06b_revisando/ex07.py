'''7. Atualizar Senha 
Crie uma função `atualizar_senha(lista, usuario, nova_senha)` que atualize a 
senha de um usuário existente. Se o usuário não for encontrado, a função deve 
informar isso. Use a estrutura do exercício 5.'''

usuarios = [
    ('luana', '12345'),
    ('pedro', '54321'),
    ('julia', '23456')
]

def atualizar_senha(usuarios, usuario, nova_senha):
    for i, (u, s) in enumerate(usuarios):
        if usuario == u:
            usuarios[i] = (u, nova_senha)
            return "Senha alterada!"
    return "Usuário não encontrado!"

usuario = input("Usuário: ")
nova_senha = input("Senha nova: ")
print(atualizar_senha(usuarios, usuario, nova_senha))
print(usuarios)
