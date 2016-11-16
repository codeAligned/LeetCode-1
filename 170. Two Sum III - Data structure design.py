# 170. Two Sum III - Data structure design
# Time: O(1)
# Space: O(N)

# dictionary to solve two sum
class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.dic = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.dic:
            self.dic[number] += 1
        else:
            self.dic[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        dic = self.dic
        for num in dic:
            if value - num in dic and (value - num != num or dic[num] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)