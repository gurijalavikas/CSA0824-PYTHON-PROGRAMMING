
def searchMatrix(matrix, target):
    for row in matrix:
        if target in row:
            return True
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target=5
print(searchMatrix(matrix,target))
