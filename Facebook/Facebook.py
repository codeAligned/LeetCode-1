#Facebook Tags on LeetCode
#Let’s do it!!!
#283. Move Zeroes
#in place moving zeroes to the end
class Solution(object):
    def moveZeroes(self, nums):
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1

#15. 3Sum
#sort list first, once got one num fixed, we can find the other two by searching 
#the rest of the list; be careful about the duplicates
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                low = i+1
                high = len(nums)-1
                s = 0 - nums[i]
                while low < high:
                    if nums[low] + nums[high] == s:
                        ret.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < s:
                        low += 1
                    else:
                        high -= 1
        return ret

		
#277. Find the Celebrity
#nice cut off of candidates, similar idea to union find		
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        for j in range(candidate):
            if knows(candidate, j):
                return -1
        for k in range(n):
            if not knows(k, candidate):
                return -1
        return candidate
		
#67. Add Binary
#key here: if one is used up, give it a nil value
#or we can use the slower method by adding zeros to make both number to be the same length
class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a) - 1
        n = len(b) - 1
        res = ''
        carry = 0
        while m >= 0 or n >= 0:
            numa = int(a[m]) if m >= 0 else 0
            numb = int(b[n]) if n >= 0 else 0
            s = numa + numb + carry
            res = str(s%2) + res
            carry = s/2
            m -= 1
            n -= 1
        return '1' + res if carry else res

#1. Two Sum
#multiple solutions. hash table for num, index
#1) hash on original 2) hash on sorted
#3) or create a new copy of the list and check target-num[i] in num[:i]+num[i+1:]
#4) or create a new copy of the list by sorted(nuts)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            try:
                d[num].append(i)
            except:
                d[num] = [i]

        for n in nums:
            try:
                tl = d[target-n]
                if target - n != n or len(d[n]) > 1:
                    ol = d[n]
                    break
                else:
                    continue
            except:
                pass
        for i in tl:
            for j in ol:
                if i != j:
                    return [i,j]

#91. Decode Ways
#solution 1 similar to dp fibonacci
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i > 1 and s[i-2:i] > '09' and s[i-2:i] < '27': #string comparisonL lexicographically
                dp[i] += dp[i-2]
        return dp[-1]
#dp2
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s)+1):
            if int(s[i-2:i]) <= 26 and int(s[i-2:i]) >= 10:
                dp[i] += dp[i-2]
            if int(s[i-1]) <= 9 and int(s[i-1]) >= 1:
                dp[i] += dp[i-1]
        return dp[-1]
		
#solution 2, O(1) fibonacci
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        c1 = 1
        c2 = 1
        for i in range(1, len(s)):
            if s[i] == '0': #c1 contributes nothing
                c1 = 0
            if s[i-1:i+1] > '09' and s[i-1:i+1] < '27': #store c1 for total, next c1 is previous c2, next result is previous c1
                c1, c2 = c1 + c2, c1
            else:  #c2 contributes nothing
                c2 = c1
        return c1

#285. Inorder Successor in BST
#recursive
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        def inorder(root, p):
            if not root:
                return root
            if root.val <= p.val:
                return inorder(root.right, p)
            else:
                left = inorder(root.left, p)
                if not left:
                    return root
                else:
                    return left
        return inorder(root, p)
#iterative
class Solution(object):
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ		
		
