import pyautogui as p
from time import sleep

play = True

while play:
    
    sem_saldo = p.locateOnScreen('sem_saldo.png')
    sem_saldo2 = p.locateOnScreen('sem_saldo2.png')

    if sem_saldo != None:

        p.click(800,449)
        print(sem_saldo)

    if sem_saldo2 != None:

        p.click(800,475)
        print(sem_saldo2)