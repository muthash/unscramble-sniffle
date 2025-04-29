"""
Given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).
Note:
  You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
  DO NOT allocate another 2D matrix and do the rotation.

Solution(1):
  - Transpose and then reverse
    - The transpose of a matrix is a new matrix whose rows are the columns of the original. 
      (This makes the columns of the new matrix the rows of the original)
    - Approach 1 makes two passes through the matrix, though it's possible to make a rotation in one pass.

Solution(2):
  - Rotate four rectangles in one single loop in layers
"""

def rotate_using_transpose(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])

    #transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # reverse each row
    for i in range(n):
        matrix[i].reverse()


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])
    for row in range(n//2 + n%2):
        for col in range(n//2):
            tmp = matrix[n - 1 - col][row]
            matrix[n - 1 - col][row] = matrix[n - 1 - row][n - col - 1]
            matrix[n - 1 - row][n - col - 1] = matrix[col][n - 1 -row]
            matrix[col][n - 1 - row] = matrix[row][col]
            matrix[row][col] = tmp


def main():
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print("The input is: {}".format(matrix))
    rotate_using_transpose(matrix)
    print("The transpose rotation: {}".format(matrix))

    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print("\nThe input is: {}".format(matrix))
    rotate(matrix)
    print("The rotation: {}".format(matrix))


if __name__ == '__main__':
    main()
