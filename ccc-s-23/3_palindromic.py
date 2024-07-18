N = int(input())

print("".join(str(min(sum(abs(int(h[j])-int(h[-j-1])) for j in range(i//2+1)) for i in range(N - 1))) for h in(input().split())))