import itertools, random

deck = list(itertools.product(range(1,14), ["Spade", "Heart", "Dimond", "Club"]))

random.shuffle(deck)

print("You got: \n")
for i in range(5):
    print(deck[i][0]," of ", deck[i][1],"\n")