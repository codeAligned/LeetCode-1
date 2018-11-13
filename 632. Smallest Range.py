# 632. Smallest Range
# Time: O(len(nums)*len(nums[0])*log(len(nums)))
# Space: O(len(nums))

# multiple pointers to track, and use a min heap to find min num faster
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pointers = [0] * len(nums)
        range_res = [float('inf'), float('inf'), 0]
        min_heap = []
        min_num, max_num, min_idx = float('inf'), float('-inf'), 0
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i))
            max_num = max(max_num, nums[i][0])
        while True:
            min_num, min_idx = heapq.heappop(min_heap)
            diff = max_num - min_num
            if diff < range_res[0]:
                range_res[0] = diff
                range_res[1] = min_num
                range_res[2] = max_num
            elif diff == range_res[0] and min_num < range_res[1]:
                range_res[0] = diff
                range_res[1] = min_num
                range_res[2] = max_num
            pointers[min_idx] += 1
            if pointers[min_idx] >= len(nums[min_idx]):
                break
            new_num = nums[min_idx][pointers[min_idx]]
            heapq.heappush(min_heap, (new_num, min_idx))
            max_num = max(max_num, new_num)
        return range_res[1:]
