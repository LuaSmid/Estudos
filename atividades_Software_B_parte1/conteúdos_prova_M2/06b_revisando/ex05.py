'''5. Verificação de Login 
Crie uma função `verificar_login(usuario, senha)` que receba um nome de 
usuário e uma senha, e verifique se eles existem em uma lista de usuários 
cadastrados. '''

usuarios = [
    ['luana', '12345'],
    ['pedro', '54321'],
    ['julia', '23456']
]

def verificar_login(usuario, senha):
    for u, s in usuarios:
        if usuario == u:
            if senha == s:
                return "Usuário cadastrado!"
            else:
                return "Senha incorreta!"
    return "Usuário não cadastrado!"

usuario = input("Usuário: ")
senha = input("Senha: ")
print(verificar_login(usuario, senha))