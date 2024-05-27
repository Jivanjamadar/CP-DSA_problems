def permutation(n):
    if n==1:
        print('1')
        return 
    if n==2 or n==3:
        print('NO SOLUTION')
        return
    even=[]
    odd=[]
    for i in range(1,n+1):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    loos=even+odd
    print(" ".join(map(str,loos)))
n=int(input())
permutation(n)