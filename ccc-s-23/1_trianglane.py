C = int(input()) # number of columns
row1 = input().split() # row 1 of triangles
row2 = input().split() # row 2 of triangles

# even indexes top point are pointing up,
# odd indexes are pointing down
# second row is inversed
def facingUp(num):
    return num % 2 == 0

perim = 0
for i in range(C):
    if row1[i] == "1": # row 1
        if i == 0 or row1[i - 1] == "0": # first is wet
            perim += 1 # first left

        if facingUp(i):
            if row2[i] == "1": # bottom is also wet
                pass
            else:
                perim += 1
        else:
            perim += 1 # top of triangle facing down
        
        if i+1 < C and row1[i + 1] == "1": # checks the one after (right side of triangle)
            pass # the one after is wet
        else:
            perim += 1 # it's not

    if row2[i] == "1":
        if i == 0 or row2[i - 1] == "0": # left side
            perim += 1

        if not facingUp(i): # second row is reversed, this is if it's facing up
            perim += 1
        else: # facing down
            if row1[i] == "1":
                pass
            else:
                perim += 1

        if i+1 < C and row2[i + 1] == "1": # checks the one after (right side of triangle)
            pass # the one after is wet
        else:
            perim += 1 # it's not

print(perim)

# 34 mins