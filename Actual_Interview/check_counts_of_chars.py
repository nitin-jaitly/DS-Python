"""
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie:
 b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be solution(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be solution(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be solution(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string inputString

A string of lowercase English letters.
"""
class Solution:
    def solution(self,inputString):
        counts = [0] * 26

        ## Count occurance of each letter
        for char in inputString:
            counts[ord(char) - ord('a')] += 1

        # Check if each letters count is at most the count of the previous letter
        for i in range(1,26):
            if counts[i] > counts[i -1]:
                return False

        return True

def main():
    input_string = "bbbaacdafe"
    sol = Solution()
    print(sol.solution(input_string))

if __name__ == "__main__":
    main()
