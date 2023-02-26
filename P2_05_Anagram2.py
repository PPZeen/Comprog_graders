char = 'abcdefghijklmnopqrstuvwxyz'
def countchar(stt):
    st=stt.lower()
    p={}
    ll=[]
    for e in char :
        p[e]=0
    for e in st:
        if e in p : p[e]+=1
    for e in p:
        ll.append([e,p[e]])
    ll.sort()
    return ll
def printans(ans1):
    for i in range(len(ans1)):
        if ans1[i][1]>1 :
            print(" - remove "+str(ans1[i][1])+" "+ans1[i][0]+"'s")
        else : print(" - remove "+str(ans1[i][1])+" "+ans1[i][0])
st1 = input()
st2 = input()
char1 = countchar(st1)
char2 = countchar(st2)
ans1 = []
ans2 = []
for i in range(26):
    if char1[i][1] > char2[i][1]:
        ans1.append([char1[i][0],char1[i][1]-char2[i][1]])
    if char1[i][1] < char2[i][1]:
        ans2.append([char2[i][0],-(char1[i][1]-char2[i][1])])
print(st1)
if len(ans1) == 0 : print(" - None")
printans(ans1)
print(st2)
if len(ans2) == 0 : print(" - None")
printans(ans2)