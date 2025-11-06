class Solution:
    def countDigits(self, num: int) -> int:
        #num = str(num)
        count = 0
        for val in str(num):
            if num % int(val) == 0:
                count += 1
        return count

        