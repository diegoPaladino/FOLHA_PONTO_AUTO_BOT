# IMPRESSAO_AUTOMATICA_FOLHA_PONTO

import pyautogui as p
import time as t

count = 48
x = 1
count = int(count)

p.moveTo(x=765, y=750,duration=0.3)

while x <= count:
    
    p.click()
    t.sleep(0.2)
    p.moveTo(x=262, y=171,duration=0.3)
    p.doubleClick()
    t.sleep(0.2)
    p.keyDown('ctrl')
    p.hotkey('c')
    p.keyUp('ctrl')
    t.sleep(0.2)
    p.hotkey('esc')
    t.sleep(0.2)
    p.moveTo(x=555, y=693,duration=0.3)
    p.click()
    p.moveTo(x=262, y=171,duration=0.3)
    p.doubleClick()
    t.sleep(0.2)
    p.keyDown('ctrl')
    p.hotkey('v')
    p.keyUp('ctrl')
    t.sleep(0.5)
    p.hotkey('enter')
    t.sleep(2)
    p.keyDown('ctrl')
    p.hotkey('p')
    p.keyUp('ctrl')
    t.sleep(1)
    p.hotkey('enter')
    t.sleep(1)
    #voltando para a lista de numeros
    p.moveTo(x=755, y=692,duration=0.3)
    p.click()
    t.sleep(0.2)
    p.hotkey('esc')
    p.hotkey('down')

    x+=1



# p.moveTo(x=765, y=750,duration=0.3)
# p.click()
# t.sleep(0.2)
# p.moveTo(x=262, y=171,duration=0.3)
# p.doubleClick()
# t.sleep(0.2)
# p.keyDown('ctrl')
# p.hotkey('c')
# p.keyUp('ctrl')
# t.sleep(0.2)
# p.hotkey('esc')
# p.moveTo(x=555, y=693,duration=0.3)
# p.click()
# p.moveTo(x=262, y=171,duration=0.3)
# p.doubleClick()
# t.sleep(0.2)
# p.keyDown('ctrl')
# p.hotkey('v')
# p.keyUp('ctrl')
# t.sleep(0.5)
# p.hotkey('enter')
# t.sleep(2)
# p.keyDown('ctrl')
# p.hotkey('p')
# p.keyUp('ctrl')
# t.sleep(1)
# p.hotkey('enter')
# t.sleep(1)
# #voltando para a lista de numeros
# p.moveTo(x=755, y=692,duration=0.3)
# p.click()
# t.sleep(0.2)
# p.hotkey('esc')
# p.hotkey('down')

