f = open('day2.in.txt','r')

lines = f.readlines()

depth, forw, aim = 0,0,0
for line in lines:
    word = line.split()[0]
    count = int(line.split()[1])
    if word=="forward":
        forw+=count
        depth+=aim*count
    if word=="down":
        aim+=count
    if word=="up":
        aim-=count
print(depth*forw)

