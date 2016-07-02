def bricks(a):
    dp=[0]*(n)
    suma=[0]*(n)
    suma[0]=a[0]
    for i in range(1,n):
        suma[i]=suma[i-1]+a[i]
    dp[0]=a[0]
    dp[1]=a[1]
    dp[2]=a[2]
    for k in range(4,n):
        dp[k]=max((suma[k-1]-dp[k-1])+a[k],(suma[k-2]-dp[k-2])+a[k]+a[k-1],(suma[k-3]-dp[k-3])+a[k]+a[k-1]+a[k-2])
    return dp[n-1]

t=input()       #takes input from user
for _ in range(t):
    n=input()
    arr=map(int,raw_input().strip().split(" "))
    a=[]
    for i in range(n-1,-1,-1):
        a.append(arr[i]) 
    print bricks(a)
