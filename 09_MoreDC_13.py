win = []
lose = []
for i in range(int(input())) :
    x = input().split()
    win.append(x[0])
    lose.append(x[1])
print(sorted(list(set(win)-set(lose))))