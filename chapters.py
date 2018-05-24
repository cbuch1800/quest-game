import time
from fancy_print import type_print

def chapter_zero():

    # Entrance to the tavern
    type_print('"Hello there."')
    time.sleep(3)
    type_print('"What can I get you?"')
    player_drink = input('Will it be a whisky (W), an ale (A) or a cider (C)?\n> ').upper()
    time.sleep(1)
    while not player_drink in ['W','A','C']:
        type_print('"Sorry, I {} quite catch that."'.format("didn't"))
        player_drink = input("> ").upper()
        time.sleep(1)
    if player_drink == 'W':
        type_print('"This is a double malt whisky aged 12 years in a Yterrian Oak cask."')
        player_drink = 'whiskey'
    elif player_drink == 'A':
        type_print('"This high-strength ale is brewed by dwarves using local barley and spring water from The Highlands."')
        player_drink = 'ale'
    elif player_drink == 'C':
        type_print('"This cider is pressed from golden pears and apples, hand-picked from the orchard by nymphs"')
        player_drink = 'cider'
    time.sleep(1)
    


while True:
    chapter_zero()



