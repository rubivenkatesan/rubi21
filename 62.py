#rubi
n=int(input())
t=n
c=1
while(t!=0):
  r=t%10
  if r>1:
    c=0
    break
  t=t//10
if c==1:
  print("yes")
else:
  print("no")
