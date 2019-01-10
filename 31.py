#ruby
input_string = input()
count = 0
for c in input_string :
  if c.isspace() != True:
    count = count + 1
print(count)
