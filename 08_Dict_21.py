s = input().lower()
char = 'abcdefghijklmnopqrstuvwxyz'
count = {}
for e in range(len(char)) :
    count[char[e]] = 0
for i in range(len(s)) :
    if s[i] in char :
        count[s[i]] += 1
k =[]
for i in range(26) :
    k.append([(-1)*(count[char[i]]),char[i]])
k.sort()
for i in range(26) :
    if k[i][0] <0 :
        print(k[i][1],'->',-1*k[i][0])
