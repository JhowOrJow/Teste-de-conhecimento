import  pyautogui as p
from time import sleep as s 


play = 13
go = True
b = []
while play:
    s(5)
    a = p.position()
    b.append(a)
    print(b)
    p.click(x=761, y=230)
    s(0.5)
    p.click(x=936, y=430)
    s(0.5)
    p.click(x=936, y=857)
    play -= 1