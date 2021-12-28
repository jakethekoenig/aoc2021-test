f = open('day6.txt','r')


count = {}
for i in range(9):
    count[i] = 0
fish = f.read().split(",")
for f in fish:
    count[int(f)] += 1
print(count)

for i in range(256):
    nex = {}
    for i in range(9):
        nex[i] = 0
    nex[8] = count[0]
    nex[6] = count[0]
    for i in range(8):
        nex[i] += count[i+1]
    count = nex


ans = 0
for i in range(9):
    ans += count[i]
print(ans)

