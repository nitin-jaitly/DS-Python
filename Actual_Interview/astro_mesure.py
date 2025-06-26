def get_spotting_metric(results):
    n = len(results)
    # window = 0 , 1  , 2 ( first elem)
    # window = 4   5    6 # when n = 7

    print(results)
    low_avg = 1000000

    for i in range(1, n - 1, 1):
        print( results[i-1], results[i], results[i+1])
        sum = results[i - 1] + results[i] + results[i + 1]
        print(f"sum = {sum}")
        cur_avg = ( sum / 3)
        print(f"cur_avg = {cur_avg}")
        low_avg = min(low_avg, cur_avg)
        rounded_low_avg = format(low_avg, '.2f')
        print(rounded_low_avg)
        print(" ")

    return rounded_low_avg


def main():
    results = [2, 1, 3, 0, 1, 5, 0, 0, 6, 7]
    print(get_spotting_metric(results))  # should print ~1.667


if __name__ == "__main__":
    main()

"""
output
/Users/nitin/PycharmProjects/DS-Python/venv/bin/python /Users/nitin/PycharmProjects/DS-Python/Actual_Interview/astro_mesure.py 
[2, 1, 3, 0, 1, 5, 0, 0, 6, 7]
2 1 3
sum = 6
cur_avg = 2.0
2.00
 
1 3 0
sum = 4
cur_avg = 1.3333333333333333
1.33
 
3 0 1
sum = 4
cur_avg = 1.3333333333333333
1.33
 
0 1 5
sum = 6
cur_avg = 2.0
1.33
 
1 5 0
sum = 6
cur_avg = 2.0
1.33
 
5 0 0
sum = 5
cur_avg = 1.6666666666666667
1.33
 
0 0 6
sum = 6
cur_avg = 2.0
1.33
 
0 6 7
sum = 13
cur_avg = 4.333333333333333
1.33
 
1.3333333333333333

Process finished with exit code 0

"""
