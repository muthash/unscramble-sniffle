"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Solution:
  - Treat the 2d grid map as an undirected graph and there is an edge between two horizontally or vertically adjacent nodes of value '1'.
  - BFS
    - Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search. 
      Put it into a queue and set its value as '0' to mark as visited node. 
      Iteratively search the neighbors of enqueued nodes until the queue becomes empty.
"""

from collections import deque 

class SolutionBFS:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.bfs(grid, row, col)
                    count += 1
        return count

    def bfs(self, grid, r, c):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = '0'
        while queue:
            row, col = queue.popleft()
            if row+1 < len(grid) and grid[row+1][col] == '1':
                queue.append((row+1, col))
                grid[row+1][col] = "0"
            if row-1 >= 0 and grid[row-1][col] == '1':
                queue.append((row-1, col))
                grid[row-1][col] = "0"
            if col+1 < len(grid[0]) and grid[row][col+1] == '1':
                queue.append((row, col+1))
                grid[row][col+1] = "0" 
            if col-1 >= 0 and grid[row][col-1] == '1':
                queue.append((row, col-1))
                grid[row][col-1] = "0" 



def main():
    grid = [['1', '1', '0', '0'], ['1', '1', '0', '0'], ['0', '0', '1', '0'],
            ['0', '0', '0', '1'], ['0', '0', '0', '1']]
    bfs = SolutionBFS()
    print("Number of Islands: {}".format(bfs.numIslands(grid)))


if __name__ == '__main__':
    main()
