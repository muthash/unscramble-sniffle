"""
Find the element that appears once
Expected time complexity is O(n) and O(1) extra space.

Solution:
    - Run a loop for all elements in array maintaining the following two values at the end of every iteration.
    - ones: The bits that have appeared 1st time or 4th time or 7th time .. etc.
    - twos: The bits that have appeared 2nd time or 5th time or 8th time .. etc.
"""


def get_single(arr):
    """
    :param arr : Iterable of elements where every element occurs three times, except one element which occurs only once
    :return : returns the element that occurs once
    """
    size = len(arr)
    ones = 0
    twos = 0

    for i in range(size):
        twos |= (ones & arr[i])
        ones ^= arr[i]
        common_bit_mask = ~(ones & twos)
        ones &= common_bit_mask
        twos &= common_bit_mask
    return ones


def main():
    arr = [3, 3, 2, 3]
    print(f"The input is: {arr}")
    print(f"The element with single occurrence is: {get_single(arr)}")


if __name__ == '__main__':
    main()
