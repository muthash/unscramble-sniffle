"""
Given a sorted array nums, remove the duplicates in-place such that each
element appear only once and return the new length.

Solution:
    - Use two pointers
    - Since the array is already sorted, we can keep two pointers i and j,
      where i is the slow-runner while j is the fast-runner.
    - As long as nums[i] = nums[j], we increment j to skip the duplicate.

    - When we encounter nums[j]≠nums[i],
        - The duplicate run has ended so we must copy its value to nums[i+1].
        - i is then incremented and we repeat the same process again until j reaches the end of array.

Clarification:
    - Note that the input array is passed in by reference,
      which means modification to the input array will be known to the caller as well.
"""


def remove_duplicates(nums):
    """
    :param nums: Iterable of elements
    :return: returns the new array length value
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return 1

    count = 0

    for index in range(1, len(nums)):
        if (nums[count] != nums[index]):
            count += 1
            nums[count] = nums[index]

    return count + 1


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f"The input is: {nums}")
    print(f"The new length is: {remove_duplicates(nums)}")


if __name__ == '__main__':
    main()
