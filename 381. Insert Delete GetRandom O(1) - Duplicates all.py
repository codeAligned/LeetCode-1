# 381. Insert Delete GetRandom O(1) - Duplicates allowed
# Time: O(1)
# Space: O(N)

class RandomizedCollection(object):
    # use list to save numbers, use dictionary with sets as value to save positions with duplicate key
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        if val not in self.pos:
            self.pos[val] = set([len(self.nums) - 1])
            return True
        else:
            self.pos[val].add(len(self.nums) - 1)
            return False
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            del_idx, last_idx = self.pos[val].pop(), len(self.nums) - 1
            self.nums[del_idx] = self.nums[last_idx] # overwrite out element with last element
            last = self.nums[last_idx]
            if del_idx != last_idx: # if out and last not the same index, update pos dictionary
                self.pos[last].remove(last_idx)
                self.pos[last].add(del_idx)
            self.nums.pop()
            if len(self.pos[val]) == 0:
                self.pos.pop(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        r = random.randrange(len(self.nums))
        return self.nums[r]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()