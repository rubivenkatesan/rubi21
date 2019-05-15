#rubi
n=int(input())
i=0
p=0
if n==0:
    print("1")
else:
    while p<n:
        p=2**i
        i=i+1
    if p==n:
        print(i)
    else:
        print(i-1)
