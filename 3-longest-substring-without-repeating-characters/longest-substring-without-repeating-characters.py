class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m_len = 0
        left =0
        duplicate = set()

        for right in range(len(s)):
            while s[right] in duplicate:
                duplicate.remove(s[left])
                left+=1
            duplicate.add(s[right])
            m_len = max(m_len, right - left +1)
        return m_len