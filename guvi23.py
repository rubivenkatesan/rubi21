#rubi
n,k=map(int,input().split())
print()
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
li3=[]
for i in range(len(li2)):
  li1.append(li2[i])
  li3.append(max(li1))
print(*li3)
