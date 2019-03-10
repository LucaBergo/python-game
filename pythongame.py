mport os
from random import randint
from World import World
from Entity import Entity




player= Entity([0,0],"P")


level1= World((6,6), player, 3)



while True:
	os.system("cls")
	print()
	print("              Developed by Luca Bergognoni            ")
	print()
	print()
	level1.campo()
	command=input().lower()
	counter+=1
	if command=="w":
		player.move("N")
	elif command=="s":
		player.move("S")
	elif command=="a":
		player.move("W")
	elif command=="d":
		player.move("E")
	elif command== "b":
		break
