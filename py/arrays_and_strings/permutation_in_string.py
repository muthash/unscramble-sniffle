"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Solution(1):
  - Sliding Window Approach
    - We create a hashmap once for the first window in s2. 
    - Then, later on when we slide the window, we know that we add one preceding character and add a new succeeding character to the new window considered. 
    - Thus, we update the hashmap by just updating the indices associated with those two characters only. 
    - For every updated hashmap, we compare all the elements of the hashmap for equality to get the required result.

Solution(2):
  - Optimized Sliding Window Approach
    - Instead of comparing all the elements of the hashmaps for every updated s2map corresponding to every window of s2 considered, 
      we keep a track of the number of elements which were already matching in the earlier hashmap and 
      update just the count of matching elements when we shift the window towards the right.
    - To do so, we maintain a count variable, which stores the number of characters(out of the 26 alphabets),
      which have the same frequency of occurence in s1 and the current window in s2.
    - When we slide the window,
      - If the deduction of the last element and the addition of the new element leads to a new frequency match of any of the characters,
        we increment the count by 1. If not, we keep the count intact.
      - If a character whose frequency was the same earlier(prior to addition and removal) is added,
        it now leads to a frequency mismatch which is taken into account by decrementing the same count variable.
      - If, after the shifting of the window, the count evaluates to 26, it means all the characters match in frequency totally. 
        So, we return a True in that case immediately.
  - Time complexity : O(l1+(l2−l1)). where l1 is the length of string s1 and l2 is the length of string s2.
"""

from collections import Counter

def check_inclusion(s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        s1map = Counter(s1)
        s2map = Counter(s2[:len(s1)])
        
        for index in range(len(s1), len(s2)):
            if s1map == s2map: 
                return True
            
            s2map[s2[index]] += 1
            s2map[s2[index-len(s1)]] -= 1
            
            if s2map[s2[index-len(s1)]] == 0: 
                del s2map[s2[index-len(s1)]]
        
        return s1map == s2map

def check_inclusion_count(s1, s2):
    """
    :param s1: str
    :param s2: str
    :rtype: bool
    """
    if len(s1) > len(s2):
        return False
    
    s1map = [0 for num in range(26)]
    s2map = [0 for num in range(26)]
    count = 0
    
    for index in range(len(s1)):
        s1map[ord(s1[index]) - ord('a')] += 1
        s2map[ord(s2[index]) - ord('a')] += 1

    for index in range(26):
        if s1map[index] == s2map[index]:
            count += 1
    
    for index in range(len(s1), len(s2)):
        if count == 26:
            return True
        
        next_end = ord(s2[index]) - ord('a')
        prev_start = ord(s2[index - len(s1)]) - ord('a')

        s2map[next_end] += 1
        if s2map[next_end] == s1map[next_end]:
            count += 1
        elif s2map[next_end] == (s1map[next_end] + 1):
            count -= 1

        s2map[prev_start] -= 1
        if s2map[prev_start] == s1map[prev_start]:
            count += 1
        elif s2map[prev_start] == (s1map[prev_start] - 1):
            count -= 1

    return count == 26

def main():
    s1 = "ab"
    s2 = "eidbaooo"
    print(f"The input is: {s1} and {s2}")
    print(f"s2 contains one permutation of s1: {check_inclusion(s1, s2)}")

    s1 = "ab"
    s2 = "eidboaooo"
    print(f"\nThe input is: {s1} and {s2}")
    print(f"s2 contains one permutation of s1: {check_inclusion(s1, s2)}")

    s1 = "ab"
    s2 = "eidbaooo"
    print(f"\nThe input is: {s1} and {s2}")
    print(f"Using count method: {check_inclusion_count(s1, s2)}")

    s1 = "ab"
    s2 = "eidboaooo"
    print(f"\nThe input is: {s1} and {s2}")
    print(f"Using count method: {check_inclusion_count(s1, s2)}")

if __name__ == '__main__':
    main()
