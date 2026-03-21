class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        f,s = m-1, n-1
        r = m+n-1
        while s>=0:
            if f>=0 and nums1[f] > nums2[s]:
                nums1[r] = nums1[f]
                f-=1
            else:
                nums1[r] = nums2[s]
                s-=1
            r-=1

            
                        
                
                