# 537. Complex Number Multiplication
# Time: O(1)
# Space: O(1)

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x, y = a.split("+")
        i1, j1 = int(x), int(y[:-1])
        x, y = b.split("+")
        i2, j2 = int(x), int(y[:-1])
        return "{}+{}i".format(i1 * i2 - j1 * j2, i1 * j2 + i2 * j1)