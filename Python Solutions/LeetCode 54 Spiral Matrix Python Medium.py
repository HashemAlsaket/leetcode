# Link to video: https://youtu.be/Qtaidu5MExM

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        res = []
        i, j, k = 0, 0, 0
        
        while k < m and k < n and matrix[k] != 'v':
            i, j = k, k
            while j < n and matrix[i][j] != 'v':
                res.append(matrix[i][j])
                matrix[i][j] = 'v'
                j += 1
            j -= 1
            i += 1
            while i < m and matrix[i][j] != 'v':
                res.append(matrix[i][j])
                matrix[i][j] = 'v'
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and matrix[i][j] != 'v':
                res.append(matrix[i][j])
                matrix[i][j] = 'v'
                j -= 1
            j += 1
            i -= 1
            while i >= 0 and matrix[i][j] != 'v':
                res.append(matrix[i][j])
                matrix[i][j] = 'v'
                i -= 1
            k += 1
        return res