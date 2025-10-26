class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = 0 
        for ch in str(x):
            total += int(ch)
        if x % total == 0:
            return total
        else:
            return -1
        