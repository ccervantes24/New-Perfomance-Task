import random

games = ["Tetris", "Minecraft ", "GTA V ", "Wii Sports ", "PUBG ", "Mario Kart 8/Mario Kart 8 Deluxe","Overwatch ", "Super Mario Bros ", "Pokémon Generation 1", "Red Dead Redemption 2"] 

values = [games[0] == 10, games[1] == 9, games[2] == 8, games[3] == 7, games[4] == 6, games[5] == 5, games[6] == 4, games[7] == 3, games[8] == 2, games[9] == 1 ]
intro = input("Would you like to play Higher or Lower: Video Game Sales? Y/N ").upper()
if intro == "N":
  print("Okay, thank you for your time!")
elif intro == "Y":
  one = input(f'1. {random.choice(games)}(1) or {random.choice(games)}(2)')
  
    
