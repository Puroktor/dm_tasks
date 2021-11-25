def toTriangle(mat, x=0):
    mult = 1 
    if x>=len(mat)-1:
        return mult
    
    if mat[x][x] == 0 :
        for j in range(x+1, len(mat)):
            if mat[j][x] != 0 :
                mat[x], mat[j] = mat[j], mat[x]
                mult *= -1
    if mat[x][x]==0 :
        return 0
    
    for i in range(x, len(mat)):
        div = mat[i][x]
        if div ==0:
            continue
        mult *= div
        for j in range(x, len(mat)):
            mat[i][j] /= div
            if i!=x :
                mat[i][j] -= mat[x][j]
                
    return mult * toTriangle(mat, x+1)
    
def getMatDet(mat):
    return toTriangle(mat)* mat[len(mat)-1][len(mat)-1]

with open('inputs/input10.txt', 'r') as file:
    mat = [[int(num) for num in line.strip().split()] for line in file]
det = getMatDet(mat)
with open('outputs/output10.txt', 'w') as file:
    file.write(str(round(det)))
