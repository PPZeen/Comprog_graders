def is_prime(n):
    if n <= 1:
         return False
    for k in range(2,int(n**0.5)+1):
         if n%k == 0:
             return False
    return True

def next_prime(N) :
    k = 1
    while True :
        if is_prime(N+k) == True : break
        else : k += 1
    return N+k

def next_twin_prime(N):
    k = 1
    s = []
    while True :
        if is_prime(N+k) == True :
            s.append(N+k)
            if len(s) >= 2 :
                if s[-1] == s[-2]+2 :
                    y = (s[-2],s[-1])
                    break
                else : k += 1
            else : k += 1
        else : k += 1        
    return y


exec(input().strip()) 