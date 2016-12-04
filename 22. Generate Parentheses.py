# 22. Generate Parentheses
# Time: O(n!)
# Space: O(2 * n + n!)

# backtracking
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lis, str = [], ""
        self.backtrack(lis, str, 0, 0, n);
        return lis;
    
    def backtrack(self, lis, str, left, right, cnt):
        if len(str) == cnt * 2:
            lis.append(str)
            return
        
        if left < cnt:
            self.backtrack(lis, str + "(", left + 1, right, cnt)
        if right < left:
            self.backtrack(lis, str + ")", left, right + 1, cnt)


# dynamic programming
# Generate one pair: ()
# Generate 0 pair inside, n - 1 afterward: () (...)...
# Generate 1 pair inside, n - 2 afterward: (()) (...)...
# ...
# Generate n - 1 pair inside, 0 afterward: ((...))
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n + 1)]
        dp[0].append("")
        for i in range (1, n + 1):
            for j in range(i):
                dp[i] += ["(" + x + ")" + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]