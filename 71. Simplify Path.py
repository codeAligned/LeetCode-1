# 71. Simplify Path
# Time: O(N)
# Space: O(1)

# 1. cd back over root /, still root /
# 2. // would still be /
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        parts = path.split('/')
        res = []
        for part in parts:
            if part == '.' or not part:
                continue
            elif part == '..':
                if res:
                    res.pop()
            else:
                res.append(part)

        return '/' + '/'.join(res)
