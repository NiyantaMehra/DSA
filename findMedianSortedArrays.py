class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        j =0
        i =0
        new = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new.append(nums1[i])
                i = i + 1
            else:
                new.append(nums2[j])
                j = j + 1

        while i < len(nums1):
            new.append(nums1[i])
            i = i + 1

        while j < len(nums2):
            new.append(nums2[j])
            j = j + 1

        if len(new)%2 == 0:
            return (new[len(new)//2] + new[(len(new) - 1)//2])/2
        else:
            return new[(len(new) - 1)//2] 

 
   