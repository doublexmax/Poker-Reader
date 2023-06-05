global card_values, suit_weight
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, "J": 11, "Q": 12, "K": 13, "A": 14}
suit_weight = {"s": 4, "h": 3, "d": 2, "c": 1}

def convertToNum(val):
	if isinstance(val, int):
		return val
		
	if isinstance(val, str) and val.isnumeric():
		return int(val)

	return card_values[val]

def convertToWeight(suit):
	return suit