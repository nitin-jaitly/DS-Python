


# Your previous Plain Text content is preserved below:

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dots menu on the tab, or add a new language
# tab using the Languages button on the left.

# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings

 #Compress array
#Given an array of characters, compress it
#The length after compression must always be smaller than or equal to the original array. Return the new array.

#Input: ['a','a','b','c','c','c', 'b','b', 'd']
#Output:  ['a','2','b','c','3', 'b', '2', 'd']

# Enjoy your interview!

class Solution:

    def compress(self,input_list):
        if len(input_list) <= 1:
            return input_list
        print(f"input_list = {input_list}")
        result = []
        count = 1
        current_char = input_list[0]

        for i in range(1, len(input_list)):
            if input_list[i] == current_char:
                count += 1
            else:
                result.append(current_char)
                if count > 1:
                    result.append(str(count))
                current_char = input_list[i]
                count = 1

        result.append(current_char)
        if count > 1:
            result.append(str(count))
        print(f"output_list = {result}")

        return result

    def compress2(self,input_list):
        seen = {}
        for i, char in enumerate(input_list):
            seen[char] = 1 + seen.get(input_list[i], 0)
        print(seen)

        output_str = []
        for k, v in seen.items():
            if v != 1:
                output_str.append(k)
                output_str.append(v)
            else:
                output_str.append(k)

        print(output_str)

    def driver_compress(self):
        input = ['a','a','b','c','c','c', 'b','b', 'd']
        return self.compress(input)


def main():
    sol = Solution()
    sol.driver_compress()
    #assert sol.driver_compress() == ['a','2','b','c','3', 'b', '2', 'd']

if __name__ == "__main__":
    main()