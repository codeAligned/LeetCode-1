# 556. Next Greater Element III
# Time: O(N)
# Space: O(N)

# from tail to head find the first decreasing pair
# and then swap the left one with from tail to head first larger num
# reverse the tail starting from the right one
# check result should less than 2^31
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_str_list = list(str(n))
        for i in range(len(n_str_list) - 1, 0, -1): # from tail to head find the first decreasing pair
            if n_str_list[i] > n_str_list[i-1]:
                for j in range(len(n_str_list) - 1, i - 1, -1):
                    if n_str_list[j] > n_str_list[i-1]: # and then swap the left one with from tail to head first larger num
                        n_str_list[j], n_str_list[i-1] = n_str_list[i-1], n_str_list[j]
                        break
                n_str_list[i:] = n_str_list[i:][::-1] # reverse the tail starting from the right one
                res = int(''.join(n_str_list)) 
                return res if res < 2**31 else -1 # check result should less than 2^31
        return -1
