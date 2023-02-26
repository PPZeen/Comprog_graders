def no_lowercase(t):
    l = "abcdefghijklmnopqrstuvwxyz"
    check = True
    for e in t :
        if e in l :
            check = False
            break
    return check
        
def no_uppercase(t):
    l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    check = True
    for e in t :
        if e in l :
            check = False
            break
    return check

def no_number(t):
    l = "0123456789"
    check = True
    for e in t :
        if e in l :
            check = False
            break
    return check
    
def no_symbol(t):
    l = "฿!@#$%^&*()_+=][}{';\":/?.,><|\\"
    check = True
    for e in t :
        if e in l :
            check = False
            break
    return check
def character_repetition(t):
    check = False
    for i in range(len(t)-3) :
        if t[i] == t[i+1] and t[i] == t[i+2] and t[i] == t[i+3] :
            check = True
            break
    return check
def number_sequence(t):
    l = "0123456789012,9876543210987"
    check = False
    for i in range(len(t)-3) :
        if t[i:i+4] in l :
            check = True
    return check
def letter_sequence(t):
    T = t.lower()
    l = "abcdefghijklmnopqrstuvwxyzabc,zyxwvutsrqponmlkjihgfedcbazyx"
    check = False
    for i in range(len(T)-3) :
        if T[i:i+4] in l :
            check = True
    return check    
    
def keyboard_pattern(t):
    T = t.lower()
    l1 = "!@#$%^&*()_+!@#,+_)(*&^%$#@!+_"
    l2 = "qwertyuiopqwe,poiuytrewqpoi"
    l3 = "asdfghjklasd,lkjhgfdsalkj"
    l4 = "zxcvbnmzxc,mnbvcxzmnb"
    L = l1+l2+l3+l4
    check = False
    for i in range(len(T)-3) :
        if T[i:i+4] in L :
            check = True
    return check 
#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8 :
    errors.append("Less than 8 characters")
if no_lowercase(passw) :
    errors.append("No lowercase letters")
if no_uppercase(passw) :
    errors.append("No uppercase letters")
if no_number(passw) :
    errors.append("No numbers")
if no_symbol(passw) :
    errors.append("No symbols")
if character_repetition(passw) :
    errors.append("Character repetition")
if number_sequence(passw) :
    errors.append("Number sequence")
if letter_sequence(passw) :
    errors.append("Letter sequence")
if keyboard_pattern(passw) :
    errors.append("Keyboard pattern")
if len(errors) == 0 : print("OK")
else : print("\n".join(errors))