def is_odd(n):
    return n%2==1
def has_odds(x):
    for e in x:
        k = is_odd(e)
        if k: return k
    return False
def all_odds(x):
    for e in x:
        k = is_odd(e)
        if not k: return k
    return True
def no_odds(x):
    return not has_odds(x)
def get_odds(x):
    return [e for e in x if is_odd(e)]
def zip_odds(a, b):
    aa = get_odds(a)
    bb = get_odds(b)
    cc = []
    for i in range(max(len(aa),len(bb))):
        if i>len(aa)-1 : cc.append(bb[i])
        elif i>len(bb)-1 : cc.append(aa[i])
        else:
            cc.append(aa[i])
            cc.append(bb[i])
    return cc

exec(input().strip())