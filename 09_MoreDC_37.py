major = {}
nmajor = int(input())
studentlist = []
ans = []
for i in range(nmajor):
    s = input().split()
    major[s[0]] = int(s[1])
nstudent = int(input())
for i in range(nstudent):
    s = input().split()
    studentlist.append([float(s[1]),s[0],s[2],s[3],s[4],s[5]])
studentlist.sort(reverse=1)
for e in studentlist:
    for k in range(2,6):
        if major[e[k]]>0:
            major[e[k]]-=1
            ans.append([e[1],e[k]])
            break
ans.sort()
for e in ans : print(e[0],e[1])