from Entity import Entity
from random import randint


class World:

	

	def __init__(self,size,player,monsternumber):
		self.size=size
		self.entities=  [ player ]




		

		





		for e in self.entities:
			e.world=self

	
	def GetEntityAtCoords(self,coordinates):
		for e in self.entities:
			if e.coordinates[0]==coordinates[0] and e.coordinates[1]==coordinates[1]:
				return e






	def campo(self):
		for y in range(self.size[1]):
			for x in range(self.size[0]):
				e=self.GetEntityAtCoords((x,y))
				if e!=None:
					print("["+e.graphic+"]", end="")
				else:
					print("[ ]", end="")
			print()