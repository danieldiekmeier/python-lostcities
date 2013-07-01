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

		if status['left_in_deck'] > 10:
			range = xrange(1,11)
		else:
			range = xrange(10,0,-1)

		for number in range:
			for key in cards:
				if cards[key] is not None and cards[key].count(number):
						print str(key) + ' ' + str(number)
						color = key
						# check if card is playable
						if status['board'][color] == None or max(status['board'][color]) <= number:
							done = True
							break
			if done:
				print '\nDONE\n'
				break

		if not done:
			print "no matching card"
			print "discard lowest card"
			location = 1
			for number in xrange(1,11):
				for key in cards:
					if cards[key] is not None and cards[key].count(number):
						print str(key) + ' ' + str(number)
						color = key
						done = True
						break
				if done:
					print '\nDONE\n'
					break




		return {'location': int(location), 'color': str(color), 'number': int(number)}

	def draw(self, status):
		return {'location': 0, 'color': 'red'}
