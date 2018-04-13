class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        flag = 0 if ((len(nums1)+len(nums2))%2==0) else 1
        num_median = int((len(nums1)+len(nums2))/2) if flag==0 else int((len(nums1)+len(nums2))/2)+1
        sumlist = nums1+nums2
        median_num = [0,0]
        for num in range((len(nums1)+len(nums2))):
            min = None
            for i in sumlist:
                if min == None:
                    min = i
                elif min > i:
                    min = i
            if(num == num_median-1):
                median_num[0] = min
            elif (num == num_median):
                median_num[1] = min
            sumlist.remove(min)

        print(median_num)
        ans = median_num[0] if flag==1 else (median_num[0]+median_num[1])/2
        return ans

test = Solution()
print(test.findMedianSortedArrays([1,2],[3,4]))