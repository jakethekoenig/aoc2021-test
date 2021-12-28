
f = open('day7.txt','r')

data = sorted([int(a) for a in f.read().split(",")])
median = data[len(data)//2]
ans = 0
for i in data:
    ans += abs(i - median)
print(ans)
best = 10000000000
for guess in range(0, max(data)+1):
    ans = 0
    for i in data:
        ans += abs(i - guess)*(abs(i - guess)+1)//2
    best = min(best, ans)
    print(ans, guess)
print(best)
    


