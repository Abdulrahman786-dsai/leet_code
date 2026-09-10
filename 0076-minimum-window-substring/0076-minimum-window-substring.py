from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        left = 0
        have = 0
        need_count = len(need)

        ans = ""
        ans_len = float("inf")

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            # Window valid hai
            while have == need_count:
                if right - left + 1 < ans_len:
                    ans_len = right - left + 1
                    ans = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return ans