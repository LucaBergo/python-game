 from random import randint

#non ho programmato il world perciò è tutto teorico
#height e weight idicano  altezza e larghezza di un ipotetico mondo
#serve creare funzione in file world che passando la lista delle entities dia la loro posizione
#volevo fare che ogni mostro ponesse un enigma, in questo caso l ho fatto solo per un unico mostro nel campo


 class Entity:






	def __init__(self,x,y,graphic):
		self.x=x
		self.y=y
		self.graphic=graphic
		
		if x<0:
			x=0
		if y<0:
			y=0




	def move(self,direction):
		
		curX=self.x
		curY=self.y




		if direction=="N" and curY>0 :
			self.y= self.y-1
			
		elif direction== "S" and curY<=world.height-1 :
			self.y= self.y+1
		
		elif direction== "W" and curX>0  :
			self.x= self.x-1
			
		elif direction== "E" and curX<=world.weight-1:
			
			self.x= self.x+1

		


		#gestione attacco mostri



		elif direction=="N" and curY>0: #e c'è un mostro 
			


			self.y= self.y-1
			print("Il mostro ti ha sfidato")
			print("Quanto fa 2+2x2?")
			print("Inserisci la lettera")
			res= input("a-6     b-8     c-4 " )
			res=res.lower()

			if res=="a":
				print("Hai ucciso il mostro")
				mosternumber-=1
			
			elif res=="b":
				print("Sbagliato")
				print("Game Over")
				exit()
			elif res=="c":
				print("Sbagliato")
				print("Game Over")
				exit()



		
			
		


		elif direction== "S" and curY<=world.height-1: #e c'è un mostro 
			


			self.y= self.y+1
			print("Il mostro ti ha sfidato")
			print("Quanto fa 2+2x2?")
			print("Inserisci la lettera")
			res= input("a-6     b-8     c-4 " )
			res=res.lower()

			if res=="a":
				print("Hai ucciso il mostro")
				mosternumber-=1
			
			elif res=="b":
				print("Sbagliato")
				print("Game Over")
				exit()
			elif res=="c":
				print("Sbagliato")
				print("Game Over")
				exit()



		elif direction== "W" and curX>0:  #e c'è un mostro
			


			self.x= self.x-1
			print("Il mostro ti ha sfidato")
			print("Quanto fa 2+2x2?")
			print("Inserisci la lettera")
			res= input("a-6     b-8     c-4 " )
			res=res.lower()

			if res=="a":
				print("Hai ucciso il mostro")
				mosternumber-=1
			
			elif res=="b":
				print("Sbagliato")
				print("Game Over")
				exit()
			elif res=="c":
				print("Sbagliato")
				print("Game Over")
				exit()



		
		elif direction== "E" and curX<=world.weight-1 : #e c'è un mostro
			



			self.x= self.x+1
			
			print("Il mostro ti ha sfidato")
			print("Quanto fa 2+2x2?")
			print("Inserisci la lettera")
			res= input("a-6     b-8     c-4 " )
			res=res.lower()

			if res=="a":
				print("Hai ucciso il mostro")
				mosternumber-=1
			
			elif res=="b":
				print("Sbagliato")
				print("Game Over")
				exit()
			elif res=="c":
				print("Sbagliato")
				print("Game Over")
				exit()


