# 384. Shuffle an Array
# Time:  O(n)
# Space: O(n)

# random.random(): 0.0 <= x < 1.0
# random.uniform(1, 10): 1.0 <= x < 10.0
# random.randint(a, b): a <= x <= b
# random.randrange(a, b, d)
# random.shuffle(list)
# random.choice(list or str)
# random.sample(list, size)

# del list[index]

class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums2 = self.nums[:]
        for i in range(len(nums2)):
            j = random.randint(0, len(nums2) - 1 - i)
            nums2[i], nums2[i + j] = nums2[i + j], nums2[i]
        return nums2


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()