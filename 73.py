#rubi
n=int(input())
m,k=map(int,input().split())
print("yes" if ((n<k) & (n>=m)) else "no")
