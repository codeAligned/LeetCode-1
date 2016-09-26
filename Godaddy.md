### Godaddy OA

*	Delete Node greater than X(LinkedList)

```cpp
// Time: O(n)
// Space: O(1)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode **ptr = &head;
        while (*ptr) {
            ListNode *temp = *ptr;
            if (temp->val == val) {
                *ptr = temp->next;
                free(temp);
            } else
                ptr = &(temp->next);
        }
        return head;
    }
};
```

---

*	next permutation

```cpp
// Time: O(N)
// Space: O(1)

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int k = -1;
        // Find the largest index k such that nums[k] < nums[k + 1]
    	for (int i = nums.size() - 2; i >= 0; i--) {
    		if (nums[i] < nums[i + 1]) {
    			k = i;
    			break;
    		}
    	} 
    	// If no such index exists, the permutation is the last permutation
    	if (k == -1) {
    	    reverse(nums.begin(), nums.end());
    	    return;
    	}
    	int l = -1;
    	// Find the largest index l greater than k such that nums[k] < nums[l]
    	for (int i = nums.size() - 1; i > k; i--) {
    		if (nums[i] > nums[k]) {
    			l = i;
    			break;
    		} 
    	} 
    	// Swap the value of nums[k] with that of nums[l]
    	swap(nums[k], nums[l]);
    	// Reverse the sequence from nums[k + 1] up to and including the final element nums[n].
    	reverse(nums.begin() + k + 1, nums.end()); 
    }
};
```

---

*	Merge Two Sorted Array: 将两个排序好的等长的array合并成一个

```cpp
// Time: O(N)
// Space: O(1)

// copy from the back
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int idx1 = m - 1, idx2 = n - 1;
        if (nums1.empty() || nums2.empty())
            return;
        int i;
        for (i = m + n - 1; i >= 0; --i) {
            if (idx2 >= 0 && idx1 >= 0)
                nums1[i] = (nums1[idx1] >= nums2[idx2]) ? nums1[idx1--] : nums2[idx2--];
            else
                break;
        }
        while (idx2 >= 0)
            nums1[i--] = nums2[idx2--];
    }
};
```

---

*   ZigZag Array: 最大，最小，第二大，第二小，第三大，第三小，....

```cpp
// Time:  O(n)
// Space: O(s.length())

class Solution {
public:
    string convert(string s, int numRows) {
        string result = "";
        if (numRows == 1)
            return s;
        int step1,step2, pos;
        int len = s.size();
        for (int i = 0; i < numRows; ++i){
            // generally 2 steps to get next character
            step1 = 2 * numRows - 2 * (i + 1); 
            step2 = 2 * i;
            pos = i;
            if (pos < len)
                result += s[pos]; // add first column
            while(1) { // keep iterating the 2 steps to get characters
                pos += step1;
                if (pos >= len) // detect overflow
                    break;
                if (step1) // last row only has step 2
                    result += s[pos];
                pos += step2;
                if (pos >= len)
                    break;
                if(step2) // first row only has step 1
                    result += s[pos];
            }
        }
        return result;
    }
};
```

---

*	Braces: 输入一个array，判断括号是不是balance，比如"([{}])"是balance，"([}]"not balanced. 输出也是一个array，balance输出Yes，not balance输出No

---

*	Missing Words: *  两个String s和t，t是s的subsequence。输出String[]，内容是s里有单t里没有的String。如String s = "I am a good boy", String t = "am good boy", 输出I a

---

*	Count Duplicates，计算给定数组里有重复的元素的个数。 eg. nums={1,1,2,2,2,3,4,3,9} return 3

---

*	Arranging coins：每一个层台阶放与台阶数相等的coins，返回最后一个放满的台阶数。eg. n=4, return 2; {1,2,1};

---

*   Same Elements in Two Arrays: 两个unsorted数组找出相同的数字，逆序输出

找出两个数组中重复的元素。如果有重复两次的数输出里面也要重复两次，但同一个item最多只能匹配一次。

>   Sort + 2 pointers: O(n logn) time + O(1) space.

---

*   String Compression. String限定由大小写字母组成: 简单地说，就是如果某个字母x连续出现c次，若c=1，则原样输出x；若c>1，则缩写成xc的格式

---

*   Subsequence, 可以参考subsets题，只不过由数字变为字符，而且不要空集

---

*	closest number

>   给一串数字（据说是以字符串的形式给的，如"1 2 3 4 5"），返回所有closest pairs。closest pair即两个数的差的绝对值最小。给定的数字没有排序，所以需要先转化为数组，然后排序。所有的pair都使用逗号隔开并依次显示。

---

*	三角形数问题，可以查wiki，有具体公式和解法。


