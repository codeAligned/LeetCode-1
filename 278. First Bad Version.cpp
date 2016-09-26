// 278. First Bad Version.cpp
// Time:  O(logn)
// Space: O(1)

// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    // Binary Search
    int firstBadVersion(int n) {
        int start = 1, end = n, mid;
        while (start < end) {
            mid = start + (end - start) / 2;
            if (isBadVersion(mid)) // first bad version in front
                end = mid;
            else
                start = mid + 1; // first bad version in back
        }
        return start; // start == end;
    }
};
