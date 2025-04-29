"""
Given an unsorted integer array, find the smallest missing positive integer.
Your algorithm should run in O(n) time and uses constant extra space.

Solution:
    - Use Index as a hash key approach
      - Check if 1 is present in the array. If not, you're done and 1 is the answer.
      - If nums = [1], the answer is 2.
      - Replace negative numbers, zeros, and numbers larger than n by 1s.
      - Walk along the array. Change the sign of a-th element if you meet number a. 
        Be careful with duplicates : do sign change only once. 
        Use index 0 to save an information about presence of number n since index n is not available.
      - Walk again along the array. Return the index of the first positive element. 
      - If nums[0] > 0 return n
      - If on the previous step you didn't find the positive element in nums, that means that the answer is n + 1.
"""

def first_missing_positive(nums):
    """
    :param nums: List[int]
    :rtype: int, returns the first missing number
    """
    nlen = len(nums)
    
    # Base case.
    if 1 not in nums:
        return 1

    # nums = [1]
    if nlen == 1:
        return 2

    # Replace negative numbers, zeros, and numbers larger than nlen by 1s.
    # After this convertion nums will contain only positive numbers.
    for index in range(nlen):
        if nums[index] <= 0 or nums[index] > nlen:
            nums[index] = 1

    # Use index as a hash key and number sign as a presence detector.
    for index in range(nlen): 
        num = abs(nums[index])
        if num == nlen:
            nums[0] = - abs(nums[0])
        else:
            nums[num] = - abs(nums[num])
    
    # Now the index of the first positive number is equal to first missing positive.
    for index in range(1, nlen):
        if nums[index] > 0:
            return index

    if nums[0] > 0:
        return nlen

    return nlen + 1

def main():
    nums = [1,2,0]
    print(f"The input is: {nums}")
    print(f"The smallest missing positive integer is: {first_missing_positive(nums)}")

    nums = [3,4,-1,1]
    print(f"\nThe input is: {nums}")
    print(f"The smallest missing positive integer is: {first_missing_positive(nums)}")

    nums = [7,8,9,11,12]
    print(f"\nThe input is: {nums}")
    print(f"The smallest missing positive integer is: {first_missing_positive(nums)}")


if __name__ == '__main__':
    main()
