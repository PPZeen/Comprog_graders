filename = input().strip()
cmd = input().strip()
if cmd not in ['LSTRIP','RSTRIP','STRIP','STRIP_ALL']:
    print('Invalid command')
    exit(0)
fn = open(filename)
left_margin = 99999
right_margin = 0
for line in fn:
    line = line.strip()
    for left in range(len(line)):
        if line[left] != '.' : break
    if left < left_margin: left_margin = left
    for right in range(len(line)-1,-1,-1):
        if line[right] != '.' : break
    if right > right_margin : right_margin = right
fn.close()
if cmd != 'STRIP_ALL':
    fn = open(filename)
    if cmd =='STRIP':
        for line in fn:
            line = line.strip()
            print(line[left_margin:right_margin+1])
    if cmd =='LSTRIP':
        for line in fn:
            line = line.strip()
            print(line[left_margin:])
    if cmd =='RSTRIP':
        for line in fn:
            line = line.strip()
            print(line[:right_margin+1])
else:
    fn = open(filename)
    li = []
    for line in fn:
        line = line.strip()
        li.append(line[left_margin:right_margin+1])
    fn.close()
    cutli = []
    for j in range(len(li[0])):
        cut = True
        for i in range(len(li)):
            if li[i][j] != '.':
                cut = False
                break
        cutli.append(cut)
    for i in range(len(li)):
        for j in range(len(cutli)):
            if not cutli[j] : print(li[i][j],end='')
        print()