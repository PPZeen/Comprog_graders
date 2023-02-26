class Card:
    def __init__(self, value, suit):
        self.val = value
        self.suit = suit
    def __str__(self):
        return '(' + self.val + ' ' + self.suit + ')'
    def next1(self):
        sortscore = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        sortsuit = ['club','diamond','heart','spade']
        if self.suit == 'spade':
            suit = 'club'
            if self.val == '2': val = '3'
            else : val = sortscore[sortscore.index(self.val)+1]
        else :
            k = sortsuit.index(self.suit)
            suit = sortsuit[k+1]
            val = self.val
        return Card(val,suit)
    def next2(self):
        nexttt = self.next1()
        self.val = nexttt.val
        self.suit = nexttt.suit
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])