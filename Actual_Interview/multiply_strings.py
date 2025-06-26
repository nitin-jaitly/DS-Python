"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        num3 = num1 * num2
        return str(num3)

    def multiply2(self,num1: str, num2: str) -> str:
        # Handle edge case of multiplying by zero
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize result array to store digits
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Process each digit from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Convert characters to digits
                n1 = ord(num1[i]) - ord('0')
                n2 = ord(num2[j]) - ord('0')

                # Multiply digits and add to result
                product = n1 * n2
                pos1, pos2 = i + j, i + j + 1

                # Add product to result positions
                product += result[pos2]
                result[pos2] = product % 10
                result[pos1] += product // 10

        # Convert result array to string
        result_str = ""
        for digit in result:
            if not (result_str == "" and digit == 0):  # Skip leading zeros
                result_str += str(digit)

        return result_str if result_str else "0"


def main():
    num1 = "2"
    num2 = "3"
    sol = Solution()
    assert "6" == sol.multiply2(num1, num2)
    print(sol.multiply2(num1, num2))

    num1 = "3233234"
    num2 = "3093411234"
    assert sol.multiply(num1, num2) == sol.multiply2(num1,num2)
    print(sol.multiply2(num1, num2))


if __name__ == "__main__":
    main()