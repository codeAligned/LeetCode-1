# 383. Ransom Note
# Time: O(len(magazine))
# Space: O(distinct letters in magazine)

from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt = Counter(magazine)
        for c in ransomNote:
            if c not in cnt:
                return False
            else:
                if cnt[c] == 0:
                    return False
                else:
                    cnt[c] -= 1
        return True