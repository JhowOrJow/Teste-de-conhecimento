
import pyautogui as p
from time import sleep

play = True


def info():

    info = p.locateCenterOnScreen('informa.png')
    info1 = p.locateCenterOnScreen('of_invalida.png')
    info2 = p.locateCenterOnScreen('info.png')
    info3 = p.locateCenterOnScreen('info1.png')

    if info3 == None:

        info3 = p.locateOnScreen('info1.png')

    if info2 == None:

        info2 = p.locateOnScreen('info.png')

    if info == None:
        
        info = p.locateOnScreen('informa.png')
    
        
    if info1 == None:

        info1 = p.locateOnScreen('of_invalida.png')

    if info != None:

        p.press('Enter')
        print(info)

    if info1 != None:

        p.press('Enter')
        print(info1)

    if info2 != None:

        p.press('Enter')
        print(info2)  

    if info3 != None:

        p.press('Enter')
        print(info3)

    erro = p.locateCenterOnScreen('erro.png')
    erro1 = p.locateCenterOnScreen('erro1.png')
    erro2 = p.locateCenterOnScreen('erro2.png')
    erro3 = p.locateCenterOnScreen('erro3.png')


    if erro2 == None:
        
        erro2 = p.locateOnScreen('erro2.png')

    if erro3 == None:
        
        erro3 = p.locateOnScreen('erro3.png')
    
    if erro == None:
        
        erro = p.locateOnScreen('erro.png')
    
    if erro1 == None:

        erro1 = p.locateOnScreen('erro1.png')

    if erro != None:

        p.press('Enter')
        print(erro)

    if erro1 != None:

        p.press('Enter')
        print(erro1)

    if erro2 != None:

        p.press('Enter')
        print(erro2)

    if erro2 != None:

        p.press('Enter')
        print(erro3)
        
    sem_saldo5 = p.locateCenterOnScreen('sem_saldo5.png')
    
    if sem_saldo5 != None:

        p.press('Enter')
        print(sem_saldo5)    

