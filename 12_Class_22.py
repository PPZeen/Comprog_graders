class Card:
    def __init__(self, value, suit):
        self.n = value
        self.s = suit

    def __str__(self):
        return "("+self.n +" "+ self.s+")"

    def getScore(self):
        c = 0
        if self.n in ["2","3","4","5","6","7","8","9","10"] : c += int(self.n)
        elif self.n == "A" : c += 1
        else : c += 10
        return c

    def sum(self, other):
        return (Card.getScore(self) + Card.getScore(other))%10
    
    def __lt__(self, rhs):
        su = ["club","diamond","heart","spade"]
        nu = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
        x = (int(nu.index(self.n)),int(su.index(self.s)))
        y = (int(nu.index(rhs.n)),int(su.index(rhs.s)))
        return x < y
    
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])