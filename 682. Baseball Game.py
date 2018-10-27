# 682. Baseball Game
# Time: O(N)
# Space: O(N)

# str.isdigit() not true for negative numbers.
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = []
        for op in ops:
            if op == 'D':
                res.append(2*res[-1])
            elif op == 'C':
                res.pop()
            elif op == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(op))
        return sum(res)
