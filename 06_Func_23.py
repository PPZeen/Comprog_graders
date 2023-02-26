def make_int_list(x):
    x = [int(e) for e in x.split()]
    return x

def is_odd(e):
    return e%2 == 1

def odd_list(alist):
    List = []
    for e in alist :
        if e%2 == 1 : List.append(e)
    return List

def sum_square(alist):
    s = 0
    for e in alist :
        s += e**2
    return s

print(make_int_list('1 2 3 4 5'))
print(is_odd(3333))
print(odd_list([1,2,3,4,5,6,7]))
print(sum_square([1,1,2,3])) 
exec(input().strip()) 