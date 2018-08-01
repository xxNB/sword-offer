"""
364. 接雨水 II
Given n x m non-negative integers representing an elevation map 2d where the
area of each cell is 1 x 1, compute how much water it is able to trap after
raining.
样例
例如，给定一个 5*4 的矩阵：

[
  [12,13,0,12],
  [13,4,13,12],
  [13,8,10,12],
  [12,13,12,12],
  [13,13,13,13]
]
返回 14.

"""
import queue

class Cell:
    def __init__(self, x, y, h):
        self.x, self.y, self.h = x,y,h

    def __cmp__(self, other):
        if self.h < other.h:
            return -1
        elif self.h > other.h:
            return 1
        else:
            return 0

class Solution:
    def __init__(self, ):
        self.dx = [1,-1,0,0]
        self.dy = [0,0,1,-1]

    def trapRainWater(self, heights):
        if len(heights) == 0:
            return 0
        q = queue.PriorityQueue()
        n = len(heights)
        m = len(heights[0])
        visit  = [[False for i in range(m)] for i in range(n)]
        for i in range(n):
            q.put(Cell(i, 0, heights[i][0]))
            q.put(Cell(i, m-1, heights[i][m-1]))
            visit[i][0] = True
            visit[i][m-1] = True
        for i in range(m):
            q.put(Cell(0,i,heights[0][i]))
            q.put(Cell(n-1,i,heights[n-1][i]))
            visit[0][i] = True
            visit[n-1][i] = True
        ans = 0
        while not q.empty():
            now = q.get()
            for i in range(4):
                nx = now.x+self.dx[i]
                ny = now.y+self.dy[i]
                if 0 <=nx and nx<n and 0<=ny and ny<m and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.put(Cell(nx,ny,max(now.h, heights[nx][ny])))
                    ans += max(0, now.h - heights[nx][ny])
        return ans
