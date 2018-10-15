# 890. Find and Replace Pattern
# Time:  O(N)
# Space: O(N)

# build bi-directional dict (two dicts) to track pattern and word
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        output = []
        for word in words:
            # not match pattern if length different
            if len(word) != len(pattern):
                continue
            pw_map = {}
            wp_map = {}
            for p, w in zip(pattern, word):
                if p not in pw_map and w not in wp_map:
                    pw_map[p] = w
                    wp_map[w] = p
                elif p in pw_map and pw_map[p] != w or w in wp_map and wp_map[w] != p:
                    break
            else:
                output.append(word)
        return output