import pyautogui as p
from time import sleep

play = True


def print_hoje():
    
    p.click(153,143) # selecionar data inicial
    sleep(0.8)
    p.press('Enter')
    sleep(0.8)
    p.click(154,171) # selecionar data final
    sleep(0.8)
    p.press('Enter')
    p.press('f5')
    sleep(1)
    p.press('f8')
    
def print_ontem():    

    p.click(153,143) # selecionar data inicial
    sleep(0.8)
    p.press('left')
    p.press('Enter')
    sleep(0.8)
    p.click(154,171) # selecionar data final
    sleep(0.8)
    p.press('left')
    p.press('Enter')
    p.press('f5')
    sleep(1)
    p.press('f8')
    
while play:
    
            print(p.position())
            print("DIGITE O PC\n-marcia\n-bighero")
            pc = str(input())
            
            print("QUER O VALOR DE HOJE OU O VALOR DE ONTEM?\n-hoje\n-ontem")
            hoje = str(input())
            
            if pc == 'marcia':

                p.doubleClick(620,751) # gerencial pc Refugo
                sleep(3)
                p.doubleClick(617,420)
                p.write("goncalvesm")
                sleep(0.5)
                p.doubleClick(582,456)
                p.write("lorena2")
                sleep(0.5)
                p.press('Enter')
                sleep(10)
                p.click(41,57) #menu
                sleep(0.8)
                p.click(354,122) #favorito
                sleep(0.8)
                p.click(367,297) # relatorio
                sleep(3)
                p.click(197,331) # barra inferior
                sleep(0.5)
                p.click(1354,339) # scroll
                sleep(0.5)
                p.dragTo(1353,534) # final scroll
                sleep(0.5)
                p.doubleClick(115,642) # usuario
                sleep(1)
                if hoje == "hoje":
                    print_hoje()
                if hoje == "ontem":
                    print_ontem()   
            
                sleep(2)
                print("AGUARDANDO O GERENCIAL ABRIR OU ESTAR VISIVEL NA TELA")
                p.click(194,241, duration=0.5) # dia inicial
                sleep(2)
                p.click(154,171, duration=0.5) # selecionar data final
                sleep(2)
                p.click(192,267, duration=0.5) # dia final
                p.press('f5') # gerar relatorio
                sleep(0.5)
                p.click(605,61, duration=0.5) # totalizar
                sleep(0.5)
                p.press('printscreen') # printar
                sleep(0.5)
                p.press('win')
                sleep(0.5)
                p.write("paint")
                sleep(1)
                p.press('Enter')
                sleep(2)
                p.hotkey('ctrl','v')
                sleep(1)
                p.click(43,12, duration = 0.5)
                sleep(2)
                p.write("valor do refugo atual")
                sleep(0.5)
                p.press('Enter')
                sleep(0.5)
                play = False

            
