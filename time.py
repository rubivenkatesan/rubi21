#rubi
time = input()
hour = time //60
time %= 60
minutes = time // 1
print("%d %d" % (hour,minutes))
