# 824. Goat Latin
# Time: O(N)
# Space: O(N)

# simulation the rules
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')
        for i, word in enumerate(words):
            if word[0].lower() in {'a', 'e', 'i', 'o', 'u'}:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += 'a' * (i + 1)
            words[i] = word
        return ' '.join(words)
