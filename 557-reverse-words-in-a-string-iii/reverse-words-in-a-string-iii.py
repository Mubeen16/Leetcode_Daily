class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = []
        s = s.split()
        for word in s:
            reverse.append(word[::-1])
        return " ".join(reverse)
        