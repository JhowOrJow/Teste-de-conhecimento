from time import sleep as s 
import  pyautogui as p
import pandas as pd
import chardet

play = True
go = True
itens = 5
lista_de_produto = []

while itens > 0:
    s(5)
    produtos = p.position()
    lista_de_produto.append(produtos)   
    print(lista_de_produto)
    itens -= 1
    