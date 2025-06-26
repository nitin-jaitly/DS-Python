"""

A valid IP address consists of exactly four integers separated by
single dots.Each integer is between 0 and 255(inclusive) and cannot
have leading zeros.

For example, "0.1.2.201" and "192.168.1.1"
are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are
invalid IP addresses. Given a string s containing only digits, return all
possible valid IP addresses that can be formed by inserting dots into
s.You are not allowed to reorder or remove any digits in s.You may return the
valid IP addresses in any order.

Example
1:

Input: s = "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
Example
2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example
3:

Input: s = "101023"
Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
"""

class Solution:
    def validIPAddresses(self,s):
        def is_valid_part(part):
            # Check if part is empty or has leading zeros
            if not part or (len(part) > 1 and  part[0] == "0"):
                return False
            # Convert to integer and check range
            try:
                num = int(part)
                return 0 <= num <= 255
            except ValueError:
                return False

        def backtrack(start, parts, result):
            # Base case : if we have 4 parts and used all characters
            if len(parts) == 4 and start == len(s):
                result.append('.'.join(parts))
                return

            # If we have more than 4 parts or reached end of string prematurely
            if len(parts) > 4 or start >= len(s):
                return

            # Try different lengths for the current part ( 1 to 3 digits )
            for length in range(1, min(4, len(s) -start + 1)):
                part = s[start:start + length]
                if is_valid_part(part):
                    # Add current part and continue with next part
                    parts.append(part)
                    backtrack(start + length, parts, result)
                    parts.pop()

        result = []
        backtrack(0, [], result)
        return result


def main():
    s = "25525511335"
    sol = Solution()
    print(sol.validIPAddresses(s))

if __name__ == "__main__":
    main()