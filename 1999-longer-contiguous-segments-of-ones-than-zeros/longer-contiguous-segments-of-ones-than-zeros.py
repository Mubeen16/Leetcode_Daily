class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones = max_zeros = 0
        count_ones = count_zeros = 0
        for i in s:
            if i == '1':
                count_ones += 1
                count_zeros = 0
            else:
                count_zeros += 1
                count_ones = 0
            max_ones = max(count_ones, max_ones)
            max_zeros = max(count_zeros, max_zeros)
        if max_ones > max_zeros:
            return True
        else:
            return False
        


        