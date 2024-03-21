

class Solution:
    def length_of_longest_substring(self,s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


    def driver_length_of_longest_substring(self):
        s = "abcabcbb"
        print(self.length_of_longest_substring(s))

        s = "bbbbb"
        print(self.length_of_longest_substring(s))

        s = "pwwkew"
        print(self.length_of_longest_substring(s))



