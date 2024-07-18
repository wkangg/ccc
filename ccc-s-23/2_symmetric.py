# crop = conseceutive mountains starting from the l-th to the r-th mountain where l <= r
# try to find the most symmetric crop
# asymmetric value of a crop = sum(abs(hl+i - hr - i)), for 0 <= i <= (r-l)/2
# for all possible crop lengths, find the asymmetric value of the most symmetric crop (the crop with the minimum asymmetric value)
import math

N = int(input()) # number of mountains in the picture
heights = input().split() # heights of each mountain, heights[N], i-th integer from the left represents hi

finalResult = []
for i in range(N): # each run is 1 int in the output
    possibleCrops = []
    for k in range(N - i): # each possible crop
        heightsCut = heights[k:i+1+k]
        # print(N, i, heights[:i + 1])
        totalDiff = 0
        for j in range(math.ceil((i + 1) / 2)): # calcs the abs diff and adds
            # print(heightsCut[j], heightsCut[-(j + 1)])
            totalDiff += abs(int(heightsCut[j]) - int(heightsCut[-(j + 1)]))
        possibleCrops.append(totalDiff)
    finalResult.append(str(min(possibleCrops)))

print(" ".join(finalResult))