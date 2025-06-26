



class Solution:
    def daily_temperatures(self, temps):
        print(temps)
        res = []
        n = len(temps)

        for i in range(n):
            count = 1
            j = i + 1

            while j < n:
                if temps[j] > temps[i]:
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            res.append(count)
        print(res)
        return res

    def daily_temperatures_using_stack(self, temps):
        n = len(temps)
        res = [0] * n
        stack = [] # pair of temp and index

        for i , t in enumerate(temps):
            while stack and t >  stack[-1][0]:
                 stackT , stackInd = stack.pop()
                 res[stackInd] = i - stackInd
            stack.append([t , i])

        return res



    def driver_daily_temperatures(self):
        temperatures = [30, 38, 30, 36, 35, 40, 28]
        output = [1,4,1,2,1,0,0]
        assert output == self.daily_temperatures(temperatures)

        assert output == self.daily_temperatures_using_stack(temperatures)

def main():
    sol = Solution()
    sol.driver_daily_temperatures()

if __name__ == "__main__":
    main()