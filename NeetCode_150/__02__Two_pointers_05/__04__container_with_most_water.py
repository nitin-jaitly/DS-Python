
class Solution:
    def max_area(self,height: list[int]) -> int:
        #  Brute Force method
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         area = ( l - r ) * min(height[l], height[r])
        #         res = max(res, area)
        #
        # return res

        # Order of N
        max_area = 0
        l, r = 0,len(height) - 1
        while l < r:
            area = ( r - l ) * min(height[l], height[r])
            max_area = max(max_area,area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

    def driver_max_water(self):
        height = [1,1,4,5,6,7,7,83,6 ,5,3,5,6]
        assert 48 == self.max_area(height)

        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        assert 49 == self.max_area(height)
        print(self.max_area(height))


def main():
    sol = Solution()
    sol.driver_max_water()

if __name__ == "__main__":
    main()