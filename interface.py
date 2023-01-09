from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout_login = [
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='§')],
    [sg.Button('Entrar')],[sg.Button('Novo Cadastro')]
]

layout_cadastro = [
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='§')],
    [sg.Text('Confirme a Senha'),sg.Input(key='senha',password_char='§')],
    [sg.Button('Salvar')]
]

login = sg.Window('Tela de Login',layout_login)
cadastro = sg.Window('Tela de Cadastro',layout_cadastro)

while True:
    eventos,valores = login.read()
    eventos,valores = cadastro.read()
    
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Salvar':
        if layout_cadastro[1] != layout_cadastro[2]:
           print('As senhas estão diferentes')
        else:
            print('Senhas iguais')
        if eventos == 'Salvar' and layout_cadastro[1] == layout_cadastro[2]:
            login = sg.Window('Tela de Login',layout_login)