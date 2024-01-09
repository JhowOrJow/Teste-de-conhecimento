import  pyautogui as p
from time import sleep as s 
import pandas as pd
import chardet

login = 'neresj'
senha = 'jonathan2023'
play = True
go = True

while play:
            with open('REFUG3.txt', 'rb') as rawdata:
                        result = chardet.detect(rawdata.read(10000000))

            encoding = result['encoding']
            dados = pd.read_csv('REFUG3.txt', delimiter=';', encoding=encoding) # Se o arquivo estiver tabulado
            print(dados.dtypes)
            dados['O.F. Mãe'] = dados['O.F. Mãe'].astype(str)
            print(dados.dtypes)
            of = dados['O.F. Mãe'].tolist()
            print(dados)
            print(of)
            p.click(x=707, y=1064)
            
            s(3)
            p.click(x=863, y=568)
            p.write(login)
            p.press('tab')
            p.write(senha)
            p.press('enter')
            s(5)
            p.press('left')
            p.press('enter')
            
            s(5)
            p.doubleClick(x=140, y=192)
            p.press('f11')
            s(2)
            p.click(x=41, y=141)
            while go:
                p.press('f11')
                p.write(of[0])
                p.press('enter')
                s(1)
                #p.click(x=596, y=139)
                #p.click(x=875, y=293)
                #s(.5)
                p.click(x=596, y=139)
                p.click(x=596, y=195)
                s(1)
                p.press('enter')
                s(1)
                p.press('enter')
                del of[0]

                if len(of) == 0:
                    play = False
                    go = False

        