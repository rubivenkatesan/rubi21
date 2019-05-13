#rubi
n=int(input())
l=[int(i) for i in input().split()]
l1=sorted(l)
if l==l1:
  print("yes")
else:
  print("no")
