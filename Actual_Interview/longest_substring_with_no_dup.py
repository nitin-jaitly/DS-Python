
class Solution:
    def longest_substring(self, s):
        l = 0
        res = 0
        my_set = set()
        r = 0

        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1

            my_set.add(s[r])
            res = max(res, r - l +  1)

        return res

def main():

    sol = Solution()
    s = "abcabcbb"
    print(f"Length of Longest subscriont for \n {s} is \n {sol.longest_substring(s)}")

if __name__ == "__main__":
    main()