N = int(input())
A = input().split()
B = input().split()

if A == B:
    print("YES\n0")
    exit()

for i in range(N):
    if A[i] != B[i] and (i == 0 or B[i] != B[i-1]) and (i == N-1 or B[i] != B[i+1]):
        print("NO")
        exit()

print("YES")

swipes = []
for i in range(N):
    if A[i] == B[i]:
        continue
    # check to the left
    for heck in range(i, -1, -1):
        # print('leftcheck','heck', heck, 'i', i, 'A[i]', A[i], 'B[heck]', B[heck])
        if A[heck] == B[i]:
            swipes.append(['R', heck, i])
            # print('swiping left', heck, i)
            for frick in range(heck, i):
                A[frick] = A[i]
    # check to the right
    for heck in range(i,N):
        # print('rightcheck','heck', heck, 'i', i, 'A[i]', A[i], 'B[heck]', B[heck])
        if A[heck] == B[i]:
            swipes.append(['L', i, heck])
            # print('swiping right', i, heck)
            for frick in range(i, heck):
                A[frick] = A[i]



    # for heck in range(N-1, -1, -1):
    #     if B[heck] == A[i]:
    #         if i > heck:
    #             # swipe left
    #             swipes.append(['L', heck, i])
    #             for frick in range(heck, i):
    #                 A[frick] = A[i]
    #         else:
    #             # swipe right
    #             swipes.append(['R', i, heck])
    #             for frick in range(i, heck):
    #                 A[frick] = A[i]

print(len(swipes))
print('\n'.join([' '.join(map(str, x)) for x in swipes]))


    # if i > 0 and A[i] == B[i-1]:
    #     swipes.append("L")
    #     A[i], A[i-1] = A[i-1], A[i]
    # elif i < N-1 and A[i] == B[i+1]:
    #     swipes.append("R")
    #     A[i], A[i+1] = A[i+1], A[i]
    # else:
    #     print("NO")
    #     exit()