from select import select
import pyautogui as p
from time import sleep


play = True

def sem_saldo():

    sem_saldo5 = p.locateCenterOnScreen('sem_saldo5.png')
    
    if sem_saldo5 != None:

        p.press('Enter')
        print(sem_saldo5)    

def lote():
    
    proc = p.locateCenterOnScreen('proc.png')
    proc_select = p.locateCenterOnScreen('proc_select.png')
    
    print(proc)
    print(proc_select)
    
    if proc != None:
        
        p.moveTo(proc)
        p.doubleClick()
        
    if proc_select != None:
        
        p.moveTo(proc_select)
        p.doubleClick()


print(p.position())

def reaproveitamento():
    
    componentes = 0
    quantidades = 0
    
    
    print("DIGITE A OF:")

    of = str (input())
    
    print('DIGITE QUANTOS ITENS SERAM REAPROVEITADOS:')

    quantidade_de_componentes = int(input())

    lista_de_componentes = []
    lista_de_quantidades = []
    
    estoque = "PROC"
    
    print("O ESTOQUE SEMPRE É:",estoque)
    print("ESCREVA A DATA SEM AS BARRAS '/'\nEX:250922...CORRETO!!!\nEX:25/09/22...ERRADO!!!")
    data = str(input())
    if componentes <= quantidade_de_componentes:

        while componentes != quantidade_de_componentes:
    
            print('QUAL COMPONENTE?')


            componente = str(input())

            print('componente = {}\n'.format(componente))


            print('QUAL A QUANTIDADE?')

            quantidade = str(input())

            print('quantidade = {}\n'.format(quantidade))


            componentes += 1

            lista_de_componentes.append(componente)

            lista_de_quantidades.append(quantidade)

            if componentes == quantidade_de_componentes:
                
                print("DIGITE O PC\n-marcia\n-bighero")
                pc = str(input())
                print(p.position())

                if pc == 'marcia':

                    p.doubleClick(747,749) #debcred

                if pc == 'bighero':

                    p.doubleClick(1314,124) #debcred
                    
                sleep(8)
                p.doubleClick(625,458) #login
                sleep(0.5)
                p.write("goncalvesm") #logi
                sleep(0.5)
                p.press('tab') # mudar para senha
                sleep(0.5)
                p.write("lorena2") # senha
                sleep(0.5)
                p.press('Enter')
                sleep(8)
                p.click(22, 48) #arquivo
                sleep(0.5)
                p.click(113, 106) #pcp
                sleep(0.5)
                p.moveTo(205,106)
                sleep(0.5)
                p.click(191,133) #reaproveitamento
                p.press('Enter')
                p.press('f2')
                sleep(0.5)
                
                while quantidade_de_componentes != 0:

                        item = lista_de_componentes[0]

                        qntd = lista_de_quantidades[0]

                        p.moveTo(144,135)
                        p.doubleClick()
                        p.write(of)
                        sleep(0.5)
                        p.press('tab')
                        sleep(0.5)
                        p.write(item)
                        print(item)
                        sleep(0.5)
                        p.press('tab')
                        sleep(0.5)
                        p.write(estoque)
                        p.moveTo(193,233)
                        p.doubleClick()
                        sleep(3)
                        lote()
                        sleep(0.5)
                        p.moveTo(111,258)
                        p.doubleClick()
                        p.write(data)
                        p.press('tab')
                        sleep(0.5)
                        p.write(qntd)
                        p.press('f5')
                        p.press('Enter')
                        sem_saldo()
                        sleep(3)
                        
                        del lista_de_componentes[0]
                        print(lista_de_componentes)
                        del lista_de_quantidades[0]
                        print(lista_de_quantidades)
                        quantidade_de_componentes -= 1
                        print(quantidade_de_componentes)

                        if quantidade_de_componentes == 0:

                            p.click(1337,14, duration= 0.5)
                            sleep(0.5)
                            p.click(636,421, duration= 0.5)
                
            #componente
            #tab
            #estoque
            #tab
            #lote
            #p.moveTo(193,233)
            #p.doubleClick()
            #sleep(3)
            #lote()
            #tab
            #data
            #p.moveTo(111,258)
            #p.doubleClick()
            #p.write(data)
            #tab
            #quantidade

while play:
    reaproveitamento()
