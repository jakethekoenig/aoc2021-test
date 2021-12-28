f = open('day9.txt','r')

data = f.readlines()
lava = [[0]*(len(data[0])-1) for _ in range(len(data))]
i = 0
for line in data:
    j = 0
    for c in line:
        if c=="\n":
            continue
        lava[i][j] = int(line[j])
        j+=1
    i+=1

def get(i,j):
    if 0<=i<len(lava) and 0<=j<len(lava[0]):
        return lava[i][j]
    return 10

ans = 0
for i in range(len(lava)):
    for j in range(len(lava[0])):
        if get(i,j)<min(get(i,j+1),get(i,j-1),get(i+1,j),get(i-1,j)):
            print(i,j)
            ans+=1+get(i,j)
print(ans)

def flood(i,j):
    if get(i,j) >= 9:
        return 0
    lava[i][j] = 9
    return 1 + flood(i+1, j) + flood(i-1, j)+ flood(i, j-1) + flood(i, j+1)

ans = []
for i in range(len(lava)):
    for j in range(len(lava[0])):
        nex = flood(i,j)
        if nex!=0:
            ans += [nex]

ans.sort()
print(ans[-1]*ans[-2]*ans[-3])
