f = open('day8.txt','r')

ans = 0

def id(data, blob):
    l = len(blob)
    if l==2:
        return 1
    if l==3:
        return 7
    if l==4:
        return 4
    if l==7:
        return 8
    if l==5:
        oneblob = ""
        for d in data:
            if len(d) == 2:
                oneblob = d
                break
        if oneblob[0] in blob and oneblob[1] in blob:
            return 3
        fourblob = ""
        for d in data:
            if len(d) == 4:
                fourblob = d
                break
        if len(set(fourblob) & set(blob)) == 3:
            return 5
        else:
            return 2
    if l==6:
        oneblob = ""
        for d in data:
            if len(d) == 2:
                oneblob = d
                break
        if not (oneblob[0] in blob and oneblob[1] in blob):
            return 6
        fourblob = ""
        for d in data:
            if len(d) == 4:
                fourblob = d
                break
        if len(set(fourblob) & set(blob)) == 3:
            return 0
        else:
            return 9




for line in f.readlines():
    data = line.split("|")[0].split()
    output = line.split("|")[1].split()
    for i,blob in enumerate(output):
        val = id(data,blob)
        print(val)
        ans+=val*(10**(3-i))

print(ans)
