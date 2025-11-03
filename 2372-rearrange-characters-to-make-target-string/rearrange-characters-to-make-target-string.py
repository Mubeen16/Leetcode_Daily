class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_freq = {}
        for ch in s:
            s_freq[ch] = s_freq.get(ch, 0) + 1
        
        t_freq = {}
        for ch in target:
            t_freq[ch] = t_freq.get(ch, 0) + 1

        min_copies = float('inf')

        for ch in t_freq:
            if ch not in s_freq:
                return 0
            copies = s_freq[ch] // t_freq[ch]
            if copies < min_copies:
                min_copies = copies
        return min_copies



        