def factor(N) :
    ans = []
    for i in range(2,N+1) :
        y = N%i
        if y != 0 : pass
        elif y == 0 :
            k = 1
            while True :
                z = N/i
                if z%i == 0 :
                    k +=1
                    N = z
                else :
                    ans.append([i,k])
                    break
            N = z
        if N == 1 : break
    return ans
print(factor(3))
print(factor(200))
print(factor(3298402))
print(factor(8137740897))