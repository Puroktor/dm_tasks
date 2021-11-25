def getMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatDet(mat):
    if len(mat) == 2:
        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]

    det = 0
    for c in range(len(mat)):
        det += ((-1)**c)*mat[0][c]*getMatDet(getMinor(mat,0,c))
    return det

with open('inputs/input10.txt', 'r') as file:
    mat = [[int(num) for num in line.strip().split()] for line in file]
det = getMatDet(mat)
with open('outputs/output10.txt', 'w') as file:
    file.write(str(det))

