N = int(input()) # num people at the social gathering
hats = [int(input()) for i in range(N)] # list of hats

count = 0
for i in range(N//2):
    if hats[i] == hats[N//2+i]:
        count += 2
print(count)