import random
import  PySimpleGUI as sg 
import os   

class PassGen:
    def __init__(self) -> None:
        sg.theme('Black')
        layout = [
            [sg.Text('Site',size=(10,1)),
             sg.Input(key='site',size=(20,1))],
            [sg.Text('E-mail',size=(10,1)),
             sg.Input(key='usuario',size=(20,1))],
            [sg.Text('Quantidade de Caracteres'),sg.Combo(values=list(range(30)),key='total_chars',default_value=1,size=(3,1))],
            [sg.Output(size=(32,5))],
            [sg.Button('Gerar Senha')]
        ]
        self.janela = sg.Window('Password Generator',layout)
        
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.Salvar_Senha(nova_senha,valores)
                
    def gerar_senha(self,valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*£¢¬§+-=<>^º'
        chars = random.choices(char_list,k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass
    
    def Salvar_Senha(self,nova_senha,valores):
        with open('Senhas.txt','a',newline='')as arquivo:
            arquivo.write(
                f"Site: {valores['site']};\nUsuário: {valores['usuario']};\nNova Senha: {nova_senha}\n\n"
                )
            print('Arquivo Salvo em Senhas.TXT ')
        
    
gen = PassGen()
gen.Iniciar()     
    