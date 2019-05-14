#rubi
import collections
n = list(map(int,input().split()))
mem = list(map(str,input().split()))
dic = dict(collections.Counter(mem))
k = n[len(n)-1]
for x,y in dic.items():
    if(y == k):
        print(x)
