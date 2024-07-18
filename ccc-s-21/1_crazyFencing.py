N = int(input())
heights = input().split()
widths = input().split()

totalArea = 0
for i in range(N):
    smaller = min(int(heights[i]), int(heights[i + 1]))
    diff = abs(int(heights[i]) - int(heights[i + 1]))
    totalArea += smaller * int(widths[i])
    totalArea += diff * int(widths[i]) / 2
print(totalArea)