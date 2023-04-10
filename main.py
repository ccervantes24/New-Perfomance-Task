import random

games = ["Tetris (1984)", "Minecraft (2009)", "GTA V (2013)", "Wii Sports (2006)", "PUBG (2017)", "Mario Kart 8/Mario Kart 8 Deluxe (2014)", "Super Mario Bros. (1985)", "Pokémon Generation 1 (1996)", "Pokémon Generation 1 (1996)"] 

intro = input(print("Would you like to play Higher or Lower: Video Game Sales? Y/N "))
if intro == 'Y' or 'y':
    one = input(f'{random.choice(games)} or {random.choice(games)}')
else:
    print("Ok, See You Later! ")