#139. Word Break
#be careful about the dp index
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(0, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

#23. Merge k Sorted Lists
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwo(node1, node2):
            head = cur = ListNode(0)
            while node1 and node2:
                if node1.val < node2.val:
                    cur.next = node1
                    node1 = node1.next
                else:
                    cur.next = node2
                    node2 = node2.next
                cur = cur.next
            cur.next = node1 if not node2 else node2
            return head.next
        
        if not lists:
            return None
        start = 0
        end = len(lists)-1
        while start != end or end != 0:
            if start >= end:
                start = 0
            else:
                lists[start] = mergeTwo(lists[start],lists[end])
                start += 1
                end -= 1
        return lists[start]

#76. Minimum Window Substring
'''
string minWindow(string s, string t) {
        vector<int> map(128,0);
        for(auto c: t) map[c]++;
        int counter=t.size(), begin=0, end=0, d=INT_MAX, head=0;
        while(end<s.size()){
            if(map[s[end++]]-->0) counter--; //in t
            while(counter==0){ //valid
                if(end-begin<d)  d=end-(head=begin);
                if(map[s[begin++]]++==0) counter++;  //make it invalid
            }  
        }
        return d==INT_MAX? "":s.substr(head, d);
    }	
'''	

#56. Merge Intervals
#be careful about merging, consider all cases of overlaps first
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            last = ret[-1]
            if last.end < interval.start:
                ret.append(interval)
            elif last.end < interval.end:
                last.end = interval.end
        return ret
		
#121. Best Time to Buy and Sell Stock		
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = prices[0]
        pro = 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            elif pro < prices[i] - low:
                pro = prices[i] - low
        return pro
		
#273. Integer to English Words	
class Solution(object):
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n/10-2]] + words(n%10)
            if n < 1000:
                return [to19[n/100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
			#enumerate can have initial starting point
                if n < 1000**(p+1):
                    return words(n/1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'

#98. Validate Binary Search Tree
#in order traversal		
class Solution(object):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True
    def inOrder(self, root, output):
        if root is None:
            return
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)

#alternative dfs solution, checking if each node's value satisfies the range
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(root, minvalue, maxvalue):
            if not root:
                return True
            if root.val <= minvalue or root.val >= maxvalue:
                return False
            else:
                return valid(root.left, minvalue, root.val) and valid(root.right, root.val, maxvalue)
        return valid(root, -float('inf'), float('inf'))
		
		
#301. Remove Invalid Parentheses
#bfs version		
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isvalid(s):
            plus = minus = 0
            for c in s:
                plus += {'(':1,')':-1}.get(c,0) #forward direction
                minus += plus < 0 #1 if True 0 if not, backwards direction
                plus = max(plus, 0)
            return plus + minus
        def dfs(s, visited, res, n):
            if n == 0:
                res.append(s)
                return
            for i in range(len(s)):
                if s[i] in ('(',')'):
                    new = s[:i]+s[i+1:]
                    if new not in visited and isvalid(new) < n:
                        visited.add(new)
                        dfs(new, visited, res, isvalid(new))
        res = []
        visited = set()
        miss = isvalid(s)
        dfs(s, visited, res, miss)
        return res

#stack/counter version
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def remove(s, res, lastIdx, lastRemove, ref):
            count = 0
            for i in range(lastIdx, len(s)):
                if s[i] == ref[0]:
                    count += 1
                if s[i] == ref[1]:
                    count -= 1
                if count >= 0:
                    continue
                for j in range(lastRemove, i+1):
                    if s[j] == ref[1] and (j == lastRemove or s[j-1] != ref[1]):
                        remove(s[:j]+s[j+1:], res, i, j, ref)
                return
            if ref == ["(", ")"]:
                remove(s[::-1], res, 0, 0, [")","("])
            else:
                if s != "":
                    res.append(s[::-1])
                else:
                    res.append("")
        res = []
        remove(s, res, 0, 0, ["(", ")"])
        return res


#206. Reverse Linked List
#classic methods of manipulating link lists
class Solution:
	# @param {ListNode} head
	# @return {ListNode}
	#iterative
	def reverseList(self, head):
		prev = None
		while head:
			curr = head
			head = head.next
			curr.next = prev
			prev = curr
		return prev	

	#recursive
    def reverseList(self, head):
        return self._reverse(head)
    
    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)	
		
#200. Number of Islands
#dfs, union find(on one linear array)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j, visited, grid):
            visited[i][j] = 1
            if i-1 >= 0 and grid[i-1][j] == '1' and visited[i-1][j] == 0:
                dfs(i-1, j, visited, grid)
            if i+1 < len(grid) and grid[i+1][j] == '1' and visited[i+1][j] == 0:
                dfs(i+1, j, visited, grid)
            if j-1 >= 0 and grid[i][j-1] == '1' and visited[i][j-1] == 0:
                dfs(i, j-1, visited, grid)
            if j+1 < len(grid[0]) and grid[i][j+1] == '1' and visited[i][j+1] == 0:
                dfs(i, j+1, visited, grid)
            return
        if not grid:
            return 0
        visited = [[0]*len(grid[0]) for i in range(len(grid))]
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    dfs(i, j, visited, grid)
                    ret += 1
        return ret

#sink islands method
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j, grid):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                if i < len(grid)-1:
                    dfs(i+1, j, grid)
                if i > 0:
                    dfs(i-1, j, grid)
                if j < len(grid[0])-1:
                    dfs(i, j+1, grid)
                if j > 0:
                    dfs(i, j-1, grid)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j, grid)
                    res += 1
        return res		
		
#75. Sort Colors
#Dutch national flag problem, 3-way partition (3-way quicksort)				
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        i = 0
        j = 0
        mid = 1
        
        while j <= n:
            if nums[j] < mid:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            elif nums[j] > mid:
                nums[j],nums[n] = nums[n],nums[j]
                n -= 1
            else:
                j += 1	
				
#78. Subsets
#recursive solution
#we can also use T/F table
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        def helper(ret, temp, nums):
            ret.append(temp)
            for i, num in enumerate(nums):
                helper(ret, temp+[num], nums[i+1:])
        helper(ret, [], nums)
        return ret

#125. Valid Palindrome		
# isalnum() --> very important
# ASCII: upper 65+ lower 97+ num 48+
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stripped_string = ''.join(ch for ch in s if ch.isalnum()).strip(' ').lower()
        reversed_string = stripped_string[::-1]
        if len(stripped_string) == 1 or len(stripped_string) == 0 or len(s)==1 or len(s)==0:
            return True
        if stripped_string == reversed_string:
            return True
        return False
		
#two pointer version, reduce space complexity		
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        low = 0
        high = len(s)-1
        while low <= high:
            while  low < high and not s[low].isalnum():
                low += 1
            while high > low and not s[high].isalnum():
                high -= 1
            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -= 1
        return True
		
#257. Binary Tree Paths
#dfs version		
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        ret = []
        if not root:
            return ret
        def dfs(root, temp, ret):
            if not root.left and not root.right:
                ret.append(temp+str(root.val))
            if root.left:
                dfs(root.left, temp+str(root.val)+'->', ret)
            if root.right:
                dfs(root.right, temp+str(root.val)+'->', ret)
        dfs(root, '', ret)
        return ret
		
