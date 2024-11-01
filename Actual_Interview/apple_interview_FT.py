####################################################
############ Query counts         ##################
####################################################


#### 3) Order output of tokens by count popularity.
def get_ordered_token_counts(queries=None):
    seen = {}

    for query in queries:
        words_in_lower = query.lower().strip().split(' ')

        for word in words_in_lower:
            if word not in seen:
                seen[word] = 1
            else:
                seen[word] = 1 + seen.get(word, 0)

    sorted_seen = sorted(seen.items(), key=lambda x: x[1], reverse=True)

    return sorted_seen


#### 2) Find the token counts for each query in the list (undercase and stripped of start/end whitespace) ###
#### Tokens are strings with query separated by whitespace - "park ave" -> ["park","ave"]
#### Example output: {"park": 2, "ave": 1, "apple": 2, "ca": 1,...}

def get_token_counts(queries=None):
    seen = {}

    for query in queries:
        lower_case_query = query.lower()
        lower_case_query = lower_case_query.strip()

        words_in_lower = lower_case_query.split(' ')

        for word in words_in_lower:
            if word not in seen:
                seen[word] = 1
            else:
                seen[word] = 1 + seen.get(word, 0)

    return seen


#### 1) Find the query count for each query in the list. Make each query undercase and stripped of start/end whitespace ###
#### Example output - {"mcdonalds": 2, "park ave": 1, ... } ###

def get_query_counts(queries=None):
    seen = {}

    for query in queries:
        lower_case_query = query.lower()
        lower_case_query = lower_case_query.strip()

        if lower_case_query not in seen:
            seen[lower_case_query] = 1
        else:
            seen[lower_case_query] = 1 + seen.get(lower_case_query, 0)

    return seen


def main():
    queries = [
        'starbucks cupertino',
        'McDonalds',
        'apple park',
        'park ave',
        'cupertino ca',
        'Mcdonalds',
        'mcdonalds',
        'Starbucks',
        'starbucks',
        'cupertino Ca',
        'starbucks ca',
        'starbucks Ca',
        'mcdonalds SF',
        'apple park',
        'park ave',
        'cupertino ca  ',
        'starbucks Cupertino',
        'mcdonalds',
        'Apple park',
        'park ave',
        'cupertino ca',
        'starbucks cupertino',
        'mcdonalds',
        'mcdonalds',
        'mcdonalds',
        'Starbucks',
        'apple park',
        'park ave',
        'cupertino ca',
    ]

    # print(get_query_counts(queries))
    # print(get_token_counts(queries))
    print(get_ordered_token_counts(queries))


if __name__ == "__main__":
    main()



