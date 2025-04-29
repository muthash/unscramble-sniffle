"""
Given a 2D matrix find the biggest square made up of 1's

Solution:
  - Consider each of the indices as not the top left but as the bottom right
  - row 0 and column 0 will be just themselves
"""

def largest_square(matrix):
    columns = len(matrix[0])
    rows = len(matrix)
    cache = [[0 for col in range(columns)] for row in range(rows)]

    result = 0
    for row in range(rows):
        for col in range(columns):
            if (row == 0 or col == 0):
                cache[row][col] = matrix[row][col]
            elif (matrix[row][col] > 0):
                cache[row][col] = 1 + min(cache[row][col-1],
                                          cache[row-1][col],
                                          cache[row-1][col-1])
            if cache[row][col] > result:
                result = cache[row][col]
    return result


def main():
    matrix = [[1, 0, 1, 0], [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1]]
    print("Biggest square: {}".format(largest_square(matrix)))


if __name__ == '__main__':
    main()