#43. Multiply Strings	
#be careful about index
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        vector = [0]*(n1+n2)
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                vector[i+j+1] += (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
        carry = 0
        for k in range(n1+n2-1, -1, -1):
            vector[k] += carry
            carry = vector[k] / 10
            vector[k] = vector[k] % 10
        ret = ''
        index = 0
        while index < (n1+n2-1) and vector[index] == 0:
            index += 1
        for f in range(index, n1+n2):
            ret += str(vector[f])
        return ret	
		

#297. Serialize and Deserialize Binary Tree
#pre order way, borrowed this code; the use of iterators is beautiful		
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

#314. Binary Tree Vertical Order Traversal	
#hashtable problem, having each column as a different index
#can't use dfs, since lower level may contain nodes occuring before upper level nodes
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ht = {}
        stack = [(root, 0)]
        while stack:
            temp = []
            for r in stack:
                if r[1] not in ht:
                    ht[r[1]] = [r[0].val]
                else:
                    ht[r[1]].append(r[0].val)
                if r[0].left:
                    temp.append((r[0].left, r[1]-1))
                if r[0].right:
                    temp.append((r[0].right, r[1]+1))     
            stack = temp
        ret = []
        l = ht.keys()
        l.sort()

        for i in l:
            ret.append(ht[i])
        return ret


#173. Binary Search Tree Iterator	
#normal in-order traversal	
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        def pre(root, stack):
            if not root:
                return None
            pre(root.left, stack)
            stack.append(root.val)
            pre(root.right, stack)
        pre(root, self.stack)
        self.stack = self.stack[::-1]
            
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
        

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()
		
#stack version
class BSTIterator(object):
	def __init__(self, root):
		self.stack = []
		while root:
			self.stack.append(root)
			root = root.left

	# @return a boolean, whether we have a next smallest number
	def hasNext(self):
		return len(self.stack) > 0

	# @return an integer, the next smallest number
	def next(self):
		node = self.stack.pop()
		x = node.right
		while x:
			self.stack.append(x)
			x = x.left
		return node.val
	
#79. Word Search
#regular dfs method; defaultdict is a optimized version of dict, initialize key when not found
from collections import defaultdict
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
    def exist(self, board, word):
        char_to_pos = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[i])):
                char_to_pos[board[i][j]].append((i, j))
        return self._exist(char_to_pos, word, set())

    def _exist(self, char_to_pos, word, used, last_pos=None):
        if not word:
            return True
        for p in char_to_pos[word[0]]:
            if p in used or (last_pos and not self._is_pos_valid(p, last_pos)):
                continue
            used.add(p)
            if self._exist(char_to_pos, word[1:], used, p):
                return True
            used.remove(p)
        return False
        
    def _is_pos_valid(self, (i1, j1), (i2, j2)):
        return (i1 == i2 and abs(j1-j2) == 1) or (j1 == j2 and abs(i1-i2) == 1)
		
		
#212. Word Search II
#nice implementation of Trie class
class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode())
        root.word = word

class Solution(object):
    def search(self, i, j, root, board, m, n, r):
        char = board[i][j]
        if not (char and char in root.children):
            return

        board[i][j], root = None, root.children[char]

        if root.word:
            r.append(root.word)
            root.word = None

        for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ii, jj = i + x, j + y
            if 0 <= ii < m and 0 <= jj < n:
                self.search(ii, jj, root, board, m, n, r)

        board[i][j] = char

    def findWords(self, board, words):
        if not board:
            return []

        tree = Trie()
        [tree.insert(word) for word in words]

        m, n, r = len(board), len(board[0]), []

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                self.search(i, j, tree.root, board, m, n, r)
        return r
		
#49. Group Anagrams
#regular hashtable question		
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ref = {}
        ret = []
        for item in strs:
            new = ''.join(sorted(item))
            try:
                ref[new].append(item)
            except:
                ref[new] = [item]
        for key in ref.keys():
            ret.append(ref[key])
        return ret
		
#398. Random Pick Index
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        last = -1
        for i, n in enumerate(self.nums):
            if n == target:
                rnd = random.randint(0, count)
                if rnd == 0:
                    last = i
                count += 1
        return last  
		
#146. LRU Cache
#ordered dict
class LRUCache(object):
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity
    
    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v   # set key as the newest one
        return v
    
    def set(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) 
        self.dic[key] = value 
		
		
#133. Clone Graph
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def dfs(node, d):
            if not node:
                return None
            if node not in d: #dfs only push forward if seeing unvisited node
                d[node] = UndirectedGraphNode(node.label)
                d[node].neighbors += [dfs(n, d) for n in node.neighbors] #beautiful way of saving data as well as moving forward
            return d[node]
        return dfs(node, {})
	
#311. Sparse Matrix Multiplication
#basic hashtable problem	
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
		#matrix multiplication initialization
        m, n, l = len(A), len(A[0]), len(B[0])
        C = [[0 for _ in range(l)] for _ in range(m)]
        tableB = {}
        for k, row in enumerate(B):
            tableB[k] = {}
            for j, eleB in enumerate(row):
                if eleB: tableB[k][j] = eleB
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in tableB[k].iteritems():
                        C[i][j] += eleA * eleB
        return C
