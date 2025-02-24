# 542. 01 Matrix

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

# BFS:
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        while q:
            i,j = q.popleft()

            for dx,dy in directions:
                x = dx + i
                y = dy + j
                if x >= 0 and x < m and y >= 0 and y < n and mat[x][y] == -1:
                    mat[x][y] = mat[i][j] + 1
                    q.append((x,y))

        return mat

# DP:
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [row[:] for row in mat]
        m, n = len(dp), len(dp[0])

        for row in range(m):
            for col in range(n):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row > 0:
                        min_neighbor = min(min_neighbor, dp[row - 1][col])
                    if col > 0:
                        min_neighbor = min(min_neighbor, dp[row][col - 1])
                        
                    dp[row][col] = min_neighbor + 1
    
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row < m - 1:
                        min_neighbor = min(min_neighbor, dp[row + 1][col])
                    if col < n - 1:
                        min_neighbor = min(min_neighbor, dp[row][col + 1])
                        
                    dp[row][col] = min(dp[row][col], min_neighbor + 1)

        return dp