N = int(input()) # canvas y
M = int(input()) # canvas x
K = int(input()) # actions

canvas = [[0 for x in range(M)] for y in range(N)]

for i in range(K):
    action = input().split()
    if action[0] == "C":
        for rowIndex in range(len(canvas)):
            canvas[rowIndex][int(action[1]) - 1] = 1 if canvas[rowIndex][int(action[1]) - 1] == 0 else 0
    elif action[0] == "R":
        for colIndex in range(len(canvas[0])):
            canvas[int(action[1]) - 1][colIndex] = 1 if canvas[int(action[1]) - 1][colIndex] == 0 else 0

gold = 0
for row in canvas:
    for loc in row:
        if loc == 1:
            gold += 1

print(gold)