def apontar_na_mesma_of():

    global defeitos,componentes,quantidades, play
    
    defeitos = 0
    componentes = 0
    quantidades = 0
    
    print('DIGITE QUANTOS ITENS SERAM REFUGADOS:')

    quantidade_de_componentes = int(input())

    lista_de_componentes = []

    lista_de_defeitos = []

    lista_de_quantidades = [] 
    
    if componentes <= quantidade_de_componentes:

        while componentes != quantidade_de_componentes:
    
            print('QUAL COMPONENTE?')

            componente = str(input())

            print('componente = {}\n'.format(componente))


            print('QUAL DEFEITO?')

            defeito = str(input())

            print('defeito = {}\n'.format(defeito))


            print('QUAL A QUANTIDADE?')

            quantidade = str(input())

            print('quantidade = {}\n'.format(quantidade))


            componentes += 1

            lista_de_componentes.append(componente)

            lista_de_defeitos.append(defeito)

            lista_de_quantidades.append(quantidade)


            if componentes == quantidade_de_componentes:

                print(lista_de_componentes)

                print(lista_de_defeitos)

                print(lista_de_quantidades)
                
                print("EM QUAL TURNO SERÁ APONTADO?\n-TURNO 1\n-TURNO 2\n-TURNO 3")

                turno = int (input())

                print("DIGITE A OF:")

                of = str (input())

                operação = "999"

                print("A OPERAÇÃO É:",operação)
                print("ESCREVA A DATA SEM AS BARRAS '/'\nEX:250922...CORRETO!!!\nEX:25/09/22...ERRADO!!!")
                data = str(input())
                print("DIGITE O PC\n-marcia\n-bighero")
                pc = str(input())
                print(p.position())

                if pc == 'marcia':

                    p.doubleClick(747,749) #debcred

                if pc == 'bighero':

                    p.doubleClick(1314,124) #debcred  

            debcred = p.locateCenterOnScreen('debcred.png') 
            
            while debcred == None:

                debcred = p.locateOnScreen('debcred.png')  
                
                if debcred != None:    

                    sleep(5)
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
                    p.moveTo(205,106) # mover para refugo
                    sleep(0.5)
                    p.moveTo(205,157) # chegar no refugo
                    sleep(0.5)
                    p.click() #refugo
                    sleep(5)
                    p.press('f2') #pag de lancamento
                    p.keyDown('down') #selecionar tipo de refugo
                    sleep(1)
                    p.keyDown('down') #componente
                    sleep(0.5)
                    p.click(120,160)

                    if turno == 1:
                        
                        p.click(120,160) #turno
                        
                    if turno == 2:    
                        
                        p.click(112,187) #turno
                        
                    if turno == 3:    
                        
                        p.click(113,200) #turno
                        
                    sleep(0.5)
                    p.click(122,182)
                    p.write(of)
                    p.press('Enter')
                    sleep(0.5)
                    p.press('tab')
                    p.press('Enter')
                    
                    sleep(0.5)
                    p.write(operação)
                    sleep(0.5)
                    p.press('tab')
                    p.press('Enter')


                    while quantidade_de_componentes != 0:

                            item = lista_de_componentes[0]

                            motivo = lista_de_defeitos[0]

                            qntd = lista_de_quantidades[0]

                            sleep(0.5)
                            p.press('Enter')
                            p.doubleClick(168,254)
                            p.write(item)
                            p.press('Enter')
                            print(item)
                            sleep(0.5)
                            p.press('tab')
                            p.press('Enter')
                            
                            sleep(0.5)
                            p.write(motivo)
                            p.press('Enter')
                            sleep(0.5)
                            p.press('tab')
                            p.press('Enter')
                            
                            sleep(0.5)
                            p.write(data)
                            p.press('Enter')
                            p.press('tab')
                            p.press('Enter')
                            
                            sleep(0.5)
                            p.write(qntd)
                            p.press('Enter')
                            p.press('f5')
                            sleep(1)
                            p.press('Enter')
                            
                            
                            
                            del lista_de_componentes[0]
                            print(lista_de_componentes)
                            del lista_de_defeitos [0]
                            print(lista_de_defeitos)
                            del lista_de_quantidades[0]
                            print(lista_de_quantidades)
                            quantidade_de_componentes -= 1
                            print(quantidade_de_componentes)

                            if quantidade_de_componentes == 0:

                                p.click(1337,14, duration= 0.5)
                                sleep(0.5)
                                p.click(636,421, duration= 0.5)
                                apontar_outra_of()
                if  debcred == None:
                    print("AGUARDANDO O DEBCRED ABRIR OU ESTAR VISIVEL NA TELA")                
                            

                               


