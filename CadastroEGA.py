import  pyautogui as p 
from time import sleep as s 
import pandas as pd
import chardet

play = True
go = True

while play:
    with open('produtos.csv', 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000000))

        encoding = result['encoding']
        dados = pd.read_csv('produtos.csv', delimiter=';', encoding=encoding) # Se o arquivo estiver tabulado
        print(dados.dtypes)
        dados['Produto'] = dados['Produto'].astype(str)
        print(dados.dtypes)
        Produto = dados['Produto'].tolist()
        print(Produto)
        dados['Prod/Ciclo (Cavidades)'] = dados['Prod/Ciclo (Cavidades)'].astype(str)
        Prod_Ciclo = dados['Prod/Ciclo (Cavidades)'].tolist()
        print(Prod_Ciclo)
        dados['Ciclos/Prod'] = dados['Ciclos/Prod'].astype(str)
        Ciclos_Prod = dados['Ciclos/Prod'].tolist()
        print(Ciclos_Prod)
        dados['Produtos/Hora'] = dados['Produtos/Hora'].astype(str)
        Produtos_Hora = dados['Produtos/Hora'].tolist()
        print(Produtos_Hora)
        dados['Peso'] = dados['Peso'].astype(str)
        Peso = dados['Peso'].tolist()
        print(Peso)
        dados['Descrição'] = dados['Descrição'].astype(str)
        Descrição = dados['Descrição'].tolist()
        print(Descrição)
        while go:
            p.doubleClick(x=737, y=303)
            p.write(Produto[0])
            p.press('tab')
            p.press('tab')
            p.write(Descrição[0])
            p.press('tab')
            p.write(Prod_Ciclo[0])
            p.press('tab')
            p.write(Produtos_Hora[0])
            p.press('tab')
            p.write(Ciclos_Prod[0])
            p.press('tab')
            p.write(Peso[0])
            p.press('tab')
            p.press('tab')
            p.press('tab')
            p.press('tab')
            p.write('Hrs')
            p.press('Enter')
            p.press('tab')
            p.press('Enter')
            s(1)
            del Produto[0]
            del Peso[0]
            del Ciclos_Prod[0]
            del Prod_Ciclo[0]
            del Produtos_Hora[0]
            del Descrição[0]
            if len(Produto) == 0:
                    play = False
                    go = False