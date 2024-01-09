import  pyautogui as p
from time import sleep as s 
import pandas as pd
import chardet

play = True
go = True
op = "999"
mes = "12"
ano = "23"
while play:
        with open('of_refugo.csv', 'rb') as rawdata:
            result = chardet.detect(rawdata.read(10000000))
            encoding = result['encoding']
            dtype_config = {'produto': str}
            dados = pd.read_csv('of_refugo.csv',dtype=dtype_config, delimiter=';', encoding=encoding)# Se o arquivo estiver tabulado
            print(dados)
            print(dados.dtypes)
            dados['of'] = dados['of'].astype(str)
            print(dados.dtypes)
            dados['produto'] = dados['produto'].astype(str)
            print(dados.dtypes)
            dados['defeito'] = dados['defeito'].astype(str)
            print(dados.dtypes)
            dados['dia'] = dados['dia'].astype(str)
            print(dados.dtypes)
            dados['quantidade'] = dados['quantidade'].astype(str)
            print(dados.dtypes)
            ofs = dados['of'].tolist()
            produto = dados['produto'].tolist()
            defeito = dados['defeito'].tolist()
            dia = dados['dia'].tolist()
            quantidade = dados['quantidade'].tolist()
            print(produto)
            print(ofs)
            while go:
                p.doubleClick(x=142, y=186)
                p.write(ofs[0])
                p.press('tab')
                p.write(op)
                p.press('tab')
                p.write(produto[0])
                p.press('tab')
                p.write(defeito[0])
                p.press('tab')
                p.write(dia[0])
                p.write(mes)
                p.write(ano)
                p.press('tab')
                p.write(quantidade[0])
                p.press('f5')
                del ofs [0]
                del produto [0]
                del defeito [0]
                del dia [0]
                del quantidade [0]
                s(8)
                p.press('enter')
                s(2)
                if len(ofs) == 0:
                    play = False
                    go = False