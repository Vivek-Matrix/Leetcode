class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng = defaultdict(lambda: -1)
        s = []

        for num in nums2:
            while s and num > s[-1]:
                ng[s.pop()] = num
            s.append(num)
        return [ng[num] for num in nums1]