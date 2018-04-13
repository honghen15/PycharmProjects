class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if  len(s) <= 1:
        #     return len(s)
        s2 = s[1:]
        count = 0
        index = 1
        max1 = None
        sub = ''
        for i in s :
            s2 = s[index:]
            sub = i
            count+=1
            for j in s2:
                if not j in sub:
                    sub+=j
                    count+=1
                else:
                    break

            if (max1==None or (max1<count)):
                max1 = count
            count = 0
            index += 1
        return max1 if max1 != None else 0
a = Solution()
print( a.lengthOfLongestSubstring('abcabcab'))
print( a.lengthOfLongestSubstring('bbbbb'))
print( a.lengthOfLongestSubstring('pwwkew'))
print( a.lengthOfLongestSubstring(''))
print( a.lengthOfLongestSubstring('p'))
print( a.lengthOfLongestSubstring('au'))