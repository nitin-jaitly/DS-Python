def find_avg_in_window(arr, window_aize):
    print(f"arr with zeros = {arr}")
    # Find arr with no zeros
    arr_no_zeros = [x for x in arr if x != 0]
    print(arr)
    print(arr_no_zeros)
    print(f"arr_no_zeros = {arr_no_zeros}")

    # Check if arr has enough elements
    if len(arr_no_zeros) < window_aize:
        return None

    # Initialize min_avg
    min_avg = float('inf')

    for i in range(len(arr_no_zeros) - window_aize + 1):
        window = arr_no_zeros[i:i + window_aize]
        window_avg = sum(window) / window_aize
        min_avg = min(min_avg, window_avg)
        print(f" window = {window} \n window_avg = {window_avg}\n min_avg = {min_avg} \n\n")

    float_min_avg = float(f"{min_avg:.2f}")
    return float_min_avg


def driver_find_avg_in_window():
    ## Test 1
    arr = [ 12 , 4, 5 , 6 , 0 , 2 , 5 , 6 , 7 , 9 , 2 , 14 , 5]
    window_size = 3
    res = find_avg_in_window(arr, window_size)
    expected_val = 4.33
    print(type(res))
    print(res)
    print(type(expected_val))
    print(expected_val)
    assert expected_val == res

def main():
    driver_find_avg_in_window()

if __name__ == "__main__":
    main()