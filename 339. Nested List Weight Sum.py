# 339. Nested List Weight Sum
# Time: O(N)
# Space: O(N)

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# bfs using queue
from collections import deque
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """ 
        sum = 0
        queue = deque()
        for item in nestedList:
            queue.append((item, 1))
        while queue:
            item, depth = queue.popleft()
            if item.isInteger():
                sum += item.getInteger() * depth
            else:
                for item2 in item.getList():
                    queue.append((item2, depth + 1))
        return sum

# dfs using recursive
class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """ 
        def dfs(nestedList, depth):
            sum = 0
            for item in nestedList:
                if item.isInteger():
                    sum += item.getInteger() * depth
                else:
                    sum += dfs(item.getList(), depth+1)
            return sum
        return dfs(nestedList, 1)

