"""Read every other line on a file called input.txt """"
f = open('input.txt', 'r')

count = 0
for line in f:
    count+=1
    if count%2 ==0:
      print line

