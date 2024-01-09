import  pyautogui as p
from time import sleep as s 
import pandas as pd
import chardet

play = 1
go = True
ofs = []
op = "999"
produto = []
defeito = []
dia = []
mes = "12"
ano = "23"
qnt = []
print("Apontamentos\n")
ply = int(input())
print(ply)
while play:
        with open('of_refugo.xlsx', 'rb') as rawdata:
                        result = chardet.detect(rawdata.read(10000000))

            encoding = result['encoding']
            dados = pd.read_excel('of_refugo.xlsx', delimiter=';', encoding=encoding) # Se o arquivo estiver tabulado
            print(dados.dtypes)
            dados['of'] = dados['of'].astype(str)
            print(dados.dtypes)
            ofs = dados['of'].tolist()
            print(dados)
            print(ofs)
    '''while ply != 0:
        print("of\n")
        of = str(input())
        ofs.append(of)
        print(ofs)
        print("produto\n")
        prod = str(input())
        produto.append(prod)
        print(produto)
        print("defeito\n")
        defe = str(input())
        defeito.append(defe)
        print(defeito)
        print("dia\n")
        day = str(input())
        dia.append(day)
        print(dia)
        print("quantidade\n")
        qntd = str(input())
        qnt.append(qntd)
        print(qnt)
        s(2)
        ply -= 1
    
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
        p.write(qnt[0])
        p.press('f5')
        del ofs [0]
        del produto [0]
        del defeito [0]
        del dia [0]
        del qnt [0]
        s(8)
        p.press('enter')
        s(2)
        play -= 1
        if len(ofs) == 0:
            go = False
            