class Player():
	def __init__(self):
		return None
	def put(self, status):
		print status['cards']
		location = None
		color = None
		number = None
		print "Where to put card?\n0: Board / 1: Discard"
		while location != 0 and location != 1:
			location = int(raw_input("Location: "))
		while color not in status['colors']:
			color = raw_input("Color: ")

		number = raw_input("Number: ")
		return {'location': int(location), 'color': str(color), 'number': int(number)}

	def draw(self, status):
		print "Where to draw card from?\n0: Deck / 1: Discard"
		location = None
		color = None
		while location != 0 and location != 1:
			location = int(raw_input("Location: "))
		if location == 1:
			while color not in status['colors']:
				color = raw_input("Color: ")
		return {'location': location, 'color': color}