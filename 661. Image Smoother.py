# 661. Image Smoother
# Time: O(N^2)
# Space: O(N)

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        col = len(M[0])
        res = [x[:] for x in M]
        for i in range(row):
            for j in range(col):
                sum = 0
                cnt = 0
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if ii < 0 or jj < 0 or ii >= row or jj >= col:
                            continue;
                        sum += M[ii][jj]
                        cnt += 1
                res[i][j] = sum // cnt;
        return res