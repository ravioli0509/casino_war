from Card import Card

class Player:
	def __init__(self):
		#implement the properties here
		#TODO
		self.chips = 0 #starts the game with 0 chips

	
	def add_chips(self, chips): #add self chips with chips
		self.chips = self.chips + chips
		
	def remove_chips(self, chips): #subtract self chips with chips
		self.chips = self.chips - chips
	
	
	def get_chips(self): #return chips
		return self.chips

		
