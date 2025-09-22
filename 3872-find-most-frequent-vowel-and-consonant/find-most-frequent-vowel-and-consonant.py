class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = s.count(i)
        
        v_count = 0
        c_count = 0
        for k, v in freq.items():
            if k in ["a", "e", "i", "o", "u"] and freq[k] > v_count:
                v_count = freq[k]
            elif k not in ["a", "e", "i", "o", "u"] and freq[k] > c_count:
                c_count = freq[k]
        return v_count + c_count