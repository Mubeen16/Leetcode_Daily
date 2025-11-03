class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}
        for ch in chars:
            freq[ch] = freq.get(ch, 0) + 1

        total_length = 0
        for word in words:
            temp = freq.copy()
            can_form = True
            for ch in word:
                if ch not in temp or temp[ch] == 0:
                    can_form = False
                    break
                else:
                    temp[ch] -= 1
            if can_form:
                total_length += len(word)
        return total_length


        
        