#two table version
#raw complexity O(m*n*l)
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None:
            return None
        m = len(A)
        n = len(A[0])
        l = len(B[0])
        C = [[0 for _ in range(l)] for _ in range(m)]
        tableA = {}
        tableB = {}
        for k, row in enumerate(A):
            tableA[k] = {}
            for j, eleA in enumerate(row):
                if eleA:
                    tableA[k][j] = eleA
        for k, row in enumerate(B):
            tableB[k] = {}
            for j, eleB in enumerate(row):
                if eleB:
                    tableB[k][j] = eleB
        for i in tableA.keys():
            for k, eleA in tableA[i].iteritems():
                if tableB.get(k, 0):
                    for j, eleB in tableB[k].iteritems():
                        C[i][j] += eleA*eleB
        return C
		
#two table with defaultdict version
from collections import defaultdict
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None:
            return None
        m = len(A)
        n = len(A[0])
        l = len(B[0])
        C = [[0 for _ in range(l)] for _ in range(m)]
        tableA = defaultdict(lambda: defaultdict(list))
        tableB = defaultdict(lambda: defaultdict(list))
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    tableA[i][k] = eleA
        for k, row in enumerate(B):
            for j, eleB in enumerate(row):
                if eleB:
                    tableB[k][j] = eleB
        for i in tableA.keys():
            for k in tableA[i].keys():
                for j in tableB[k].keys():
                    C[i][j] += tableA[i][k]*tableB[k][j]
        return C
#38. Count and Say		
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        prev=""
        cur="1"
        for i in range(n-1):
            prev=cur
            cur=""
            cnt=1
            for s in range(len(prev)):
                if s+1<len(prev) and prev[s]==prev[s+1]:
                    cnt+=1
                else:
                    cur=cur+str(cnt)+str(prev[s])
                    cnt=1
        return cur
		
#158. Read N Characters Given Read4 II - Call multiple times		
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        import collections
        self.Queue = collections.deque([])
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        numReadTotal = 0
        localBuf     = [''] * 4
        while numReadTotal < n:
            if not self.Queue: # *Try* to read more content
                numRead = read4(localBuf) 
                self.Queue.extend(localBuf[0:numRead])
    
            if self.Queue: # Can be empty if we do not have anything left to read
                buf[numReadTotal] = self.Queue.popleft()
                numReadTotal += 1
            else:
                break
        return numReadTotal      

#236. Lowest Common Ancestor of a Binary Tree		
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:  return p
        if p == root or q == root:  return root
        parent_dic = {}
        def dfs(root,parent_dic):
            if root.left:
                parent_dic[root.left] = root
                dfs(root.left,parent_dic)
            if root.right:
                parent_dic[root.right] = root
                dfs(root.right,parent_dic)
            return 
        dfs(root,parent_dic)
        dummy = TreeNode(0)
        parent_dic[root],p_path = dummy,[]
        while(p != dummy):
            p_path.append(p)
            p = parent_dic[p]
        while(q != dummy):
            if q in p_path: return q
            else:   q = parent_dic[q]

#iterative solution, using dfs with stack
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left: #doesn’t matter which one goes first
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestor = []
        while p:
            ancestor.append(p)
            p = parent[p]
        while q not in ancestor:
            q = parent[q]
        return q
#really beautiful recursive solution
#each step returns p/q/null
#only when both sides are not null, root is returned
#otherwise, return the previous step
#once root is returned, it will be covered anyways since for the bottom up approach, this only happens once
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root

#208. Implement Trie (Prefix Tree)
#nice dictionary problem, defaultdict used here			
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False       

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True         

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word
    

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True   

#211. Add and Search Word - Data structure design
#trie
class Trie(object):

    def __init__(self):
        self.children = [None] * 27

    def add(self, word):
        if not word:
            self.children[26] = Trie()
            return
        w = word[0]
        ind = ord(w) - ord('a')
        if not self.children[ind]:
            self.children[ind] = Trie()
        self.children[ind].add(word[1:])

    def has(self, word):
        if not word:
            return self.children[26] != None
        w = word[0]
        if w == '.':
            for child in self.children:
                if child and child.has(word[1:]):
                    return True
            return False
        ind = ord(w) - ord('a')
        if self.children[ind]:
            return self.children[ind].has(word[1:])
        else:
            return False
            
class WordDictionary(object):
    def __init__(self):
        self.trie = Trie()
        
    def addWord(self, word):
        self.trie.add(word)
        
    def search(self, word):
        return self.trie.has(word)	


#57. Insert Interval
#insert the new one and remove overlaps			
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x.start)
        stack = [intervals[0]]
        i = 1
        while i < len(intervals):
            cur = stack[-1]
            new = intervals[i]
            if new.start <= cur.end:
                stack.pop()
                stack.append(Interval(min(new.start, cur.start), max(new.end, cur.end)))
            else:
                stack.append(new)
            i += 1
        return stack

#161. One Edit Distance
#guaranteed one distance apart        
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                elif len(s) < len(t):
                    return s[i:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]
        return abs(len(s)-len(t)) == 1	
        
#282. Expression Add Operators 
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res
    
    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)     
 
#209. Minimum Size Subarray Sum
#be very careful about the binary search                
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sums = [0]
        for i in range(0, len(nums)):
            sums.append(sums[-1]+nums[i])
        res = float('inf')
        for i in range(len(nums)):
            left = i+1
            right = len(nums)
            t = sums[i]+s
            while left <= right:
                mid = left + (right-left)/2
                if sums[mid] < t:
                    left = mid+1
                else:
                    right = mid-1
            if left == len(sums):
                break
            res = min(res, left-i)
        return res if res != float('inf') else 0  
		
