
class Solution:
    def pascals_triangle(self, numRows: int) -> list[list[int]]:

        res = [[1]]

        for i in range(numRows -1):

            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j], temp[j + 1])

            res.append(row)

        return res

    def driver_pascals_triangle(self):
        numRows = 5
        actual_output = self.pascals_triangle(5)
        output = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        assert actual_output == output

         
