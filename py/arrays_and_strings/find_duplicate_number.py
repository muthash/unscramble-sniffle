"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
Prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Solution (1):
  - Use Floyd's Tortoise and Hare (Cycle Detection)
    - If we interpret nums such that for each pair of index i and value vi​, the "next" value vj​ is at index vi,
      we can reduce this problem to cycle detection.

Solution (2):
  - Array should not be read-only
    - Use the abs(vi) as the index for the next value
    - If the value is positive, change it to negative
    - if the value is negative, then the value acting as index is repeated
"""

def find_duplicate_floyd(nums):
    """
    :param nums: List[int]
    :return: returns the duplicate number
    """    
    if not nums or len(nums) < 2:
        return False

    # Find the intersection point of the two runners.
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Find the "entrance" to the cycle.
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    
    return ptr1


def find_duplicate(nums):
    """
    :param nums: List[int]
    :return: returns the duplicate number
    """  
    if not nums or len(nums) < 2:
        return False

    for num in nums:
        if nums[abs(num)] > 0:
            nums[abs(num)] *= -1
        else:
            return abs(num)

def main():
    nums = [1,3,4,2,2]
    print(f"The input is: {nums}")
    print(f"Floyd's Cycle Detection: {find_duplicate_floyd(nums)}")

    nums1 = [1,3,4,2,2]
    print(f"\nThe input is: {nums1}")
    print(f"The duplicate is: {find_duplicate(nums1)}")


if __name__ == '__main__':
    main()
