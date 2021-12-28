f = open('day1.in','r')

lines = f.readlines()
lines = [int(a) for a in lines]
count = 0
 
for i in range(len(lines)-3):
    if lines[i+3]>lines[i]:
        count +=1
print(count)

