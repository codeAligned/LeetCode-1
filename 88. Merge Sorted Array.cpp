// 88. Merge Sorted Array
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