import pandas as pd

class Solution:
    def topK(self, weather, k, sort_by):

        df_weather = pd.DataFrame(weather, columns =['city', 'temp', 'humidity'])
        result_df = df_weather.sort_values(by=sort_by, ascending=False).head(k)
        return result_df

    def check_top_k(self):
        k = 2  # Find the top 2 temperatures for all these cities
        sort_by = "temp"
        sort_by = "humidity"

        weather =[('san ramon', 73, 4.0), ('san jose', 76, 4.5), ('santa clara', 74, 3.0)]
        print(self.topK(weather,k, sort_by))

        k = 1
        print(self.topK(weather,k, sort_by))
        #assert [76, 74] == self.topk(weather, k)

def main():
    sol = Solution()
    sol.check_top_k()

if __name__ == "__main__":
    main()