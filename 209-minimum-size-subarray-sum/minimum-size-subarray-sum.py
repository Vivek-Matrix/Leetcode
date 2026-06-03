class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        w_sum = 0
        w_m_len = float('inf')
        l = 0

        for r in range(len(nums)):
            w_sum += nums[r]

            while w_sum >=target:
                w_m_len = min(w_m_len,r-l+1)
                w_sum -= nums[l]
                l+=1
        return 0 if w_m_len == float('inf') else w_m_len