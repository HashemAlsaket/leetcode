# Link to video: https://youtu.be/AAiNtPhZl3I

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        
        arr = []
        
        for i in range(m):
            diag = []
            a = i
            j = 0
            while a >= 0 and j < n:
                diag.append(mat[a][j])
                a -= 1
                j += 1
            arr.append(diag)
        
        for j in range(1, n):
            diag = []
            a = j
            i = m - 1
            while a < n and i >= 0:
                diag.append(mat[i][a])
                i -= 1
                a += 1
            arr.append(diag)
        
        for i in range(1, len(arr), 2):
            arr[i] = arr[i][::-1]
        return [x for y in arr for x in y]