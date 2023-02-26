x = input()
l = ['a','e','i','o','u']
if x[-1] == 's' or x[-1] == 'x' or x[-2:] == 'ch' : x += 'es'
elif x[-1] == 'y' and x[-2] not in l : x = x[:-1] + 'ies'
else : x += 's'
print(x)