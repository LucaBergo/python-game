from random import randint

class Entity:



	

	def __init__(self,coordinates,graphic):
		self.coordinates=coordinates
		self.graphic=graphic
		
		for i in range(2):
			if coordinates[i]<0:
				coordinates[i]=0

	def move(self,direction):
		curX=self.coordinates[0]
		curY=self.coordinates[1]
		world=self.world



		if self.world==None:
			return

		


		if direction=="N" and curY>0 and world.GetEntityAtCoords((curX,curY-1))==None :
			self.coordinates[1]= self.coordinates[1]-1
			
		elif direction== "S" and curY<=world.size[1]-2 and world.GetEntityAtCoords((curX,curY+1))==None:
			self.coordinates[1]= self.coordinates[1]+1
			
		elif direction== "W" and curX>0  and world.GetEntityAtCoords((curX-1,curY))==None:
			self.coordinates[0]= self.coordinates[0]-1
			
		elif direction== "E" and curX<=world.size[0]-2 and world.GetEntityAtCoords((curX+1,curY))==None:
			self.coordinates[0]= self.coordinates[0]+1

		elif direction=="N" and curY>0 and world.GetEntityAtCoords((curX,curY-1))=="W" :
			
			self.coordinates[1]= self.coordinates[1]

		elif direction== "S" and curY<=world.size[1]-2 and world.GetEntityAtCoords((curX,curY+1))=="W":
			
			self.coordinates[1]= self.coordinates[1]

			
		elif direction== "W" and curX>0  and world.GetEntityAtCoords((curX-1,curY))=="W":

			self.coordinates[0]= self.coordinates[0]
	
		elif direction== "E" and curX<=world.size[0]-2 and world.GetEntityAtCoords((curX+1,curY))=="W":
			
			self.coordinates[0]= self.coordinates[0]


		elif direction=="N" and curY>0 and world.GetEntityAtCoords((curX,curY-1))=="C" :
			
			self.coordinates[1]= self.coordinates[1]-1
			entities.remove(chiave)
			counter+=1

		elif direction== "S" and curY<=world.size[1]-2 and world.GetEntityAtCoords((curX,curY+1))=="C":
			
			self.coordinates[1]= self.coordinates[1]+1
			entities.remove(chiave)
			counter+=1

			
		elif direction== "W" and curX>0  and world.GetEntityAtCoords((curX-1,curY))=="C":

			self.coordinates[0]= self.coordinates[0]-1
			entities.remove(chiave)
			counter+=1
	
		elif direction== "E" and curX<=world.size[0]-2 and world.GetEntityAtCoords((curX+1,curY))=="C":
			
			self.coordinates[0]= self.coordinates[0]+1
			entities.remove(chiave)
			counter+=1



