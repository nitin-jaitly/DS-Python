

class Solution:
    def length_of_longest_substring(self,s: str) -> int:
        my_charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in my_charSet:
                my_charSet.remove(s[l])
                l += 1

            my_charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


    def driver_length_of_longest_substring(self):
        s = "abcabcbb"
        print(f"For string {s} longest_sub_length = {self.length_of_longest_substring(s)}")

        s = "bbbbb"
        print(f"For string {s} longest_sub_length = {self.length_of_longest_substring(s)}")

        s = "pwwkew"
        print(f"For string {s} longest_sub_length = {self.length_of_longest_substring(s)}")


def main():
    sol = Solution()
    sol.driver_length_of_longest_substring()

if __name__ == "__main__":
    main()