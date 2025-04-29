"""
In a given grid, each cell can have one of three values:
    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Solution:
  - In the above, as we can see, starting from the top rotten orange, the contamination would propagate layer by layer (or level by level),
    until it reaches the farthest fresh oranges. 
    The number of minutes that are elapsed would be equivalent to the number of levels in the graph that we traverse during the propagation.
  - The main algorithm is built around a loop iterating through the queue. 
    At each iteration, we pop out an element from the head of the queue. 
    Then we do some particular process with the popped element. 
    More importantly, we then append neighbors of the popped element into the queue, to keep the BFS process running.
"""

from collections import deque


def rotting_oranges_bfs(grid):
    queue = deque()

    # Step 1). build the initial set of rotten oranges
    fresh_oranges = 0
    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_oranges += 1

    # Mark the round / level, _i.e_ the ticker of timestamp
    queue.append((-1, -1))

    # Step 2). start the rotting process via BFS
    minutes_elapsed = -1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        row, col = queue.popleft()
        if row == -1:
            # we finish one round of processing
            minutes_elapsed += 1
            if queue:
                queue.append((-1, -1))
        else:
            # this is a rotten orange
            # then it would contaminate its neighbors
            for d in directions:
                neighbor_row, neighbor_col = row + d[0], col + d[1]
                if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                    if grid[neighbor_row][neighbor_col] == 1:
                        # this orange would be contaminated
                        grid[neighbor_row][neighbor_col] = 2
                        fresh_oranges -= 1

                        # this orange would then contaminate other oranges
                        queue.append((neighbor_row, neighbor_col))
    
    return minutes_elapsed if fresh_oranges == 0 else -1


def main():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print("Minimum number of minutes : {}".format(rotting_oranges_bfs(grid)))


if __name__ == '__main__':
    main()
