sameGroup = []
diffGroup = []
realGroup = []

x = int(input())
for i in range(x):
    a = input().split()
    sameGroup.append(a)
    
y = int(input())
for i in range(y):
    b = input().split()
    diffGroup.append(b)

g = int(input())
for i in range(g):
    c = input().split()
    realGroup.append(c)

c1 = x
c2 = 0

for i in realGroup:
    for j in sameGroup:
        r = all(elem in i for elem in j)
        if r:
            c1 -= 1

for i in realGroup:
    for j in diffGroup:
        r = all(elem in i for elem in j)
        if r:
            c2 += 1

viols = c1+c2
print(viols)