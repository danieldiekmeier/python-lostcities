class Player():
	def __init__(self):
		return None
	def put(self, status):
		print status['cards']
		print "Where to put card?\n0: Board\n1: Discard"
		location = raw_input("Location: ")
		color = raw_input("Color: ")
		number = raw_input("Number: ")
		return {'location': int(location), 'color': str(color), 'number': int(number)}

	def draw(self, status):
		return {'location': 0, 'color': 'red'}
