"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Solution:
  - Treat the 2d grid map as an undirected graph and there is an edge between two horizontally or vertically adjacent nodes of value '1'.
  - DFS
    - Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Depth First Search.
      During DFS, every visited node should be set as '0' to mark as visited node. 
      Count the number of root nodes that trigger DFS.
      This number would be the number of islands since each DFS starting at some root identifies an island.
"""

class SolutionDFS:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count += 1
        return count

    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >=len(grid) or col>=len(grid[0]) or grid[row][col] != "1":
            return
        
        grid[row][col] = '0'
        self.dfs(grid, row+1, col)
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row, col-1)


def main():
    grid = [['1', '1', '0', '0'], ['1', '1', '0', '0'], ['0', '0', '1', '0'],
            ['0', '0', '0', '1'], ['0', '0', '0', '1']]
    dfs = SolutionDFS()
    print("Number of Islands: {}".format(dfs.numIslands(grid)))


if __name__ == '__main__':
    main()