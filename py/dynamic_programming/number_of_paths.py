"""
Find the number of paths from top left to bottom right in a matrix.

Solution:
  - The only paths to be considered is movement either right or down
  - To get to the bottom, you consider the adjecnt two cells in the matrix
  - row 0 and column 0 will be 1 because there is only one way to get the cells
"""

def number_of_paths(num):
    """
    :type: int
    :rtype: int
    """
    grid = [[0 for col in range(num)] for row in range(num)]
    
    for row in range(num):
        for col in range(num):
            if row == 0 or col == 0:
                grid[row][col] = 1
            else:
                grid[row][col] = grid[row-1][col] + grid[row][col-1]

    return grid[num-1][num-1]


def main():
    num = 4
    print("The number of paths: {}".format(number_of_paths(num)))
    num = 10
    print("\nThe number of paths: {}".format(number_of_paths(num)))

if __name__ == '__main__':
    main()
