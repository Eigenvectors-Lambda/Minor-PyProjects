import itertools, random

deck= list(itertools.product([1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King"],['Spades','Hearts','Diamonds','Clubs']))

random.shuffle(deck)

print("Combination is:")

start_Number=5
for i in range(start_Number):
    print(deck[i][0], "of",deck[i][1])