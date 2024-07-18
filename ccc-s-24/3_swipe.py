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

swipes = []
for i in range(N-1, -1, -1):
    if A[i] == B[i]:
        continue
    # check to the right
    for heck in range(i,N):
        if A[heck] == B[i]:
            swipes.append(['L', i, heck])
            for frick in range(i, heck):
                # print("L",frick)
                A[frick] = B[i]
            break
    # check to the left
    for heck in range(i, -1, -1):
        if A[heck] == B[i]:
            swipes.append(['R', heck, i])
            for frick in range(heck, i):
                # print("R",frick)
                A[frick+1] = B[i]
            break

# print(A)
# print(B)
print("YES" if A == B else "NO")
print(len(swipes))
swipes = swipes[::-1]
print('\n'.join([' '.join(map(str, x)) for x in swipes]))