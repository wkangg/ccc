donger = [
    [1, 2],
    [3, 4]
]

def verticalFlip():
    donger[0], donger[1] = donger[1], donger[0]

def horizontalFlip():
    donger[0][0], donger[0][1] = donger[0][1], donger[0][0]
    donger[1][0], donger[1][1] = donger[1][1], donger[1][0]

a = input()
for i in range(len(a)):
    if a[i] == 'H':
        verticalFlip()
    else:
        horizontalFlip()

print(donger[0][0], donger[0][1])
print(donger[1][0], donger[1][1])