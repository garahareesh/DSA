class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = [0]*(len(nums1)+len(nums2))
        i = j= k=0
        median = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                temp[k]=nums1[i]
                i +=1
            else:
                temp[k]=nums2[j]
                j +=1
            k +=1
        while i<len(nums1):
            temp[k]=nums1[i]
            k +=1
            i +=1
        while j<len(nums2):
            temp[k]=nums2[j]
            k +=1
            j +=1
        if len(temp)%2 == 1:
            n = len(temp)//2
            median = temp[n]
        else:
            n = len(temp)//2
            median = (temp[n-1]+temp[n])/2
        return median

        