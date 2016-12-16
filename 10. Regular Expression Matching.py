# 10. Regular Expression Matching

import re

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = re.compile(p + "$")
        results = re.match(pattern, s)
        if results:
            return True
        else:
            return False
