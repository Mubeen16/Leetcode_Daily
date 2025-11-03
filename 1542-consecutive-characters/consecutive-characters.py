class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_power = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
                max_power = max(count, max_power)
            else:
                count = 1
        return max_power

        