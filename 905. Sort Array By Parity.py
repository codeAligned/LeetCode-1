# 905. Sort Array By Parity
# Time:  O(N)
# Space: O(N)

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_list = []
        even_list = []
        for num in A:
            if num % 2 == 1:
                odd_list.append(num)
            else:
                even_list.append(num)
        return even_list + odd_list