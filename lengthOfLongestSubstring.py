class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        d = {}
        start = 0
        ans = 0
    
        for i in range(len(s)):
            if s[i] in d:
                start = max(start,d[s[i]] + 1)
                d[s[i]] = i
            else:
                d[s[i]] = i
            length = i - start + 1
            if length > ans:
                ans = length
        return ans
                