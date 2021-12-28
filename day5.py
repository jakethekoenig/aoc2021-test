f = open('day5.txt','r')

field = [[0]*1000 for _ in range(1000)]

for line in f.readlines():
    p1 = line.split()[0]
    x1 = int(p1.split(",")[0])
    y1 = int(p1.split(",")[1])
    p2 = line.split()[-1]
    x2 = int(p2.split(",")[0])
    y2 = int(p2.split(",")[1])
    if x1==x2:
        for i in range(min(y1,y2),max(y1,y2)+1):
            field[x1][i]+=1
    elif y1==y2:
        for i in range(min(x1,x2),max(x1,x2)+1):
            field[i][y1]+=1
    if abs(x1-x2) == abs(y1-y2) :
        stepx = (1 if x1<x2 else -1)
        stepy = (1 if y1<y2 else -1)
        for i,j in zip(range(x1, x2+stepx, stepx), range(y1, y2+stepy, stepy)):
            field[i][j] +=1

ans = 0
for i in range(1000):
    for j in range(1000):
        if field[i][j]>1:
            ans+=1
print(ans)
