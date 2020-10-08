from Card import Card
from random import shuffle
from CQ import Queue
import time 
import random


class Table:
	def __init__(self):
		#Variables will be set to 0
		self.shoe = 0
		self.player_card = 0
		self.dealer_card = 0
		self.discard = Queue()
		self.bet = 0		

	def resolve_round(self, srrank, orrank):
		print("Let's see the result...\n")
		time.sleep(random.randint(1,2))
		print("Player shows "+str(srrank)+", Dealer shows "+str(orrank))
		if Card.convert_rank(srrank, srrank.get_rank()) > Card.convert_rank(orrank, orrank.get_rank()):
			#checks if player is higher than dealer
			print("Player wins!\n")
			return 1
		elif Card.convert_rank(orrank, orrank.get_rank()) > Card.convert_rank(srrank, srrank.get_rank()):
			#checks if dealer is higher than player
			print("Dealer wins!\n")
			return -1
		elif Card.convert_rank(srrank, srrank.get_rank()) == Card.convert_rank(orrank, orrank.get_rank()):
			#checks if dealer and player have the same rank
			time.sleep(random.randint(0,1))
			print("War!\n")
			return 0	
	
	def set_bet(self, bet):
		self.bet = bet #bet becomes the self.bet
	
	def get_bet(self):
		return self.bet #get_bet simply returns the bet
	
	def clear(self): #player and dealer cards will be enqueued into the disscard queue
		self.discard.enqueue(self.player_card) 
		self.discard.enqueue(self.dealer_card)
		self.dealer_card = 0
		self.player_card = 0
		
	def create_deck(self): #suits and ranks will be appended into temp list as cards
		suits = ["S".upper(),"H".upper(),"D".upper(),"C".upper()]
		ranks = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
		temp = []
		for i in suits:
			for j in ranks:
				temp.append(Card(j,i))
		return temp
		
	def validate_deck(self, deck):
		#validation for the cards and their format
		suits = ["S".upper(),"H".upper(),"D".upper(),"C".upper()]
		ranks = ["2","3","4","5","6","7","8","9","T".upper(),"J".upper(),"Q".upper(),"K".upper(),"A".upper()]
		if len(deck) != 52: #raises exception if the length of deck is not 52
			raise Exception("Total number of cards have to be 52")
		duplicate = []
		for card in deck:
			if card.get_rank() not in ranks: #raises exception if the valid rank is not in the card of the deck
				raise Exception("Invalid rank")
			if card.get_suit() not in suits: #raises exception if the valid suit is not in the card of the deck
				raise Exception("Invalid suit")
			if len(card.get()) != 2: #raises exception if the card format is not 2
				raise Exception("Card Format Error") 
			if card.get() not in duplicate: #checks if duplicate is not there and appends it into duplicate list
				duplicate.append(card.get())
			else:
				raise Exception("Card Duplicated") #raises the exception
		return True


	def make_shoe(self):
		decks = []
		for i in range(6): #appends the created deck into the shoe decks
			decks.append(self.create_deck())
		for j in decks: #checks if each deck is a valid deck or raises exception
			vald = self.validate_deck(j)
			if not vald :
				raise Exception("Not a valid deck")
		for k in decks:
			shuffle(k) #shuffles the deck
		q1 = Queue() #creates new 3 queues
		q2 = Queue()
		q3 = Queue()
		for deck in decks:
			for card in deck:
				q1.enqueue(card)
			if q1.size() == 156: #stops enqueueing if the size is 156
				break 
		for deck in decks[3:6]:
			for card in deck:
				q2.enqueue(card)
			if q2.size() == 156: #enqueues the rest of decks until it hits 156 again
				break 
		for j in range(6):
			temp = []
			for i in range(26): #adds the enqueued q1 and q2 to temp list and the shuffle
				temp.append(q1.dequeue())
				temp.append(q2.dequeue())
			shuffle(temp)

			for i in temp:
				q3.enqueue(i)
		return q3
	
	def set_shoe(self, shoe):
		self.shoe = shoe #sets the self.shoe as shoe

	def deal(self): #dealer and player will be dealt with a dequeued card from the shoe
		self.player_card = self.shoe.dequeue() 
		self.dealer_card = self.shoe.dequeue()

	def reset_shoe(self):
		if self.shoe.size() < 52: #if the shoe size is less than 52, the rest will be enqueued to discard
			for i in range(self.shoe.size()):
				self.discard.enqueue(self.shoe.dequeue())
			#sets new queues
			q1 = Queue()
			q2 = Queue()
			q3 = Queue()
			while (not self.discard.isEmpty()): #puts discard card back to q1 and q2
				q1.enqueue(self.discard.dequeue())
				q2.enqueue(self.discard.dequeue())
			for j in range(6):
				temp = [] 
				for i in range(26): #adds the enqueued q1 and q2 to temp list and the shuffle
					temp.append(q1.dequeue())
					temp.append(q2.dequeue())
				shuffle(temp)

				for i in temp:
					q3.enqueue(i) #temp elements will be added to q3 and q3 will be set to shoe
			self.shoe = q3
			


