#rubi
n=int(input())
for i in range(2,n):
  if (n%i<1):
    print("yes")
    break
else:
  print("no")
