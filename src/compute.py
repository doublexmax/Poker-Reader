from utils import *
from itertools import combinations

"""
1. Get cards (each player & community)
2. Calculate equity of each through monte carlo + optimization
"""

def evaluate(*cards, community = []):
	"""
	Cards come in format ("Xt","Yq") with X and Y representing the card value (2..."A") and t and q representing the suit (["s","c","h","d"])
	"""

	availableCards = ['2s', '2d', '2h', '2c', '3s', '3d', '3h', '3c', '4s', '4d', '4h', '4c', '5s', '5d', '5h', '5c', \
				'6s', '6d', '6h', '6c', '7s', '7d', '7h', '7c', '8s', '8d', '8h', '8c', '9s', '9d', '9h', '9c', \
				'10s', '10d', '10h', '10c', '11s', '11d', '11h', '11c', '12s', '12d', '12h', '12c', \
				'13s', '13d', '13h', '13c', '14s', '14d', '14h', '14c']

	parsedCards = []
	for card in cards:
		cardOne = card[0]
		cardTwo = card[1]

		cardOneVal = convertToNum(cardOne[:-1])
		cardOneSuit = convertToWeight(cardOne[-1])

		cardTwoVal = convertToNum(cardTwo[:-1])
		cardTwoSuit = convertToWeight(cardTwo[-1])

		parsedCards.append((cardOneVal, cardOneSuit, cardTwoVal, cardTwoSuit))

		availableCards.remove(str(cardOneVal) + cardOneSuit)
		availableCards.remove(str(cardTwoVal) + cardTwoSuit)

	communityCardsParsed = []
	for card in community:
		cardVal = convertToNum(card[:-1])
		cardWeight = convertToWeight(card[-1])

		communityCardsParsed.append((cardVal, cardWeight))

		availableCards.remove(str(cardVal) + cardWeight)

	book = {}

	print(parsedCards, communityCardsParsed, availableCards)

	equity = calculate_equity(parsedCards, communityCardsParsed, availableCards, book = book)
	print(equity)
	print(book)


def calculate_equity(cards, community, available, book = {}):
	"""
	card comes as: (X, t, Y, q)
	"""
	if len(community) == 5:
		bestHands = {}
		winner = (0,(0,))
		winners = []

		for i, player in enumerate(cards):
			highHand = (0,(0,))
			suits = list(combinations([convertToWeight(player[1]), convertToWeight(player[3]), \
									convertToWeight(community[0][1]), convertToWeight(community[1][1]), convertToWeight(community[2][1]), \
									convertToWeight(community[3][1]), convertToWeight(community[4][1]) \
									], 5))
			combos = list(combinations([convertToNum(player[0]), convertToNum(player[2]), \
									convertToNum(community[0][0]), convertToNum(community[1][0]), convertToNum(community[2][0]), \
									convertToNum(community[3][0]), convertToNum(community[4][0]) \
									], 5))

			#print(suits)

			for j, combo in enumerate(combos):
				handValue = highestHand(combo, suits[j])

				if compare(highHand, handValue) == -1:
					highHand = handValue

			bestHands[i] = highHand

		for x in bestHands:
			if compare(winner, bestHands[x]) == -1:
				winners = [x]
				winner = bestHands[x]
			elif compare(winner, bestHands[x]) == 0:
				winners.append(x)

		for player in winners:
			book[player] = book.get(player, 0) + 1
			if player == 0:
				print(bestHands[0])

		return book

	else:
		for card in available:
			#print(list(filter(lambda x: x[-1] != card[-1] and x[:-1] != card[:-1], available)))
			print(calculate_equity(cards, community + [(card[:-1], card[-1])], \
				list(filter(lambda x: x[-1] != card[-1] or x[:-1] != card[:-1], available)), book))

def highestHand(cards, suits):
	lastSuit = suits[0]
	highCard = max(cards)
	flush = True

	for i in range(1,len(suits)):
		if lastSuit != suits[i]:
			flush = False
			break

	occurrences = {}

	if flush:
		straight_check = 0
		straight_mult = 1
		for card in cards:
			straight_check = straight_check + card * straight_mult
			straight_mult = straight_mult * -1

		if straight_check % 2 == 0:
			return (8, (highCard,))

		return (5, (highCard,))

	straight_max = 0
	straight_min = 15
	for card in cards:
		straight_max = max(straight_max, card)
		straight_min = min(straight_min, card)

		if card in occurrences:
			occurrences[card] += 1
		else:
			occurrences[card] = 1


	quads = False
	trips = False
	pairs = []

	for card in occurrences:
		count = occurrences[card]

		if count == 4:
			# any quads is the best
			for x in cards:
				if x != card:
					return (7, (card, x))
		elif count == 3:
			trips = card
		elif count == 2:
			pairs.append(card)

	# full house
	if trips and len(pairs):
		return (6, (trips, (max(pairs),)))

	# straight
	if straight_max - straight_min == 4:
		return (4, (highCard,))

	if trips:
		for i, x in enumerate(cards):
			for j in range(i+1, len(cards)):
				if x != trips and cards[j] != trips:
					if x > cards[j]:
						return (3, (trips, x, cards[j]))
					else:
						return (3, (trips, cards[j], x))

	if len(pairs) == 2:
		for card in cards:
			if card != pairs[0] and card != pairs[1]:
				if pairs[0] > pairs[1]:
					return (2, (pairs[0], pairs[1], card))
				else:
					return (2, (pairs[1], pairs[0], card))

	if len(pairs) == 1:
		missingCards = filter(lambda x: x != pairs[0], cards)
		return (2, sorted(missingCards, reverse = True))
	
	return (0, sorted(cards, reverse = True))

def compare(handOne, handTwo):
	if handOne[0] > handTwo[0]:
		return 1
	elif handOne[0] == handTwo[0]:
		if handOne[1][0] > handTwo[1][0]:
			return 1
		elif handOne[1][0] == handTwo[1][0]:
			try:
				if handOne[1][1] > handTwo[1][1]:
					return 1
				elif handOne[1][1] == handTwo[1][1]:
					if handOne[1][2] > handTwo[1][2]:
						return 1
					elif handOne[1][2] == handTwo[1][2]:
						if handOne[1][3] > handTwo[1][3]:
							return 1
						elif handOne[1][3] == handTwo[1][3]:
							if handOne[1][4] > handTwo[1][4]:
								return 1
							elif handOne[1][4] == handTwo[1][4]:
								return 0
			except Exception:
				return 0

	return -1