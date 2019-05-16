#ru
s=input()
m=""
for i in range(len(s)-1):
  for j in range(i+1,len(s)+1):
    r=s[i:j+1]
    if len(r)>len(m) and r==r[::-1]:
            m=r
print(m)
    
