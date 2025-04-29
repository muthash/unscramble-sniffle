"""
Given two sorted arrays nums1 and nums2 of size x and y respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log(m+n)).

Solution:
    - Using binary search
    - Partition the arrays such that the combined elements on left of X and Y are equal to the combined elements on the right
    - Do a binary search on the smaller of the two arrays and
      try to find such a point that every element on the left <= element on the right.

    How to find the partition
        1) Start with the size of the smaller array divided into two as first partition i.e start=0 and end=len(array),
            - partitionX = (start + end) // 2
            - partitionY = (x + y + 1) // 2 - partitionX
        2) Check that every element on the left side <= every element on the right side
            - If maxLeftX <= minRightY and maxLeftY <= minRightX the median will be:
                - max(leftX, rightX) + min(leftY, rightY) / 2 for even
                - max(leftX, rightX) for odd
                    - If the total number of elements is odd, we will have one extra element on the left side
            - If maxLeftX > minRightY
                - we are too much on the right side so we move our binary search towards the left in X
                  :end = partitionX - 1
            - If maxLeftY > minRightX
                - we move torwards the right in X
                  :start = partitionX + 1

    - O(log(min(x,y))) time complexity
"""


def find_median_sorted_arrays(nums1, nums2):
    """
    :param nums1: Iterable of elements
    :param nums2: Iterable of elements
    :return: returns the median number
    """

    x, y = len(nums1), len(nums2)
    if x == 0 and y == 0:
        return 0

    if x == 0:
        medianY = y // 2
        return (nums2[medianY-1] + nums2[medianY]) / 2 if y % 2 == 0 else nums2[medianY]

    if y == 0:
        medianX = x // 2
        return (nums1[medianX-1] + nums1[medianX]) / 2 if x % 2 == 0 else nums1[medianX]

    if x > y:
        nums1, nums2, x, y = nums2, nums1, y, x

    start = 0
    end = x

    while start <= end:
        partitionX = (start + end) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        # if partitionX is 0, it means nothing is there on the left side. Use -inf for maxLeftX
        # if partiotionX is length of input then there is nothing on the right side. Use +inf for minRightX
        maxLeftX = float('-inf') if not partitionX else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if not partitionY else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # We have partitioned array at the correct place
            # Get max of the left elements and min of the right elements in case of even combined length
            # get max of the left for odd length
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            end = partitionX - 1
        else:
            start = partitionX + 1


def main():
    nums1, nums2 = [1, 2], [3, 4]
    print(f"The input is: {nums1} and {nums2}")
    print(f"The median is: {find_median_sorted_arrays(nums1, nums2)}")

    nums3, nums4 = [1, 3, 8, 9, 15], [7, 11, 19, 21, 18, 25]
    print(f"\nThe input is: {nums3} and {nums4}")
    print(f"The median is: {find_median_sorted_arrays(nums3, nums4)}")

    nums5, nums6 = [], []
    print(f"\nThe input is: {nums5} and {nums6}")
    print(f"The median is: {find_median_sorted_arrays(nums5, nums6)}")

    nums9, nums10 = [7, 11, 12, 16, 18], []
    print(f"\nThe input is: {nums9} and {nums10}")
    print(f"The median is: {find_median_sorted_arrays(nums9, nums10)}")

    nums7, nums8 = [], [7, 11, 19, 21, 22, 25]
    print(f"\nThe input is: {nums7} and {nums8}")
    print(f"The median is: {find_median_sorted_arrays(nums7, nums8)}")

    # Check on how to handle unsorted inputs
    nums11, nums12 = [3, 5, 2, 1], [10, 9]
    print(f"\nThe input is: {nums11} and {nums12}")
    print(f"The median is: {find_median_sorted_arrays(nums11, nums2)}")


if __name__ == '__main__':
    main()
