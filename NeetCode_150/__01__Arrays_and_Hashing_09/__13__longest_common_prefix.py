
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution:

    def driver_longest_common(self):
        strs = ["flower","flow","flight"]
        print(self.longest_common(strs))

        strs = ["flower", "flow", "flight"]
        print(self.longest_common_2(strs))

        strs = ["dog", "racecar", "car"]
        print(self.longest_common(strs))

    def longest_common(self,strs: list[str]) -> str:

        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

    def longest_common_2(self, v: list[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans