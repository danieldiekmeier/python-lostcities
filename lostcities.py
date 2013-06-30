# IMPORTS

from random import choice, shuffle

# CONFIG

colors = ['yellow', 'blue', 'white', 'green', 'red']

class Card:
	def __init__(self, color, number):
		self.color = color
		self.number = number
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		if self.number == 1:
			return self.color+' multiplicator'
		return self.color+' '+str(self.number)

class Player:
	def __init__(self):
		self.cards = []
		for n in xrange(0,8):
			self.draw()
		self.board = Board()
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		return str(self.score)+' points'
	def show_cards(self):
		return self.cards
	def score(self):
		return self.board.score()
	def put(self, card):
		self.board.put(card)
		self.draw()
	def draw(self):
		self.cards.append(deck.pop(0))

class Board:
	def __init__(self):
		self.columns = []
		for color in colors:
			self.columns.append(Column(color))
	def __repr__(self):
		return self.__str__()
	def __str__(self):
		return 'this is a board'
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
	def value(self):
		multiplicator = 1
		cards_value = 0
		for card in self.cards:
			if card.number == 1:
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

# SETUP CARDS

numbers = [1, 1]
numbers.extend(range(1,11))

# SETUP DECK

deck = []

for color in colors:
	for number in numbers:
		deck.append(Card(color, number))

shuffle(deck)

# CREATE THE TWO PLAYERS WITH THE DECK
user = Player()
computer = Player()

print user.show_cards()
print computer.show_cards()

print user.score()

user.put(user.cards.pop(0))

print user.score()