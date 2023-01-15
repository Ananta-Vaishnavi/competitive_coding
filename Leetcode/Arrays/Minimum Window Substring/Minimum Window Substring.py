class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        t_counts = {}
        for c in t:
            if c in t_counts:
                t_counts[c] += 1
            else:
                t_counts[c] = 1
        s_counts = {}
        left = 0
        min_len = len(s) + 1
        min_str = ""
        for right in range(len(s)):
            if s[right] in t_counts:
                if s[right] in s_counts:
                    s_counts[s[right]] += 1
                else:
                    s_counts[s[right]] = 1
                while self.is_valid(s_counts, t_counts):
                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        min_str = s[left:right + 1]
                    if s[left] in s_counts:
                        s_counts[s[left]] -= 1
                        if s_counts[s[left]] == 0:
                            del s_counts[s[left]]
                    left += 1
        return min_str
        
    def is_valid(self, s_counts, t_counts):
        for c in t_counts:
            if c not in s_counts or s_counts[c] < t_counts[c]:
                return False
        return True
