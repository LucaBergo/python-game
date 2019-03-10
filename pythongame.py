import os
from random import randint
from World import World
from Entity import Entity



wall= Entity([randint(0,5),randint(0,5)], "W" )

player= Entity([0,0],"P")


chiave= Entity([randint(0,4),randint(0,4)], "C")


level1= World((6,6), player, chiave, 8)


counter=0
while True:
	os.system("clear")
	print()
	print("              Developed by Luca Bergognoni        ")
	print()
	print()
	level1.campo()
	command=input().lower()
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
	

	



	











