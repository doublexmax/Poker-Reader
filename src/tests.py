from compute import *

def runTests():
	highHandTests()

	handComparisonTests()

def highHandTests():
	print(royalFlushTests())
	print(straightFlushTests())
	print(quadsTests())
	print(fullHouseTests())
	print(flushTests())
	print(straightTests())
	print(threeOfAKindTests())
	print(twoPairTests())
	print(onePairTests())
	print(highCardTests())

def handComparisonTests():
	pass

def royalFlushTests():
	royalFlushes = [([14,13,12,10,11], [1,1,1,1,1]),
					([14,13,12,10,11], [2,2,2,2,2]),
					([14,13,12,10,11], [3,3,3,3,3]),
					([14,13,12,10,11], [4,4,4,4,4]),]

	for royalFlush in royalFlushes:
		parsed = highestHand(royalFlush[0], royalFlush[1])

		assert parsed == (9,(14,))

	return "Royal Flush tests passed successfully."

def straightFlushTests():
	straightFlushes = [([13,12,10,11,9], [2,2,2,2,2]),
						([13,12,10,11,9], [1,1,1,1,1]),
						([13,12,10,11,9], [3,3,3,3,3]),
						([13,12,10,11,9], [4,4,4,4,4]),
						([12,10,11,9,8], [2,2,2,2,2]),
						([11,10,9,8,7], [2,2,2,2,2]),
						([10,8,7,6,9], [2,2,2,2,2]),
						([9,7,6,5,8], [2,2,2,2,2]),
						([4,5,7,6,8], [2,2,2,2,2]),
						([7,5,3,4,6], [2,2,2,2,2]),
						([2,6,5,4,3], [2,2,2,2,2]),
						([1,2,3,4,5], [2,2,2,2,2]),
						([3,4,5,2,1], [1,1,1,1,1])]

	for straightFlush in straightFlushes:

		parsed = highestHand(straightFlush[0], straightFlush[1])

		assert parsed == (8,(max(straightFlush[0]),))

	return "Straight Flush tests passed successfully."

def quadsTests():
	quads = [([9,9,9,3,9], [1,3,2,1,4]),
				([8,8,8,4,8], [1,3,2,1,4]),
				([7,7,3,7,7], [1,3,2,2,4]),
				([5,6,6,6,6], [1,3,2,1,4]),
				([13,13,13,13,2], [1,3,2,4,4]),
				([11,11,11,11,3], [1,3,2,4,4])]

	for quad in quads:
		parsed = highestHand(quad[0], quad[1])

		assert parsed == (7, (max(quad[0]),min(quad[0])))

	return "4 of a kind tests passed successfully."

def fullHouseTests():
	fullHouses = [([3,3,3,2,2],[1,2,3,1,2]),
					([2,2,2,3,3],[1,2,3,1,2]),
					([13,13,13,2,2],[1,2,3,1,2]),
					([3,3,3,12,12],[1,2,3,1,2]),
					([3,3,3,2,2],[1,2,3,1,2])]

	for fullHouse in fullHouses:

		parsed = highestHand(fullHouse[0], fullHouse[1])

		assert parsed == (6,(fullHouse[0][0], fullHouse[0][4])), fullHouse

	return "Full house tests passed successfully."

def flushTests():
	flushes = [([3,4,2,6,7], [3,3,3,3,3]),
				([3,4,2,6,7], [4,4,4,4,4]),
				([3,4,2,6,7], [2,2,2,2,2]),
				([3,4,2,6,7], [1,1,1,1,1]),
				([6,4,2,6,8], [3,3,3,3,3]),
				([8,4,2,6,9], [3,3,3,3,3]),
				([7,4,2,6,10], [3,3,3,3,3]),
				([5,4,2,6,11], [3,3,3,3,3]),
				([3,9,2,6,12], [3,3,3,3,3]),
				([3,5,2,6,13], [3,3,3,3,3])]

	for flush in flushes:

		parsed = highestHand(flush[0], flush[1])

		assert parsed == (5,(max(flush[0]),)), flush

	return "Flush tests passed successfully."

