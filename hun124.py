#rubi
r= int(input())
for i in range(r,0,-1):
    s = []
    for _ in range(i,0,-1):
        s.append('1')
    print(' '.join(s))
