n = int(input())
k = int(input())
if (n<1) and (k<1) : print('Invalid n and k')
elif (n<1) : print('Invalid n')
elif k<1 : print('Invalid k')
else :
  head = [str(i)+(n+1-len(str(i)))*'-' for i in range(1,k)]
  head.append(str(k)+(n-len(str(k)))*'-')
  print(''.join(head))
  ans = ['0','1']
  for i in range(n-1):
      ans = ans + ans[::-1]
      for j in range(len(ans)//2):
          ans[j] = '0'+ans[j]
          ans[j+len(ans)//2] = '1'+ans[j+len(ans)//2]
  ans2 = [ans[i:i+k] for i in range(0,2**n,k)]
  for e in ans2:
      print(','.join(e))