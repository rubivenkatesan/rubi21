#ru
n=int(input())
l=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
i=l.index(l[n-2])
j=a.index(l[i])
print(i-j)