def straightTests():
	straights = [([4,5,6,7,8], [1,2,3,1,2]),
					([3,4,5,6,7], [1,2,3,1,2]),
					([2,3,4,5,6], [1,2,3,1,2]),
					([1,2,3,4,5], [1,2,3,1,1]),
					([5,6,7,8,9], [3,2,3,4,4]),
					([6,7,8,9,10], [3,3,3,1,2]),
					([7,8,9,10,11], [4,4,3,1,2]),
					([8,9,10,11,12], [1,2,4,1,2]),
					([9,10,11,12,13], [1,2,3,2,2])]

	for straight in straights:
		parsed = highestHand(straight[0], straight[1])

		assert parsed == (4,(max(straight[0]),)), straight

	return "Straight tests passed successfully."

def threeOfAKindTests():
	threeOfAKinds = [([4,4,4,9,2], [1,3,2,3,3]),
						([5,5,5,4,2], [1,3,2,3,3]),
						([6,6,6,9,3], [1,3,2,3,3]),
						([7,7,7,9,2], [1,3,2,3,3]),
						([8,8,8,9,2], [1,3,2,3,3]),
						([9,9,9,10,2], [1,3,2,3,3]),
						([10,10,10,9,2], [1,3,2,3,3]),
						([11,11,11,9,2], [1,3,2,3,3]),
						([12,12,12,9,2], [1,3,2,3,3]),
						([13,13,13,9,2], [1,3,2,3,3]),
						([2,2,2,9,4], [1,3,2,3,3]),
						([3,3,3,9,4], [1,3,2,3,3])]

	for threeOfAKind in threeOfAKinds:

		parsed = highestHand(threeOfAKind[0], threeOfAKind[1])

		assert parsed == (3,(threeOfAKind[0][0], threeOfAKind[0][3], threeOfAKind[0][4])), threeOfAKind

	return "Three of a kind tests passed successfully."

def twoPairTests():
	twoPairs = [([9,9,5,5,6], [1,2,3,4,3]),
				([10,10,5,5,6], [1,2,3,1,1]),
				([13,13,7,7,4], [1,2,3,4,2]),
				([12,12,4,4,6], [1,2,3,4,1]),
				([11,11,3,3,6], [3,2,3,4,3]),
				([10,10,5,5,6], [1,4,3,4,3]),
				([9,9,8,8,3], [1,2,3,4,3]),
				([8,8,2,2,3], [1,2,3,4,3]),
				([7,7,3,3,4], [2,1,1,4,1]),
				([6,6,5,5,10], [1,2,3,4,3]),
				([5,5,4,4,13], [1,2,3,4,4]),
				([4,4,2,2,9], [1,2,3,4,4]),
				([3,3,2,2,4], [1,3,3,4,3])]

	for twoPair in twoPairs:

		parsed = highestHand(twoPair[0], twoPair[1])

		assert parsed == (2,(twoPair[0][0], twoPair[0][2],twoPair[0][4])), twoPair

	return "Two pair tests passed successfully."

def onePairTests():
	onePairs = [([8,8,10,9,3], [3,4,4,4,2]),
				([7,7,8,4,2], [3,4,4,4,2]),
				([6,6,5,3,2], [3,4,4,4,2]),
				([5,5,10,9,8], [3,4,4,4,2]),
				([4,4,11,7,6], [3,4,4,4,2]),
				([3,3,11,10,9], [3,4,4,4,2]),
				([2,2,10,9,8], [3,4,4,4,2]),
				([9,9,7,6,2], [3,4,4,4,2]),
				([10,10,9,3,2], [3,4,4,4,2]),
				([11,11,8,5,4], [3,4,4,4,2]),
				([12,12,11,10,9], [3,4,4,4,2]),
				([13,13,7,6,5], [3,4,4,4,2])]

	for onePair in onePairs:

		parsed = highestHand(onePair[0], onePair[1])

		assert parsed == (1,[onePair[0][0], onePair[0][2], onePair[0][3], onePair[0][4]]), ("Hand:", onePair, "Evaluated to:", parsed)

	return "One pair tests passed successfully."

def highCardTests():
	highCards = [([13,12,11,10,8], [1,2,3,1,2]),
				([12,11,10,8,3], [1,2,3,1,2]),
				([11,9,5,4,3], [1,2,3,1,2]),
				([10,8,7,6,5], [1,2,3,1,2]),
				([9,5,4,3,2], [1,2,3,1,2]),
				([8,7,4,3,2], [1,2,3,1,2]),
				([7,6,4,3,2], [1,2,3,1,2])]

	for highCard in highCards:

		parsed = highestHand(highCard[0], highCard[1])

		assert parsed == (0,highCard[0])

	return "High card tests passed successfully."


if __name__ == '__main__':
	runTests()