def apontar_outra_of():
    
    global defeitos,componentes,quantidades, play
    
    defeitos = 0
    componentes = 0
    quantidades = 0
    of = 0

    print("DIGITE QUANTAS OF's SERAM REFUGADAS:")

    quantidade_de_of = int(input())

    lista_de_componentes = []

    lista_de_defeitos = []

    lista_de_quantidades = [] 
    
    
    lista_de_of = []

    if componentes <= quantidade_de_of:

        while componentes != quantidade_de_of:

            '''print("QUAL TIPO DE REFUGO?\n1-COMPONENTE\n2-PRODUTO")
            tipo = str(input())
            tipo = tipo.upper()'''

            print('QUAL OF?')

            of = str(input())

            print('of = {}\n'.format(of))
    
            print('QUAL COMPONENTE?')

            componente = str(input())

            print('componente = {}\n'.format(componente))


            print('QUAL DEFEITO?')

            defeito = str(input())

            print('defeito = {}\n'.format(defeito))


            print('QUAL A QUANTIDADE?')

            quantidade = str(input())

            print('quantidade = {}\n'.format(quantidade))


            componentes += 1

            lista_de_componentes.append(componente)

            lista_de_defeitos.append(defeito)

            lista_de_quantidades.append(quantidade)

            lista_de_of.append(of)

            if componentes == quantidade_de_of:

                print(lista_de_componentes)

                print(lista_de_defeitos)

                print(lista_de_quantidades)


                print(lista_de_of)
                
                print("EM QUAL TURNO SERÁ APONTADO?\n-TURNO 1\n-TURNO 2\n-TURNO 3")

                turno = int (input())

                operação = "999"

                print("A OPERAÇÃO É:",operação)
                print("ESCREVA A DATA SEM AS BARRAS '/'\nEX:250922...CORRETO!!!\nEX:25/09/22...ERRADO!!!")
                data = str(input())
                print("DIGITE O PC\n-marcia\n-bighero")
                pc = str(input())
                print(p.position())

                if pc == 'marcia':

                    p.doubleClick(747,749) #debcred

                if pc == 'bighero':

                    p.doubleClick(1314,124) #debcred  


                debcred = p.locateCenterOnScreen('debcred.png') 


                while debcred == None:
                    
                    debcred = p.locateOnScreen('debcred.png')  
                    
                    
                    
                    if debcred != None:    

                        sleep(5)
                        p.doubleClick(625,458) #login
                        sleep(0.5)
                        p.write("goncalvesm") #logi

                        sleep(0.5)
                        p.press('tab') # mudar para senha
                        sleep(0.5)
                        p.write("lorena") # senha
                        sleep(0.5)
                        p.press('Enter')
                        sleep(8)
                        p.click(22, 48) #arquivo
                        sleep(0.5)
                        p.click(113, 106) #pcp
                        sleep(0.5)
                        p.moveTo(205,106) # mover para refugo
                        sleep(0.5)
                        p.moveTo(205,157) # chegar no refugo
                        sleep(0.5)
                        p.click() #refugo
                        sleep(5)
                        p.press('f2') #pag de lancamento
                        #if tipo == "1":
                        p.keyDown('down') #selecionar tipo de refugo
                        sleep(1)
                        p.keyDown('down') #componente

                        '''if tipo =="2":   

                        p.keyDown('down')#produto'''
                        sleep(0.5)
                        p.click(120,160)
                        

                        if turno == 1:
                            
                            p.click(120,160) #turno
                            
                        if turno == 2:    
                            
                            p.click(112,187) #turno
                            
                        if turno == 3:    
                            
                            p.click(113,200) #turno


                        while quantidade_de_of != 0:

                                item = lista_de_componentes[0]

                                motivo = lista_de_defeitos[0]

                                qntd = lista_de_quantidades[0]

                                ofs = lista_de_of[0]

                                sleep(0.5)
                                p.press('Enter')
                                p.doubleClick(122,182)                
                                p.write(ofs)
                                p.press('Enter')
                                print(ofs)
                                sleep(0.5)
                                p.press('tab')
                                p.press('Enter')
                                
                                sleep(0.5)
                                p.write(operação)
                                sleep(0.5)
                                p.press('tab')
                                
                                sleep(0.5)
                                #if tipo == "1":
                                p.doubleClick(168,254)
                                p.write(item)
                                p.press('Enter')
                                print(item)
                                sleep(0.5)
                                p.press('tab')
                                p.press('Enter')

                                sleep(0.5)
                                #if tipo =="2": 
                                p.doubleClick(125,279)
                                p.write(motivo)
                                p.press('Enter')
                                sleep(0.5)
                                p.press('tab')
                                p.press('Enter')
                                
                                sleep(0.5)
                                p.write(data)
                                p.press('Enter')
                                sleep(0.5)
                                p.press('tab')
                                p.press('Enter')
                                
                                sleep(0.5)
                                p.write(qntd)
                                p.press('Enter')
                                p.press('f5')
                                sleep(10)
                                p.press('Enter')
                                
                                
                                
                                
                                
                                del lista_de_componentes[0]
                                print(lista_de_componentes)
                                del lista_de_defeitos [0]
                                print(lista_de_defeitos)
                                del lista_de_quantidades[0]
                                print(lista_de_quantidades)
                                del lista_de_of[0]
                                print(lista_de_of)
                                quantidade_de_of -= 1
                                print(quantidade_de_of)

                                if quantidade_de_of == 0:

                                    p.click(1337,14, duration= 0.5)
                                    sleep(0.5)
                                    p.click(636,421, duration= 0.5)
                                    apontar_outra_of()
                    if debcred == None:
                        
                        print("AGUARDANDO O DEBCRED ABRIR OU ESTAR VISIVEL NA TELA")                
 
