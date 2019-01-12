# 165. Compare Version Numbers
# Time:  O(N)
# Space: O(N)

# split version by dot, and compare from left to right
class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        min_len = min(len(v1), len(v2))
        
        for n1, n2 in zip(v1[:min_len], v2[:min_len]): # compare same bits from left
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        
        if len(v1) > min_len: # if v1 is longer, check if any number > 0
            for n in v1[min_len:]:
                if n > 0:
                    return 1
            return 0
        elif len(v2) > min_len: # if v2 is longer, check if any number > 0
            for n in v2[min_len:]:
                if n > 0:
                    return -1
            return 0
        
        return 0 # same length and same numbers between v1 and v2, return 0
