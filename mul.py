#ruby
def multiple(m, n): 
  
    # inserts all elements from n to  
    # (m * n)+1 incremented by n. 
    a = range(n, (m * n)+1, n) 
      
    print(*a) 
  
# driver code  
m = int(input())
n = int(input())
multiple(m, n) 
