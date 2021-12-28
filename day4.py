f = open('day4.txt','r')

lines = f.readlines()
count = (len(lines)-2)//6

calls = [int(a) for a in lines[0].split(",")]

def finished(board):
    for i in range(5):
        col = True
        row = True
        for j in range(5):
            if board[j][i] != 0:
                col=False
            if board[i][j] != 0:
                row=False
        if col or row:
            return True
    return False

def cross(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0

def score_board(board):
    ans = 0
    for i in range(5):
        ans+=sum(board[i])
    return ans

def time_score(board):
    b = [[]]*5
    for i in range(5):
        b[i] = [int(a) for a in board[i].split()]
    for i in range(len(calls)):
        cross(b, calls[i])
        if finished(b):
            print(b)
            print(score_board(b))
            return i, calls[i]*score_board(b)

best = 0
best_score = 0
for i in range(count):
    time,score = time_score(lines[2+i*6:2+(i+1)*6-1])
    if time>best:
        best=time
        best_score = score

print(best_score)
