num = int(input())
ways = 0

for i in range(num //4 + 1):
    for j in range(num//5 + 1):
        if (4*i + 5*j) == num:
            ways += 1
print(ways)