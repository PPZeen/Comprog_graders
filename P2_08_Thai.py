def readword(n):
    read = ['soon','neung','song','sam','si','ha','hok','chet','paet','kao']
    return read[n]
def to_Thai(n):
    ans = ''
    k = n
    if k == 0 : ans+=readword(k)
    else :
        if len(str(n))>3:
            p = k//1000
            if p>0 : 
                ans+=readword(p)
                ans+=' pun '
            k%=1000
        if len(str(n))>2:
            p = k//100
            if p>0 : 
                ans+=readword(p)
                ans+=' roi '
            k%=100
        if len(str(n))>1:
            p = k//10
            if p>2 : 
                ans+=readword(p)+' sip '
            elif p==1: ans+='sip '
            elif p==2:
                ans+='yi sip '
            k%=10
        if k==1 and len(str(n))>1 : ans+='et'
        elif k==0 : pass
        else : ans+=readword(k)
    return ans.strip()
exec(input().strip())