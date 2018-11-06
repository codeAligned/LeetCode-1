# 929. Unique Email Addresses
# Time: O(N)
# Space: O(N)

# use a set to store normalized emails and return length of the set
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            ln, dn = email.split('@')
            nn = ''.join(ln.split('+')[0].split('.'))
            email_set.add('@'.join([nn, dn]))
        return len(email_set)
