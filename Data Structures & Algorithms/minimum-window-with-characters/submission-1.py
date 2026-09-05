class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = {}

        for c in t:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1

        left = 0
        minlength = float("inf")  # min length is infinity
        result = ""  # string
        count = len(t)

        for right in range(len(s)):
            c = s[right]

            if c in map:
                if map[c] > 0:
                    count -= 1
                map[c] -= 1

            if count == 0:

                while s[left] not in map or map[s[left]] < 0:

                    if s[left] in map:
                        map[s[left]] += 1

                    left += 1

                if right - left + 1 < minlength:
                    minlength = right - left + 1
                    result = s[left:right + 1]

                if s[left] in map:
                    map[s[left]] += 1
                    count += 1

                left += 1

        return result