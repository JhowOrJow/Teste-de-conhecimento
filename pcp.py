import pyautogui as p
from time import sleep

play = True

xturno_1 = 20
yturno_1 = 383

xturno_2 = 20
yturno_2 = 400

xturno_3 = 120
yturno_3 = 363

def login():

    global login

    login = p.locateAllOnScreen('login_pcp.png')

    if login != None:

        p.click(614,340)
        usuario = 'oziel'
        usuario = usuario.lower()
        p.write(usuario)
        p.press('tab')
        p.write(usuario)
        p.press('Enter')


'''def pcp():

    
    pcp_barra = p.locateAllOnScreen('pcp_barra.png')
    pcp_area = p.locateAllOnScreen('pcp_area.png')
    exe_pcp = p.locateAllOnScreen('exe_pcp.png')
    exe_pcp2 = p.locateAllOnScreen('exe_pcp2.png')

    if pcp_barra != None or pcp_area != None:

        pcp_barra = p.locateCenterOnScreen('pcp_barra.png')
        pcp_area = p.locateCenterOnScreen('pcp_area.png')

        p.moveTo(pcp_barra)
        p.click()
        print(pcp_barra)

    if exe_pcp != None or exe_pcp2 != None:

        exe_pcp = p.locateCenterOnScreen('exe_pcp.png')
        exe_pcp2 = p.locateCenterOnScreen('exe_pcp2.png')

        p.press('left')
        p.press('Enter')'''


def pcp():

    p.click(807,745)
    sleep(1)
    p.press('left')
    p.press('Enter')

while play:

    print('QUAL TURNO?\n-TURNO 1\n-TURNO 2\n-TURNO 3')
    turno = str(input())
    print(p.position())
    sleep(5)
    pcp()
    sleep(10)
    
    while login != None:
        login()
        sleep(4)
        p.click(294,32)
        sleep(0.5)
        p.click(332,201)
        sleep(3)
        p.click(444,78)
        sleep(0.5)
        p.tripleClick(481,143)
        sleep(3)
    p.moveTo(323,380)  
    p.click(323,380)
    sleep(3)
    p.click(323,380)
    sleep(3)
    if turno == '1':
            sleep(3)
            p.moveTo(xturno_1,yturno_1) 
            p.click(xturno_1,yturno_1)
    if turno == '2':
            p.tripleClick(xturno_2,yturno_2)
    if turno == '3':
            p.tripleClick(xturno_3,yturno_3)
    sleep(0.5)
    p.click(1210,49)
    play = False
    

