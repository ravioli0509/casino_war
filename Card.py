from random import shuffle
from CQ import Queue  

class Card:
	
	def __init__(self, rank, suit): #initializes the items, ranks and suits 
		self.rank = rank 
		self.suit = suit

	def get(self):
		return self.rank+self.suit #returns the combination of ranks and suits to make a card
		
	def get_rank(self): #returns ranks
		return self.rank 	
	
	def get_suit(self): #returns suits
		return self.suit

	def convert_rank(self, rank): #Makes the ranks in list form and returns their index
		ranks = ["2","3","4","5","6","7","8","9","T".upper(),"J".upper(),"Q".upper(),"K".upper(),"A".upper()]
		return ranks.index(rank)

	def __gt__(self, other): #Using the index from convert rank, we check if self is greater than other rank
		return self.convert_rank(self.get_rank())>self.convert_rank(other.get_rank())

	def __lt__(self, other): #Using the index from convert rank, we check if self is less than other rank
		return self.convert_rank(self.get_rank()) < self.convert_rank(other.get_rank())

	def __eq__(self, other): #Using the index from convert rank, we check if self is equal other rank
		return self.convert_rank(self.get_rank()) == self.convert_rank(other.get_rank())		
			
	def __str__(self): #returns the format of the card for string
		return self.rank+self.suit 