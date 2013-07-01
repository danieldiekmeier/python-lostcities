class Player():
	def __init__(self):
		return None
	def put(self, status):
		print '\nDANIEL AI 1\n'
		cards = status['cards']
		print cards

		# NEVER DISCARD
		location = 0

		done = False
		for number in xrange(1, 10):
			for card in cards:
				if cards[card] is not None:
					if cards[card].count(number):
						print number
						print 'ist am kleinsten und die farbe ist'
						print card
						color = card
						done = True
						break
			if done:
				break

		return {'location': int(location), 'color': str(color), 'number': int(number)}

	def draw(self, status):
		return {'location': 0, 'color': 'red'}
