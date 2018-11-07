# 748. Shortest Completing Word
# Time: O(N)
# Space: O(N)

# Counter have operator '-', 
# for: 
#     if: 
#         break 
# else:
#     something meet for loop needs
from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        lp_cnt = Counter(''.join([l for l in licensePlate.lower() if l.isalpha()]))
        min_length = float('inf')
        res = ''
        for word in words:
            word_cnt = Counter(word.lower())
            if len(word) < min_length and not lp_cnt - word_cnt:
                min_length = len(word)
                res = word
        return res
