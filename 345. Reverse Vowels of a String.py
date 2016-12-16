# 345. Reverse Vowels of a String
# Time: O(N)
# Space: O(vowels)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        lis_s = list(s)
        v = []
        for c in lis_s:
            if c in vowels:
                v.append(c)
        for i, c in enumerate(lis_s):
            if c in vowels:
                lis_s[i] = v.pop()
        return "".join(lis_s)
