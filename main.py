#This game is created by Ravindu Cooray as a part of
#the assignment given from a Computing Class in University of Alberta

from Player import Player
from Table import Table
from Card import Card
import random
import time

#global variables of the statistics to show the numbers every time the player quits 
number_hands = 0
total_bet = 0
total_profit = 0
win_count = 0
war_count = 0

def main():	
	print("Welcome to Casino War") 
	player = Player() 
	table = Table()
	table.set_shoe(table.make_shoe()) 
	#every time the game starts, shoe is made as the table class sets it
	running = True
	while running:
		print("You currently have "+str(player.get_chips())+" chips.")
		print("What would you like to do?\n")
		print("Play (P)")
		print("Buy Chips (B)")
		prompt = input("Quit (Q) : ").upper()
		if prompt == "Q":	
			#autoplay will data will be stored into temp. Every time statistics are displayed,
			#the program will reach into temp, which the global variables are stored in list form
			temp = auto_play(prompt,0,player,table) #autoplay takes prompt 
			print("Played "+str(temp[0])+" hands.")
			print("The Average bet was "+str(round(temp[1],2))+" chips")
			print("The Average profit of the session was "+str(round(temp[2],2))+".")
			print("Player won "+str(temp[3])+" out of "+str(temp[0])+" hands, or "+str(round(temp[4],2))+"%")
			print("The war count was "+str(temp[5])+".")
			print("Goodbye")
			#round(temp[i],2) will be used to round the numbers into 2 decimal format
			break
		elif prompt == "B":
			prompt2 = int(input("How many chips would you like to buy? (1-1000) :"))
			if prompt2 > 1000 or prompt2 < 1: #to check if the player input is between 1 and 1000
				print("Invalid transaction, a number between 1 and 1000 should be inserted.")
				print("Returning to the main menu\n") #goes back to the main menu if the input is out of bounds
			else:
				auto_play(prompt,prompt2,player,table)	#autoplay includes prompt2 now
		elif prompt == "P":
			print("Place your bet!")
			prompt2 = int(input("The bet should be an even number 2-100: "))
			if prompt2 > 100: #checks if the player input is greater than 100
				print("Bet is too large\n")
				print("Returning to the Menu")
				continue
			if prompt2 < 2: #checks if the player input is less than 1 
				print("Bet is too small\n")
				print("Returning to the Menu")
				continue
			if prompt2 % 2 != 0 : #checks if the player input is an even integer by checking the modulo
				print("Bet is odd, should be even\n")
				print("Returning to the Menu")
				continue
			print("No more bets!")
			auto_play(prompt,prompt2,player,table) #autoplay intakes prompt2 from the betting input
		else:
			print("Invalid Entry")

def auto_play(action,amount = 0,player = 0,table=0):
	#calling the global variables 
	global number_hands 
	global total_bet 
	global total_profit
	global win_count
	global war_count
	if action == "Q":	
		if number_hands == 0: #returns all the statistics of the game to 0, if the number of hands is 0
			return[0,0,0,0,0,0]
		else:	#returns the statistics in normally	
			return [number_hands, total_bet/number_hands , total_profit/number_hands, win_count, win_count/number_hands * 100 , war_count]
	elif action == "B": 
		player.add_chips(amount) #adds chip by the amount depending on the player input
		return True
	elif action == "P": 
		if player.get_chips() >= amount: #play function will work if the player has enough chips to bet
			number_hands += 1
			total_bet += amount
			table.reset_shoe() 
			table.set_bet(amount)
			table.deal()
			resolve = table.resolve_round(table.player_card,table.dealer_card)
			if resolve == 1: #total bet, win count and total profit will be increased if the resolve was 1
				time.sleep(random.randint(0,1))
				total_profit += amount
				win_count += 1
				player.add_chips(amount)
			elif resolve == -1: #total bet, win count and total profit will be decreased if the resolve was -1
				time.sleep(random.randint(0,1))
				total_profit -= amount
				player.remove_chips(amount)
			elif resolve == 0: #war count will be added if the resolve was 0
				time.sleep(random.randint(0,1))
				war_count += 1
				if player.get_chips() >= 2*amount: #checking if player has the right amount to go to war 
					#(more than 2*amount)
					print("We are going to war! You doubled up your bet.")
					print("We are burning 3 cards\n")
					for i in range(3): #in war, 3 cards will be burned from the shoe and enqueued to discard queue
						table.discard.enqueue(table.shoe.dequeue())
					#clears the table and new cards will be dealt 
					table.clear() 
					table.deal()
					war_resolve = table.resolve_round(table.player_card,table.dealer_card)
					if war_resolve >= 0: #play will win if the resolve is 1 or 0. So the profit will be increased
						total_profit += amount 
						player.add_chips(amount)
					else: #player will lose 2*amount if the dealer wins with resolve = -1
						total_profit -= 2*amount 
						player.remove_chips(2*amount)
				else: #If the player don't have enough chips, the player will surrender with profit decreased with half of the amount bet
					print("You didn't have enough chips, so you surrendered")
					total_profit -= amount/2
					player.remove_chips(amount/2)
			return player.get_chips()
		else:
			print("Not Enough Chips!")



if __name__ == "__main__":
 
	main()