#128. Longest Consecutive Sequence
#decent union-find solution
#item in set -> O(n)                
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for n in nums:
            if n-1 not in nums:
                m = n+1
                while m in nums:
                    m += 1
                best = max(best, m-n)
        return best
 
        
#127. Word Ladder
#beautiful set manipulation
#set intersect, union, difference can be calculated with & | -    
#list(string.ascii_lowercase) gives all chars    
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        front, back=set([beginWord]), set([endWord]) 
        length=2
        width=len(beginWord)
        charSet=list(string.ascii_lowercase)
        wordList.discard(beginWord)
        wordList.discard(endWord)
        while front:
            newFront=set()
            for phrase in front:
                for i in xrange(width):
                    for c in charSet:
                        nw=phrase[:i]+c+phrase[i+1:]
                        if nw in back:
                            return length
                        if nw in wordList:
                            newFront.add(nw)
            front=newFront
            if len(front)>len(back):
                front,back=back,front
            wordList-=front
            length+=1
        return 0

#68. Text Justification        
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def justify_line(templist, templen):
            n = len(templist)
            if n == 1: 
            	return templist[0].ljust(maxWidth)
            space_count = maxWidth - templen
            space_location = space_count / (n-1) + 1 #this is because the initialization of the templen includes an space after each word
            space_remain = space_count % (n-1)
            r = ''
            for i in range(n-1):
                if i < space_remain:
                    r += templist[i] + ' ' * (space_location+1)
                else:
                    r += templist[i] + ' ' * (space_location)
            r += templist[n-1]
            return r
        
        templen, templist, res = -1, [], []
        for word in words:
            templen += len(word) + 1
            if templen > maxWidth:
                res.append(justify_line(templist, templen - len(word) - 1))
                templist = [word]
                templen = len(word)
            else:
                templist.append(word)
        if len(templist) > 0:
        	#ljust(width, fillchar) : left justify with fillchar
            res.append(" ".join(templist).ljust(maxWidth))
        return res
		

#404. Sum of Left Leaves
#use of a tag to indicate if it is a left child		
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, count, left):
            if not node:
                return 0
            if node.left or node.right:
                return dfs(node.left, count, 1) + dfs(node.right, count, 0)
            else:
                return node.val if left else 0
        return dfs(root, 0, 0)
	

#157. Read N Characters Given Read4	
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while n > 0:
            buf4 = ['']*4
            l = read4(buf4)
            if not l:
                return idx
            for i in range(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx
		
		
#410. Split Array Largest Sum		
#very clean binary search solution
#need to find out if each of the limit is valid
#impossible if looking for subarray
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        high = sum(nums)
        low = high/len(nums) #if we set this, we must ensure that no individual number can be greater than the limit
        
        def isValid(limit):
            cur = 0
            count = 0
            for item in nums:
                if item > limit: #don't need these two lines if set low to the largest num
                    return False #
                cur += item
                if cur > limit:
                    count += 1
                    if count >= m:
                        return False
                    cur = item
            return True
        
        while low < high:
            mid = low + (high-low)/2
            if isValid(mid):
                high = mid
            else:
                low = mid + 1
        return low

#85. Maximal Rectangle
#beautiful solution with stack		
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0]*(n+1)
        ret = 0
        for row in matrix:
            #converting to max rectangle on each row, swipe down and update
            for i in range(n):
                #if discontinued, height become zero
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1] #-1 position has height of zero
            for i in range(n+1):
                while height[i] < height[stack[-1]]:
                    #while loop calculates max area before i
                    #height must be increasing before i
                    #after each loop, i become the max height
                    h = height[stack.pop()]
                    w = i-1-stack[-1]
                    ret = max(ret, h*w)
                stack.append(i)
        return ret
		
#240. Search a 2D Matrix II		
#divide and couquer, binary search
#key idea is that the increasing order of the matrix		
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ref = len(matrix[0])
        for row in matrix:
            if target > row[-1]:
                continue
            low = 0
            high = ref
            while low <= high:
                mid = low + (high-low)/2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            ref = low #here low means the upper bound
			#[n + (n+1)]/2 = n; int(3.9) = 3
			#python2: division just use '/'
			#python3: integer division need to be '//'
        return False

#278. First Bad Version
#high is kept as the lowest bad version for known at each iteration		
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return False
        low = 0
        high = n
        while low < high:
            mid = low + (high-low)/2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return high
		
		
#116. Populating Next Right Pointers in Each Node
#work on each level since this is a perfect binary tree		
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        pre = root
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
			

#117. Populating Next Right Pointers in Each Node II
#level order traversal			
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        cur = root #current node at current level
        prev = None #leading node at next level
        head = None #head node at next level
        while cur:
            #going in each level
            while cur:
                #left child
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left
                #right child
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                cur = cur.next
            cur = head
            prev = None
            head = None
			
			
#0.1 task cooldown problem
#hashtable to store the last finishing time of each task
def getCompleteTime(tasks, waitBetweenRepeatedTask):
	time = 0	# clock
	record = {}	# record[t] represents last time t is done
	for t in tasks:
		if t in record and time - record[t] < waitBetweenRepeatedTask:
			# wait the cooldown
			time = record[t] + waitBetweenRepeatedTask
		# execute t
		time += 1
		# update record
		record[t] = time
	return time
