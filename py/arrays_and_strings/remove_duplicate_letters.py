"""
Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Solution:
    - Use an ascending stack
    - While adding a letter to the stack, check if it has not been added and mark the letter as visited
    - If current letter is smaller than the top of the stack and the top letter has remaining appearance after,
      pop the letter out and mark it as not visited
"""
from collections import Counter, deque


def remove_duplicate_letters(string):
    """
    :param string: string containing only lowercase letters.
    :return: returns smallest lexicographical string order
    """
    if not string:
        return -1

    visited = set()
    stack = deque()
    counter = Counter(string)

    for char in string:
        counter[char] -= 1
        if char in visited:
            continue

        while stack and char < stack[-1] and counter[stack[-1]]:
            visited.remove(stack.pop())

        stack.append(char)
        visited.add(char)

    return "".join(stack)


def main():
    string = "cbacdcbc"
    print(f"The input is: {string}")
    print(f"The smallest lexicographical order is: {remove_duplicate_letters(string)}")


if __name__ == '__main__':
    main()
