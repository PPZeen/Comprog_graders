pos = input().strip()
row = ''
col = ''
if len(pos) <= 3: 
    row = pos[0]
    col = pos[1:]
else:
    pos = pos.split(',')
    pos[0],pos[1] = pos[0].split('='),pos[1].split('=')
    k = [k.strip() for e in pos for k in e]
    for i in [0,2]:
        if k[i] == 'row' : row = k[i+1]
        if k[i] == 'col' : col = k[i+1]
#-----------------------------------------
row = row.strip()
col = col.strip()
#-----------------------------------------
valid_row = True
valid_col = True
if len(row) != 1 : valid_row = False
if not('A'<=row<='Z' or 'a'<=row<='z') : valid_row = False
if len(col) >= 3 or len(col) <=0 : valid_col = False
elif len(col) == 2 :
    if not '0'<=col[0]<='5' : valid_col = False
    elif col[0]=='5' and not '0'<=col[1]<='2' : valid_col = False
    elif not '0'<=col[1]<='9' : valid_col = False
elif len(col) == 1 :
    if not '1'<=col<='9' : valid_col = False
#-----------------------------------------
if not valid_row and not valid_col : print('Invalid row and column')
elif not valid_row : print('Invalid row')
elif not valid_col : print('Invalid column')
else:
    if ord(row)%2==int(col)%2 : print('White')
    else : print('Black')