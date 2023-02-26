x = input()
o = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
if x in o:
    print("Error")
else :
    if len(x) == 2 :
        x = int(x)
        if x == 1 or x == 2 or 20<=x<=40 or 51<=x<=58 :
            print("OK")
        else :
            print("Error")
    else :
        print("Error")