#to find the best sequence, we need to use a maxheap
def fastestTaskSequence(tasks, n):
	#because all items have the same cool down, we check their frequency
	frequencies = dict()
	a = []
	for ch in tasks:
		if ch in frequencies:
			frequencies[ch] += 1
		else:
			frequencies[ch] = 1
	#push all items into the maxheap
	#the reason for maxheap is to make sure later items are depleted first
	#in this way we make sure that each item satisfied the cool down
	for key, val in frequencies.iteritems():
		maxheappush(a, [val, key])
	result = ''
	while len(a):
		temp = []
		for i in range(n+1):
			if len(a):
				task = maxheappop(a)
				result += task[1]
				temp.append(task)
			else:
				break
		itemPushed = len(temp)
		while len(temp):
			task = temp.pop()
			task[0] -= 1
			if task[0] > 0:
				maxheappush(a, task)
		if len(a):
			result += '_' * (n+1-itemPushed)
	return result
	
#50. Pow(x, n)
#iterative, recursive, bit manipulation	
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x, n):
            if n == 0:
                return 1
            if n%2 == 0:
                return power(x*x, n/2)
            else:
                return power(x*x, n/2)*x
        if n < 0:
            return power(1/x,-n)
        else:
            return power(x, n)
#bit version			
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x, n):
            if n == 0:
                return 1
            if n&1:
                return power(x*x, n>>1)*x
            else:
                return power(x*x, n>>1)
        if n < 0:
            return power(1/x,-n)
        else:
            return power(x, n)

#69. Sqrt(x)
#binary search			
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        low = 1 #lower limit set to 1
        high = x
        while low <= high:
            mid = low + (high-low)/2
            if mid <= x/mid:
                if mid+1 > x/(mid+1): #important check to avoid missing the correct solution
                    return mid
                low = mid + 1
            else:
                high = mid - 1
				
#252. Meeting Rooms				
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
		
#253. Meeting Rooms	II
#overloading comparators in python
#def __lt__(self, other): or cmp
#    return self.intAttribute < other.intAttribute
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = []
        heapq.heappush(heap, (intervals[0].end, intervals[0]))
		#python built-in heapq is a min heap
		#we can only use tuple sort by attribute if we dont change the interval definition
		#tuples will be sorted by the first element
        for i in range(1, len(intervals)):
            interval = intervals[i]
            last = heapq.heappop(heap)[1]
            if interval.start >= last.end:
                last.end = interval.end
            else:
                heapq.heappush(heap, (interval.end, interval))
            heapq.heappush(heap, (last.end, last))
        return len(heap)		



#0.2 json parser
#Pretty print a json object using proper indentation
def jsonReader(s):
	res = []
	indent = ""
	cur = ""
	if len(s) == 0:
		return ret
	i = 0
	while i < len(s):
		key = s[i]
		cur += key
		if key == ",":
			res.append(cur)
			cur = indent
			i += 1
		elif key == ":":
			i += 1
			if s[i] == "{" or s[i] == "[":
				res.append(cur)
				cur = indent
		elif key == "{" or key == "[":
			i += 1
			res.append(cur)
			if s[i] != "]" and s[i] != "}":
				indent += "\t"
			cur = indent
		elif key == "]" or key == "}":
			i += 1
			if i < len(s) and s[i] == ",":
				continue
			res.append(cur)
			if i < len(s) and (s[i] != "]" or s[i] != "}"):
				if len(indent) > 0:
					indent = indent[:-1]
				cur = indent
		else:
			i += 1
			if i < len(s) and (s[i] == "]" or s[i] == "}"):
				res.append(cur)
				if len(indent) > 0:
					indent = indent[:-1]
				cur = indent
	return res
			
#380. Insert Delete GetRandom O(1)	
#important to keep track of the positions
#very smart idea of removing		
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums)-1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            idx = self.pos[val]
            last = self.nums[-1]
            self.nums[idx] = last
            self.pos[last] = idx
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums)-1)]
		

#221. Maximal Square
#smart dp solution		
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = 0
        dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == '1':
					#key point of updating
                    dp[i][j] = min([dp[i-1][j], dp[i-1][j-1], dp[i][j-1]])+1
                    res = max(dp[i][j], res)
        return res*res
		
#210. Course Schedule II
#topological sort, finding zero indegrees and use bfs (dfs) works as well
#for scenarios like this problem, a regular dictionary should work
#key point is that it's possible that not all courses are included in the pre-req		
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list) #graph initialization
        count = collections.defaultdict(int) #indegree count
        for i in range(numCourses):
            graph[i] = []
            count[i] = 0
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            count[edge[0]] += 1
        tovisit = collections.deque()
        for node in graph.keys():
            if count[node] == 0:
                tovisit.append(node)
        res = []
        while len(tovisit) > 0:
            cur = tovisit.popleft()
            res.append(cur)
            for nxt in graph[cur]:
                count[nxt] -= 1
                if count[nxt] == 0:
                    tovisit.append(nxt)
        #when a cycle occurs, some parts of the graph will not be included
        #this will cause the result to be less than the required courses
        return res if len(res) == numCourses else []
		
		
