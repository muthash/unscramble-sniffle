"""
You are given a circular array nums of positive and negative integers. 
If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. 
Since the array is circular, assume that the last element's next element is the first element,
and the first element's previous element is the last element.

A cycle must start and end at the same index and the cycle's length > 1 and movements in a cycle must all follow a single direction.
In other words, a cycle must not consist of both forward and backward movements.

Solution:
  - Loop through the array
   - Handle empty array and an array with one element
   - Check if element is visited (change to str) 
   - Check if there is a change in direction (use XOR or num * nums[i] > 0)
   - Check for self circular loop (nums[i] % nlen)
"""

def circular_array_loop(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums or len(nums) < 2:
        return False
        
    nlen = len(nums)
        
    for index in range(nlen): 
        if isinstance(nums[index], str):
            continue
        
        mark = str(index) # Use a distinct marker for each starting point
        direction = nums[index] > 0 # loop direction, cannot be changed midway

        # Explore while node is new, direction is same, and is not self loop
        # Note: if node has been marked by a different marker, no need to proceed. This gives O(n) time.
        while isinstance(nums[index], int) and (direction ^ (nums[index] < 0)) and (nums[index] % nlen != 0):
            jump = nums[index]
            nums[index] = mark
            index = (index + jump) % nlen

        # if self loop, nums[i] is never marked
        # if nums[i] is marked, a cycle is found
        if nums[index] == mark:
            return True

    return False


def main():
    nums = [2,-1,1,2,2]
    print(f"The input is: {nums}")
    print(f"Circular loop: {circular_array_loop(nums)}")

    nums1 = [-2,1,-1,-2,-2]
    print(f"\nThe input is: {nums1}")
    print(f"Circular loop: {circular_array_loop(nums1)}")

    nums2 = [791, 1]
    print(f"\nThe input is: {nums2}")
    print(f"Circular loop: {circular_array_loop(nums2)}")


if __name__ == '__main__':
    main()
