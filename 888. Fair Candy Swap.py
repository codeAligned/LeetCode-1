# 888. Fair Candy Swap
# Time: O(N)
# Space: O(N)

# use the fact that final sum is the average of sum_A + sum_B
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A, sum_B = sum(A), sum(B)
        set_A, set_B = set(A), set(B)
        final_sum = (sum_A + sum_B) // 2
        for num in set_A:
            if final_sum - (sum_A - num) in set_B:
                return [num, final_sum - (sum_A - num)]
