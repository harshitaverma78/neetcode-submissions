class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Count characters needed from t
        countT = {}
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        window = {}
        have = 0
        need = len(countT)

        left = 0
        res = ""
        resLen = float("inf")

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # This character now has enough occurrences
            if ch in countT and window[ch] == countT[ch]:
                have += 1

            # Window is valid → try to make it smaller
            while have == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    res = s[left:right + 1]

                # Remove left character
                leftChar = s[left]
                window[leftChar] -= 1

                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    have -= 1

                left += 1

        return res