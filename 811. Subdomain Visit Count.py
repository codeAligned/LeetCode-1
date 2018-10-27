# 811. Subdomain Visit Count
# Time: O(N)
# Space: O(N)

from collections import defaultdict

# use defaultdict to safe existence check
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_cnt = defaultdict(int)
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split(' ')
            parts = domain.split('.')
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                domain_cnt[subdomain] += int(cnt)
        return [' '.join([str(cnt), domain]) for domain, cnt in domain_cnt.items()]