#265. Paint House II	
#very nice dp idea
#need to revisit
#basic idea is to keep min for each house with color j, and another min for the house without color j-1
#the two conditions will contribute to the next ones
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])
        prevMin = 0
        prevInd = -1
        secondMin = 0
        
        for i in range(n):
            mi = float('inf')
            miId = -1
            sec = float('inf')
            for j in range(k):
                val = costs[i][j] + secondMin if j == prevInd else costs[i][j] + prevMin
                if miId < 0: #initialize the min for each house
                    mi = val
                    miId = j
                elif val < mi: #two step eval, find min and second min
                    sec = mi
                    mi = val
                    miId = j
                elif val < sec:
                    sec = val
            prevMin = mi
            prevInd = miId
            secondMin = sec
        return prevMin
		
#25. Reverse Nodes in k-Group
#recursive swap, be careful about the corner cases, if the remaining nodes are less than k, we don't swap		
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        #checking if there are at least k remaining nodes
        while cur and count != k:
            cur = cur.next
            count += 1
        #reverse k nodes starting from head: (k+1)th node
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head
		
#269. Alien Dictionary
#topological sort problem		
import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        #different from course scheduling, because same edge can occur multiple times
        graph = collections.defaultdict(set)  #graph initialization
        degree = collections.defaultdict(set) #indegree (edges) of each char
        clist = {}  #character list
        for i in range(len(words)):
            w = words[i]
            for c in w:
                clist[c] = True
            if i < len(words)-1:
                wnxt = words[i+1]
                p, q = 0, 0
				#pair-wise comparison is the key here
                while p < len(w) and q < len(wnxt):
                    if w[p] != wnxt[q]:
                        graph[w[p]].add(wnxt[q])
                        degree[wnxt[q]].add(w[q])
                        break
                    else:
                        p += 1
                        q += 1
                if len(w) > len(wnxt) and q == len(wnxt):
                    return ''
        #regular topological sort
        order = []
        tovisit = collections.deque()
        for c in clist:
            if len(degree[c]) == 0:
                tovisit.append(c)
        while len(tovisit) > 0:
            ch = tovisit.popleft()
            order.append(ch)
            for nxt in graph[ch]:
                degree[nxt].remove(ch)
                if len(degree[nxt]) == 0:
                    tovisit.append(nxt)
        return ''.join(order) if len(order) == len(clist) else ''
		
#377. Combination Sum IV
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [0]*(target+1)
        for i in range(1, target+1):
            for n in nums:
                if n > i:
                    break
                elif n == i:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-n]
        return dp[target]

		
#218. The Skyline Problem
#not the code I wrote, need to revisit
import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        def addsky(pos, height):
            if sky[-1][1] != height:
                sky.append([pos, height])

        sky = [[-1,0]]
        # possible corner positions
        position = set([b[0] for b in buildings] + [b[1] for b in buildings])
        
        # live buildings
        live = []
        i = 0
        for t in sorted(position):
            # add the new buildings whose left side is lefter than position t
            # nice use of priority queue
            while i < len(buildings) and buildings[i][0] <= t:
                heapq.heappush(live, (-buildings[i][2], buildings[i][1])) # need neg since built-in is a min-heap
                i += 1
            # remove the past buildings whose right side is lefter than position t
            while live and live[0][1] <= t:
                heapq.heappop(live)
            # pick the highest existing building at this moment
            h = -live[0][0] if live else 0
            addsky(t, h)
    
        return sky[1:]

#44. Wildcard Matching
#linear-like solution, less than n^2 for sure
#basically when a * is found, match the following elements, if a no-match is found, move on to the next one to match
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ids = 0
        idp = 0
        match = 0 #first position that needs to be matched
        star = -1 #last * location
        
        while ids < len(s):
            if idp < len(p) and (s[ids] == p[idp] or p[idp] == '?'):
                ids += 1
                idp += 1
            elif idp < len(p) and p[idp] == '*':
                star = idp
                match = ids
                idp += 1
            elif star != -1:
                idp = star + 1
                match += 1
                ids = match
            else:
                return False
        while idp < len(p) and p[idp] == '*':
            idp += 1
        return idp == len(p)

#325. Maximum Size Subarray Sum Equals k
#ht solution
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = []
        s = 0
        for n in nums:
            s += n
            total.append(s)
        l = 0
        ht = {0:-1}
        for i in range(len(total)):
            if total[i]-k in ht:
                l = max(l, i - ht[total[i]-k])
            if total[i] not in ht:
                ht[total[i]] = i
        return l

#215. Kth Largest Element in an Array		
#quick sort solution
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #after returning, all numbers before 'r' is greater than or equal to pivot
        #all numbers after 'r' is smaller than pivot
        def partition(nums, left, right):
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[left], nums[r] = nums[r], nums[left]
            return r
 
        left = 0
        right = len(nums) - 1
        while True:
            pivot = partition(nums, left, right)
            if pivot == k-1:
                return nums[pivot]
            elif pivot < k-1:
                left = pivot + 1
            else:
                right = pivot - 1
				
#332. Reconstruct Itinerary
#nice dfs solution, sort needed for lex order
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def route_helper(origin, ticket_cnt, graph, ans):
            if ticket_cnt == 0:
                return True

            for i, (dest, valid)  in enumerate(graph[origin]):
                if valid:
                    graph[origin][i][1] = False #beautiful way of labeling visited nodes
                    ans.append(dest)
                    if route_helper(dest, ticket_cnt - 1, graph, ans):
                        return ans
                    ans.pop()
                    graph[origin][i][1] = True
            return False

        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append([ticket[1], True])
        for k in graph.keys():
            graph[k].sort()

        origin = "JFK"
        ans = [origin]
        route_helper(origin, len(tickets), graph, ans)
        return ans
		
