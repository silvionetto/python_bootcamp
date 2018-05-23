class Deck:
	
	def __init__(self):
		''' Create a deck in order '''
		self.deck = []
		for suit in suits:
			for rank in ranking:
				self.deck.append(Card(suit,rank))

	def shuffle(self):
		''' Shuffle the deck, python actually already has a shuflly method in its random lib '''
		random.shuflly(self.deck)

	def deal(self):
		''' Grab the first item in the deck '''
		single_card = self.deck.pop()
		return single_card