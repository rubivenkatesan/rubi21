#rubi
a=input()
l=['a','e','i','o','u']
if any(i in l for i in a):
  print("yes")
else:
  print("no")