#34. Search for a Range
#search for left and then search for right		
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Find the first index where target <= nums[idx]
        left = self.binarySearch(lambda x, y: x >= y, nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        # Find the first index where target < nums[idx]
        right = self.binarySearch(lambda x, y: x > y, nums, target)
        return [left, right - 1]
    
    def binarySearch(self, compare, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) / 2
            if compare(nums[mid], target):
                right = mid
            else:
                left = mid + 1
        return left

    def binarySearch2(self, compare, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if compare(nums[mid], target):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def binarySearch3(self, compare, nums, target):
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = left + (right - left) / 2
            if compare(nums[mid], target):
                right = mid
            else:
                left = mid
        return right
		
#126. Word Ladder II		
# BFS
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        
        result, cur, visited, found, trace = [], [start], set([start]), False, {word: [] for word in dict}  

        while cur and not found:
            for word in cur:
                visited.add(word)
                
            next = set()
            for word in cur:
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in dict:
                            if candidate == end:
                                found = True
                            next.add(candidate)
                            trace[candidate].append(word)
            cur = next
            
        if found:
            self.backtrack(result, trace, [], end)
        
        return result
    
    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)
				
#317. Shortest Distance from All Buildings
#need to keep track of the distance from one node to all buildings	
#use a count to indicate that a node is reachable from n buildings			
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(grid, dists, cnts, x, y):
            dist, m, n = 0, len(grid), len(grid[0])
            visited = [[False for _ in xrange(n)] for _ in xrange(m)]
    
            pre_level = [(x, y)]
            visited[x][y] = True
            while pre_level:
                dist += 1
                cur_level = []
                for i, j in pre_level:
                    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        I, J = i+dir[0], j+dir[1]
                        if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and not visited[I][J]:
                            cnts[I][J] += 1
                            dists[I][J] += dist
                            cur_level.append((I, J))
                            visited[I][J] = True
    
                pre_level = cur_level


        m, n, cnt = len(grid),  len(grid[0]), 0
        dists = [[0 for _ in xrange(n)] for _ in xrange(m)]
        cnts = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    cnt += 1
                    bfs(grid, dists, cnts, i, j)

        shortest = float("inf")
        for i in xrange(m):
            for j in xrange(n):
                if dists[i][j] < shortest and cnts[i][j] == cnt:
                    shortest = dists[i][j]

        return shortest if shortest != float("inf") else -1
		
#186. Reverse Words in a String II		
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        def reverse(s, begin, end):
            for i in xrange((end - begin) / 2):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]

        reverse(s, 0, len(s))
        i = 0
        for j in xrange(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                reverse(s, i, j)
                i = j + 1
				

#229. Majority Element II
#reservoir sampling for 3 elements				
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k, n, cnts = 3, len(nums), collections.defaultdict(int)

        for i in nums:
            cnts[i] += 1
            # Detecting k items in cnts, at least one of them must have exactly
            # one in it. We will discard those k items by one for each.
            # This action keeps the same mojority numbers in the remaining numbers.
            # Because if x / n  > 1 / k is true, then (x - 1) / (n - k) > 1 / k is also true.
            if len(cnts) == k:
                for j in cnts.keys():
                    cnts[j] -= 1
                    if cnts[j] == 0:
                        del cnts[j]

        # Resets cnts for the following counting.
        for i in cnts.keys():
            cnts[i] = 0

        # Counts the occurrence of each candidate integer.
        for i in nums:
            if i in cnts:
                cnts[i] += 1

        # Selects the integer which occurs > [n / k] times.
        result = []
        for i in cnts.keys():
            if cnts[i] > n / k:
                result.append(i)
		return result
		
#382. Linked List Random Node				
from random import randint
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.__head = head


    # Proof of Reservoir Sampling:
    # https://discuss.leetcode.com/topic/53753/brief-explanation-for-reservoir-sampling
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        reservoir = self.__head.val
        curr, n = self.__head.next, 1
        while curr:
            reservoir = curr.val if randint(1, n+1) == 1 else reservoir
            curr, n = curr.next, n+1
        return reservoir

        
		
#300. Longest Increasing Subsequence
#binary search solution		
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        def insert(target):
            left, right = 0, len(LIS) - 1
            # Find the first index "left" which satisfies LIS[left] >= target
            while left <= right:
                mid = left + (right - left) / 2;
                if LIS[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target);
            else:
                LIS[left] = target

        for num in nums:
            insert(num)

        return len(LIS)

# Time:  O(n^2)
# Space: O(n)
# Traditional DP solution.
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []  # dp[i]: the length of LIS ends with nums[i]
        for i in xrange(len(nums)):
            dp.append(1)
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0
		
#304. Range Sum Query 2D - Immutable
#calculate sum at each position, then get asked range
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        self.__sums = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                self.__sums[i][j] = self.__sums[i][j-1] + matrix[i-1][j-1]
        for j in xrange(1, n+1):
            for i in xrange(1, m+1):
                self.__sums[i][j] += self.__sums[i-1][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.__sums[row2+1][col2+1] - self.__sums[row2+1][col1] - \
               self.__sums[row1][col2+1] + self.__sums[row1][col1]