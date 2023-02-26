x = int(input())
sc1 , sc2 , n = 0,0,0
while sc1 != x and sc2 != x and n != 3*x :
    one,two = input().split()
    if one == "R" :
        if two == "S" : sc1 += 1
        elif two == "P" : sc2 += 1
    elif one == "S" :
        if two == "R" : sc2 += 1
        elif two == "P" : sc1 += 1
    elif one == "P" :
        if two == "R" : sc1 += 1
        elif two == "S" : sc2 += 1
    n += 1
print(str(sc1)+ " "+str(sc2))
if sc1 == sc2 : print("Tie")
if sc1 > sc2 : print("Player 1 wins")
elif sc2 > sc1 : print("Player 2 wins")