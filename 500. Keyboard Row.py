# 500. Keyboard Row
# Time: O(N)
# Space: O(N)

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1_set = set("qwertyuiop")
        row2_set = set("asdfghjkl")
        row3_set = set("zxcvbnm")
        res = []
        for word in words:
            word_set = set(word.lower())
            if word_set <= row1_set or word_set <= row2_set or word_set <= row3_set:
                res.append(word)
        return res
