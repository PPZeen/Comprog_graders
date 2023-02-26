def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a
def is_coprime(a, b, c):
    return gcd(gcd(a,b),c)== 1
def primitive_Pythagorean_triples(max_len):
    triple = []
    for i in range(1,max_len+1):
        for j in range(i,max_len+1):
            for k in range(j,max_len+1):
                if is_coprime(i,j,k) and (i*i+j*j)==k*k:
                    triple.append([k,i,j])
    triple.sort()
    triple2 = [[i,j,k] for k,i,j in triple]
    return triple2
exec(input().strip())