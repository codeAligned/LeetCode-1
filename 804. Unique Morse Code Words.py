# 804. Unique Morse Code Words
# Time:  O(N)
# Space: O(N)

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trans_set = set()
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            trans_set.add(''.join([morse_code[ord(c) - ord('a')] for c in word]))
        return len(trans_set)