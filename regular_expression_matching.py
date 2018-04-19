import re

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #pattern = re.split(p, s )
        #str1 = pattern.match(s)
        #return re.findall(p,s)
        return  False if re.findall(p,s) == [] or (re.findall(p,s)[0] != s) else True


a = Solution()
print(a.isMatch("aa", "a"))
print(a.isMatch("aa", "a*"))
print(a.isMatch("ab", ".*"))
print(a.isMatch("aab", "c*a*b"))
print(a.isMatch("mississippi", "mis*is*p*."))
print(a.isMatch("ab", ".*c"))

