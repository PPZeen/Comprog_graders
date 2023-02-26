def rot_13(x) :
    rot = "abcdefghijklmnopqrstuvwxyzabcdefghijklm"
    Rot = rot.upper()
    y = ""
    for i in range(len(x)) :
        if x[i] in rot : y += rot[rot.index(x[i])+13]
        elif x[i] in Rot : y += Rot[Rot.index(x[i])+13]
        else : y += x[i]
    return y
y = ""
while True :
    x = input()
    if x == "end" : break
    y += rot_13(x) + "\n"
print(y)

    
    