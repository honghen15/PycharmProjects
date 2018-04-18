class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        list =[]
        putstr = ''
        for i in range(numRows):
            list.append(putstr)
        county = countx = 0
        for letter in s:
            if countx == numRows-1:
                county = countx = 0
            elif countx > 0:
                list[numRows-countx-1] += letter
                countx += 1
                continue
            list[county] += letter
            county += 1
            if county == numRows:
                countx += 1
        return ''.join(list)



a = Solution()
print(a.convert('abcdefghijklmnop', 1))