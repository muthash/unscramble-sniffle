"""
Given a collection of distinct integers, return all possible permutations.

Solution:
  - https://www.youtube.com/watch?v=GuTPwotSdYw
  - Backtracking is an algorithm for finding all solutions by exploring all potential candidates. 
    If the solution candidate turns to be not a solution (or at least not the last one),
    backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

  - The backtrack function will take the index of the first integer to consider as an argument backtrack(first).
    - If the first integer to consider has index n that means that the current permutation is done.
    - Iterate over the integers from index first to index n - 1.
      - Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
      - Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
      - Now backtrack, i.e. swap(nums[first], nums[i]) back.
"""
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(first = 0):
        # if all integers are used up
        if first == n:  
            output.append(nums[:])
        for i in range(first, n):
            # place i-th integer first in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]
    
    n = len(nums)
    output = []
    backtrack()
    return output


def main():
    nums = [1,2,3]
    print("The input is: {}".format(nums))
    print("Permutations are: {}".format(permute(nums)))


if __name__ == '__main__':
    main()
