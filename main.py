import pyautogui as pg
import random
import time
import decimal

amount_of_iterations = 20

while amount_of_iterations > 0:
    # Random seconds between .5 - 2
    seconds = decimal.Decimal(random.randrange(50, 200))/100
    time.sleep(int(seconds))
    
    # clicks
    pg.click()
    amount_of_iterations -= 1

    