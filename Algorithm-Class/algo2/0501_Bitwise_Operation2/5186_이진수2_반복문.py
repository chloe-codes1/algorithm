T=int(input())
for t in range(1, T+1):
    a=float(input())
    ans=[]
    tmp=0
    for i in range(13):
        if tmp ==a:
            break
        if tmp + 1*(2)**(-i-1)>a:
            ans.append(0)
        else:
            tmp += 1*(2)**(-i-1)
            ans.append(1)
    if len(ans)>12:
        result = 'overflow'
    else:
        result = ''.join(repr(k) for k in ans)
    
    print("#{} {}".format(t,result))