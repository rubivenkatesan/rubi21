#rubi
s=input()
l=list(s)
a=""
for i in range(0,len(l),2):
    l[i],l[i+1]=l[i+1],l[i]
for i in l:
    a=a+i
print(a)
