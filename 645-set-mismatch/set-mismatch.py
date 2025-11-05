class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}
        dup = miss = 0
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for i in range(1, len(nums)+1):
            if i not in freq:
                miss = i
            elif freq[i] == 2:
                dup = i
        return [dup, miss]
        