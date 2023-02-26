def knows(R,x,y):
    return y in R[x]
def is_celeb(R,x):
    if len(R[x])==0 or (len(R[x])==1 and x in R[x]) :
        for e in R:
            if e!=x and x not in R[e] : return False
        return True
    return False
def find_celeb(R):
    for e in R:
        if is_celeb(R,e): return e
    return None
def read_relations() :
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1 : break
        if d[0] not in R: R[d[0]] = set()
        if d[1] not in R: R[d[1]] = set()
        R[d[0]].add(d[1])
    return R
def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)
exec(input().strip())