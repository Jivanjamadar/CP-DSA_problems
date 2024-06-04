def coin(t,test_cases):
    res=[]
    for a,b in test_cases:
        if (a+b)%3==0 and a<=2*b and b<=2*a:
            res.append("YES")
        else:
            res.append("NO")
    return res

t=int(input())
test_cases=[list(map(int,input().strip().split())) for _ in range(t)]  # test_cases storing in tuples for easy access
result= coin(t,test_cases)
for _ in range(t):
    print(result[_])