while play:

    print('APONTAMENTO DE VARIOS ITENS NA MESMA OF?')
    
    resposta = str (input())
    resposta = resposta.upper()
    
    print(p.position())
    
    if resposta == "SIM" or resposta == "S":
        apontar_na_mesma_of()
    else:
        apontar_outra_of()  
        
    '''LOAD_GLOBAL(p), LOAD_METHOD(locateCenterOnScreen), LOAD_CONST('informa.png'), CALL_METHOD{1}, STORE_FAST(info)
LOAD_GLOBAL(p), LOAD_METHOD(locateCenterOnScreen), LOAD_CONST('of_invalida.png'), CALL_METHOD{1}, STORE_FAST(info1)
LOAD_GLOBAL(p), LOAD_METHOD(locateCenterOnScreen), LOAD_CONST('info.png'), CALL_METHOD{1}, STORE_FAST(info2)
LOAD_GLOBAL(p), LOAD_METHOD(locateCenterOnScreen), LOAD_CONST('info1.png'), CALL_METHOD{1}, STORE_FAST(info3)

LOAD_FAST(info3), LOAD_CONST(None), COMPARE_OP(==), POP_JUMP_IF_FALSE(to 58)

LOAD_GLOBAL(p), LOAD_METHOD(locateOnScreen), LOAD_CONST('info1.png'), CALL_METHOD{1}, STORE_FAST(info3)

LOAD_FAST(info2), LOAD_CONST(None), COMPARE_OP(==), POP_JUMP_IF_FALSE(to 76)

LOAD_GLOBAL(p), LOAD_METHOD(locateOnScreen), LOAD_CONST('info.png'), CALL_METHOD{1}, STORE_FAST(info2)

LOAD_FAST(info), LOAD_CONST(None), COMPARE_OP(==), POP_JUMP_IF_FALSE(to 94)

LOAD_GLOBAL(p), LOAD_METHOD(locateOnScreen), LOAD_CONST('informa.png'), CALL_METHOD{1}, STORE_FAST(info)


LOAD_FAST(info1), LOAD_CONST(None), COMPARE_OP(==), POP_JUMP_IF_FALSE(to 112)

LOAD_GLOBAL(p), LOAD_METHOD(locateOnScreen), LOAD_CONST('of_invalida.png'), CALL_METHOD{1}, STORE_FAST(info1)

LOAD_FAST(info), LOAD_CONST(None), COMPARE_OP(!=), POP_JUMP_IF_FALSE(to 138)

LOAD_GLOBAL(p), LOAD_METHOD(press), LOAD_CONST('Enter'), CALL_METHOD{1}, POP_TOP
print(info)

LOAD_FAST(info1), LOAD_CONST(None), COMPARE_OP(!=), POP_JUMP_IF_FALSE(to 164)

LOAD_GLOBAL(p), LOAD_METHOD(press), LOAD_CONST('Enter'), CALL_METHOD{1}, POP_TOP
print(info1)

LOAD_FAST(info2), LOAD_CONST(None), COMPARE_OP(!=), POP_JUMP_IF_FALSE(to 190)

LOAD_GLOBAL(p), LOAD_METHOD(press), LOAD_CONST('Enter'), CALL_METHOD{1}, POP_TOP
print(info2)

LOAD_FAST(info3), LOAD_CONST(None), COMPARE_OP(!=), POP_JUMP_IF_FALSE(to 216)

LOAD_GLOBAL(p), LOAD_METHOD(press), LOAD_CONST('Enter'), CALL_METHOD{1}, POP_TOP
print(info3)

LOAD_GLOBAL(p), LOAD_METHOD(locateCenterOnScreen), LOAD_CONST('erro.png'), CALL_METHOD{1}, STORE_FAST(erro)
LOAD_GLOBAL(p), LOAD_METHOD(locateCenterOnScreen), LOAD_CONST('erro1.png'), CALL_METHOD{1}, STORE_FAST(erro1)
LOAD_GLOBAL(p), LOAD_METHOD(locateCenterOnScreen), LOAD_CONST('erro2.png'), CALL_METHOD{1}, STORE_FAST(erro2)
LOAD_GLOBAL(p), LOAD_METHOD(locateCenterOnScreen), LOAD_CONST('erro3.png'), CALL_METHOD{1}, STORE_FAST(erro3)


LOAD_FAST(erro2), LOAD_CONST(None), COMPARE_OP(==), POP_JUMP_IF_FALSE(to 274)

LOAD_GLOBAL(p), LOAD_METHOD(locateOnScreen), LOAD_CONST('erro2.png'), CALL_METHOD{1}, STORE_FAST(erro2)

LOAD_FAST(erro3), LOAD_CONST(None), COMPARE_OP(==), POP_JUMP_IF_FALSE(to 292)

LOAD_GLOBAL(p), LOAD_METHOD(locateOnScreen), LOAD_CONST('erro3.png'), CALL_METHOD{1}, STORE_FAST(erro3)

LOAD_FAST(erro), LOAD_CONST(None), COMPARE_OP(==), POP_JUMP_IF_FALSE(to 310)

LOAD_GLOBAL(p), LOAD_METHOD(locateOnScreen), LOAD_CONST('erro.png'), CALL_METHOD{1}, STORE_FAST(erro)

LOAD_FAST(erro1), LOAD_CONST(None), COMPARE_OP(==), POP_JUMP_IF_FALSE(to 328)

LOAD_GLOBAL(p), LOAD_METHOD(locateOnScreen), LOAD_CONST('erro1.png'), CALL_METHOD{1}, STORE_FAST(erro1)

LOAD_FAST(erro), LOAD_CONST(None), COMPARE_OP(!=), POP_JUMP_IF_FALSE(to 354)

LOAD_GLOBAL(p), LOAD_METHOD(press), LOAD_CONST('Enter'), CALL_METHOD{1}, POP_TOP
print(erro)

LOAD_FAST(erro1), LOAD_CONST(None), COMPARE_OP(!=), POP_JUMP_IF_FALSE(to 380)

LOAD_GLOBAL(p), LOAD_METHOD(press), LOAD_CONST('Enter'), CALL_METHOD{1}, POP_TOP
print(erro1)

LOAD_FAST(erro2), LOAD_CONST(None), COMPARE_OP(!=), POP_JUMP_IF_FALSE(to 406)

LOAD_GLOBAL(p), LOAD_METHOD(press), LOAD_CONST('Enter'), CALL_METHOD{1}, POP_TOP
print(erro2)

LOAD_FAST(erro2), LOAD_CONST(None), COMPARE_OP(!=), POP_JUMP_IF_FALSE(to 432)

LOAD_GLOBAL(p), LOAD_METHOD(press), LOAD_CONST('Enter'), CALL_METHOD{1}, POP_TOP
print(erro3)

LOAD_GLOBAL(p), LOAD_METHOD(locateCenterOnScreen), LOAD_CONST('sem_saldo5.png'), CALL_METHOD{1}, STORE_FAST(sem_saldo5)

LOAD_FAST(sem_saldo5), LOAD_CONST(None), COMPARE_OP(!=), POP_JUMP_IF_FALSE(to 472), return |472|None

LOAD_GLOBAL(p), LOAD_METHOD(press), LOAD_CONST('Enter'), CALL_METHOD{1}, POP_TOP
print(sem_saldo5), return None
'''
    
    play = False