# 17. Letter Combinations of a Phone Number
# Time: O()
# Space: O(3**len(digits))

# use reduce to save middle state
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
            
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return reduce(lambda acc, digit: [x + y for x in acc for y in dic[digit]], digits, [''])

# use recursion to get later results
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
            
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return [a + b for a in self.letterCombinations(digits[:-1]) # not loop if only one digit
                      for b in self.letterCombinations(digits[-1])] or list(dic[digits])