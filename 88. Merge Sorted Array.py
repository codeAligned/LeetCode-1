# 88. Merge Sorted Array
# Time: O(N)
# Space: O(1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1
        ptr2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if ptr1 >= 0 and ptr2 >= 0:
                if nums1[ptr1] >= nums2[ptr2]:
                    nums1[i] = nums1[ptr1]
                    ptr1 -= 1
                else:
                    nums1[i] = nums2[ptr2]
                    ptr2 -= 1
            elif ptr1 < 0:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1
            else:
                break