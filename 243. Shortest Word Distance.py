# 243. Shortest Word Distance
# Time: O(N)
# Space: O(1)

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = p2 = float('inf')
        result = float('inf')
    
        for i, w in enumerate(words):
            if w == word1:
                p1 = i
    
            elif w == word2:
                p2 = i

            result = min(abs(p2 - p1), result)
                
        return result