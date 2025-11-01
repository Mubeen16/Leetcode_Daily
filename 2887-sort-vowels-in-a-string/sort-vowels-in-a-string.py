class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s_list = list(s) #list conversion

        v = []
        for ch in s_list: #step 1 extracting the voewels and sort it by ASCII
            if ch in vowels:
                v.append(ch) # appending the vowels to the to the new list
        v.sort() # sort it by ASCII value
        j = 0 
        for i in range(len(s_list)):  #reinsert sorted voewls to 
            if s_list[i] in vowels:
                s_list[i] = v[j]
                j += 1
        return "".join(s_list)
        