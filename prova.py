""" Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop."""


email_cadastro = 'exemplo@gmail.com'
senha_cadastro = 'in12345678'

while True:
 email = (input('digite o email: ')).lower().strip()
 senha = (input('digite a senha: ')).strip()
 if email_cadastro == email and senha_cadastro == senha:
  break
 else:
  print('email e/ou senha incorreto(s)!!')

print('Semha e email valido!!!!')