a = input().strip()
b = input().strip()
c = input().strip()
cou = open(a,'r')
tea = open(b,'r')
dat = open(c,'r')
course = {}
teacher = {}
for line in cou:
    s = line.strip().split(',')
    course[s[0]]=s[1]
for line in tea:
    s = line.strip().split(',')
    teacher[s[0]]=s[1]
for line in dat:
    a,b = line.strip().split(',')
    if a in course and b in teacher : print(course[a]+','+teacher[b])
    else : print('record error')