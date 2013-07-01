# IMPORTS

from random import choice, shuffle

#from lcinput import Player as Player0
from danielai1 import Player as Player0
from danielai1 import Player as Player1

# CONFIG

COLORS = ('yellow', 'blue', 'white', 'green', 'red')

NUMBERS = [1, 1]
NUMBERS.extend(range(1,11))
MULTIPLICATOR_NUMBER = 1


class Card:
	def __init__(self, color, number):
		self.color = color
		self.number = number
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		if self.number == MULTIPLICATOR_NUMBER:
			return self.color + ' multiplicator'
		return self.color + ' ' + str(self.number)

class Player:
	def __init__(self, brain):
		self.cards = []
		for n in xrange(0,8):
			self.draw()
		self.board = Board()
		self.brain = brain
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		return str(self.score) + ' points'
	def show_cards(self):
		cards = dict()
		for color in COLORS:
			cards[color] = []
		for card in self.cards:
			cards[card.color].append(card.number)
		for key in cards:
			if cards[key] == []:
				cards[key] = None
		return cards
	def score(self):
		return self.board.score()
	def put(self, card):
		self.board.put(card)
		self.cards.pop(self.cards.index(card))
	def draw(self):
		self.cards.append(deck.pop(0))
	def pickup(self, color):
		self.cards.append(discardpile.draw(color))
	def discard(self, card):
		discardpile.put(card)
		self.cards.remove(card)

class Board:
	def __init__(self):
		self.columns = []
		for color in COLORS:
			self.columns.append(Column(color))
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		return self.columns
	def show(self):
		columns = dict()
		for column in self.columns:
			columns[column.color] = column.show()
		return columns
	def score(self):
		score = 0
		for column in self.columns:
			score += column.value()
		return score
	def put(self, card):
		for column in self.columns:
			if column.color == card.color:
				column.put(card)
		return True

class Column:
	def __init__(self, color):
		self.color = color
		self.cards = []
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		return str(self.value()) + ' points'
	def show(self):
		if len(self.cards):
			cards = []
			for card in self.cards:
				cards.append(card.number)
			return cards
		return None
	def value(self):
		multiplicator = 1
		cards_value = 0
		for card in self.cards:
			if card.number == MULTIPLICATOR_NUMBER:
				multiplicator += 1
			else:
				cards_value += card.number
		if len(self.cards):
			value = multiplicator * -20
			value += multiplicator * cards_value
			return value
		return 0
	def put(self, card):
		self.cards.append(card)

class DiscardPile:
	def __init__(self):
		self.stacks = []
		for color in COLORS:
			self.stacks.append(Stack(color))
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		cards_in_stacks = []
		for stack in self.stacks:
			cards_in_stacks.append(stack.peek())
		return str(cards_in_stacks)
		# better repr/str later
	def draw(self, color):
		for stack in self.stacks:
			if stack.color == color:
				return stack.draw()
	def put(self, card):
		for stack in self.stacks:
			if stack.color == card.color:
				stack.put(card)
		return True
	def show(self):
		stacks = dict()
		for stack in self.stacks:
			stacks[stack.color] = stack.show()
		return stacks

class Stack:
	def __init__(self, color):
		self.color = color
		self.cards = []
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		return 'this is the' + self.color + 'stack'
	def draw(self):
		return self.cards.pop()
	def put(self, card):
		self.cards.append(card)
	def peek(self):
		return self.cards[-1] if len(self.cards) else None
	def show(self):
		return self.cards[-1].number if len(self.cards) else None

def status():
	not_current_player = players[1] if current_player == players[0] else players[0]
	return {'cards': current_player.show_cards(), 'board': current_player.board.show(), 'opponent_board': not_current_player.board.show(), 'discardpile': discardpile.show(), 'left_in_deck': len(deck), 'colors': COLORS}


# SETUP DECK

deck = []

for color in COLORS:
	for number in NUMBERS:
		deck.append(Card(color, number))

shuffle(deck)

# CREATE THE TWO players WITH THE DECK
players = (Player(Player0()), Player(Player1()))

# CREATE THE DISCARD PILE
discardpile = DiscardPile()

current_player = choice(players)

while len(deck):
	# THE GAME
	not_current_player = players[1] if current_player == players[0] else players[0]

	# ENTSCHEIDEN, WAS GELEGT WIRD
	put_decision = current_player.brain.put(status())
	for card in current_player.cards:
		if card.color == put_decision['color'] and card.number == put_decision['number']:
			current_card = card
			break
	if put_decision['location'] == 0:
		print current_card
		current_player.put(current_card)
	elif put_decision['location'] == 1:
		current_player.discard(current_card)
	else:
		print 'Not Valid'


	# ENTSCHEIDEN, WAS GEZOGEN WIRD
	draw_decision = current_player.brain.draw(status())
	if draw_decision['location'] == 0:
		current_player.draw()
	elif draw_decision['location'] == 1:
		current_player.pickup(draw_decision['color'])
	else:
		print 'Not Valid'

	# STUFF
	print 'Score:' + str(current_player.score())
	print ''
	print 'BOARD:'
	print current_player.board.show()
	print 'OTHER BOARD:'
	print not_current_player.board.show()
	print 'DISCARD:'
	print discardpile.show()
	print 'LEFT ON DECK'
	print len(deck)
	print ''

	# ANDERER SPIELER IST DRAN
	current_player = players[1] if current_player == players[0] else players[0]

print 'Final Score:'
print 'Player 1: ' + str(players[0].score())
print 'Player 2: ' + str(players[1].score())
