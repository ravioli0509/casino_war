from Card import Card
from Player import Player
from Table import Table
from CQ import Queue

def test_card():
	#Creates a card which is the Ace of Diamonds
	my_card = Card("A", "D")
	
	#tests get function
	assert my_card.get() == "AD", "Invalid card"
	#tests rank function
	assert my_card.get_rank() == "A", "Invalid rank"
	#tests suit function
	assert my_card.get_suit() == "D", "Invalid suit"
	
	#tests a rank convertion function
	assert my_card.convert_rank("A") == 14, "Invalid conversion"
	assert my_card.convert_rank("K") == 13, "Invalid conversion"
	assert my_card.convert_rank("Q") == 12, "Invalid conversion"
	assert my_card.convert_rank("J") == 11, "Invalid conversion"
	assert my_card.convert_rank("T") == 10, "Invalid conversion"
	assert my_card.convert_rank("9") == 9, "Invalid conversion"
	assert my_card.convert_rank("8") == 8, "Invalid conversion"
	assert my_card.convert_rank("7") == 7, "Invalid conversion"
	assert my_card.convert_rank("6") == 6, "Invalid conversion"
	assert my_card.convert_rank("5") == 5, "Invalid conversion"
	assert my_card.convert_rank("4") == 4, "Invalid conversion"
	assert my_card.convert_rank("3") == 3, "Invalid conversion"
	assert my_card.convert_rank("2") == 2, "Invalid conversion"
	
	#tests that the suit has no influence on comparison __eq__
	assert Card("A","D") == Card("A","S") == Card("A","H") == Card("A","C"), "Invalid comparison =="
	
	#tests rank comparison function _gt__
	assert Card("A","H") > Card("K", "H") > Card("2", "S"), "Invalid comparison >"
	
	#tests the __str__ function
	assert str(my_card) == "AD", "Invalid string"
	
	#returns True to sinalize that it has passed all tests	
	return True

def test_player():
	player = Player()
	#test to add chips
	assert player.add_chips(3) == 3, "Invalid input"
	#test to get chips 
	assert player.get_chips() == 3, "Invalid input"
	#returns True to sinalize that it has passed all tests	
	return True


def test_table():
	table = Table()
	#test to resolve round 
	A = Card("A","S")
	B = Card("8","H")
	C = Card("8","C")
	assert table.resolve_round(A,B) == 1
	assert table.resolve_round(B,A) == -1
	assert table.resolve_round(B,C) == 0
	#test to get_bet
	table.set_bet(100) 
	assert table.get_bet() == "100", "Invalid Bet"
	#test to create deck by checking if the type is a list
	deck = table.create_deck() 
	assert type(deck) == list , "Invalid Type"
	#test to validate_deck 
	assert table.validate_deck(deck) == True , "Invalid Validation"
	#test to make_shoe by checking if the tyoe is a queue
	queue = table.make_shoe() 
	assert type(queue) == Queue, "Invalid shoe"



