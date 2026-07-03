email = 'johndoe@admin.com.br'
password = 'admin123'

email_input = input('Email: ')
password_input = input('Password: ')

if email_input == email and password_input == password:
    print('Seja Bem-Vindo ao sistema, Administrador!')
else:
    print('Acesso bloqueado')