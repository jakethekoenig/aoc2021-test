f = open('day3.txt','r')

lines = f.readlines()

count_zero = {}
count_one = {}
for line in lines:
    for i,c in enumerate(line[::-1]):
        if c=="0":
            count_zero[i-1] = count_zero.get(i-1, 0) + 1
        if c=="1":
            count_one[i-1] = count_one.get(i-1, 0) + 1
eps, gam = 0,0
print(count_zero)
print(count_one)
for i in count_zero.keys():
    if count_one[i] > count_zero[i]:
        eps += (2**i)
    else:
        gam += (2**i)

print(eps*gam)

def most_common(numbers, prefix):
    one,zero = 0,0
    for n in numbers:
        n = n.strip()
        if prefix == n[:len(prefix)]:
            if n[len(prefix)] == "1":
                one+=1
            else:
                zero+=1
    return (one, zero)

oxy = ""
co  = ""
for i in range(len(lines[0])-1):
    one,zero = most_common(lines, oxy)
    print(one,zero)
    if one>=zero:
        oxy+="1"
    else:
        oxy+="0"
    one,zero = most_common(lines, co)
    if one==0:
        co+="0"
    elif zero==0:
        co+="1"
    elif zero<=one:
        co+="0"
    else:
        co+="1"
print(oxy)
print(co)
print(int(oxy, 2)*int(co, 2))
