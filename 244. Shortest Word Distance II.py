# 244. Shortest Word Distance II
# Time: O(N)
# Time: O(N)

from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dic = defaultdict(list)
        for i, w in enumerate(words):
            self.dic[w].append(i)
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lst1, lst2 = self.dic[word1], self.dic[word2]
        len1, len2, i, j, res = len(lst1), len(lst2), 0, 0, float("inf")
        while i < len1 and j < len2:
            res = min(res, abs(lst1[i] - lst2[j]))
            if lst1[i] < lst2[j]:
                i += 1
            else:
                j += 1
        return res
        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")