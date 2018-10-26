# 846. Hand of Straights
# Time: O(N)
# Space: O(N)

# maintain a min heap and a counter dict
from collections import defaultdict

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        cnt_dict = defaultdict(int)
        heap = []
        for num in hand:
            cnt_dict[num] += 1
            heapq.heappush(heap, num)
        while len(cnt_dict):
            min_num = -1
            while min_num not in cnt_dict: # get the min num that's in the cnt dict
                min_num = heapq.heappop(heap)
            for i in range(min_num, min_num + W):
                if i not in cnt_dict:
                    return False
                cnt_dict[i] -= 1
                if cnt_dict[i] == 0:
                    cnt_dict.pop(i)
            
        return True