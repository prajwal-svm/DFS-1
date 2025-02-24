# 733. Flood Fill

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# DFS Intuition:
# Use a recursive function to traverse the grid.
# Keep track of the number of fresh oranges and the number of minutes elapsed.
# If a fresh orange is adjacent to a rotten orange, it becomes rotten and the number of fresh oranges is decremented.
# Return the number of minutes elapsed when there are no fresh oranges left.

# DFS Recursive:
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        original = image[sr][sc]
        if original == newColor:
            return image

        def fill(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original:
                return

            image[r][c] = newColor

            fill(r - 1, c)
            fill(r + 1, c)
            fill(r, c - 1)
            fill(r, c + 1)

        fill(sr, sc)
        return image
    
# DFS Iterative:
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        m, n = len(image), len(image[0])
        original = image[sr][sc]
        if original == newColor:
            return image

        stack = [(sr,sc)]

        while stack:
            r,c = stack.pop()

            if image[r][c] != original:
                continue
            
            image[r][c] = newColor
            
            if r >= 1 and image[r-1][c] == original:
                stack.append((r-1, c))
            if r + 1 < m and image[r+1][c] == original:
                stack.append((r + 1, c))
            if c >= 1 and image[r][c-1] == original:
                stack.append((r, c - 1))
            if c + 1 < n and image[r][c+1] == original:
                stack.append((r, c + 1))

        return image

# BFS Iterative:
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        m,n = len(image), len(image[0])

        directions = [
            [0,1],
            [1,0],
            [-1,0],
            [0,-1]
        ]

        q = deque([[sr,sc]])
        while q:
            r,c = q.popleft()

            for dx, dy in directions:
                x = r + dx
                y = c + dy

                if x >= 0 and x < m and y >= 0 and y < n:
                    if image[r][c] == image[x][y] and image[r][c] != color:
                        q.append([x,y])

            image[r][c] = color

        return image

