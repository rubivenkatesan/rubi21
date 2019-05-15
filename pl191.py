#rubi
m=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if b[::-1]==a:
  print("yes")
else:
  print("no")  
