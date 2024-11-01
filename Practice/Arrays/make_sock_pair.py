

def sockMerchant(n, ar):
    my_hash = {}
    for num in ar:
        my_hash[num] =  1 + my_hash.get(num, 0)

    countPairs = 0
    for k,v in my_hash.items():
        print(k,v)
        countPairs += v // 2

    return countPairs

def main():
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    n = len(ar)
    print(sockMerchant(n, ar))

if __name__ == "__main__":
    main()