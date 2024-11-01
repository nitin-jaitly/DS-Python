"""
Use the input below to create the the element list, with each list element being a dictionary with the following keys: "mac_addr" and "interface".

Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  1111.1111.1111  ARPA  Gi0/0/0
Internet  10.220.88.2  29  2222.2222.2222  ARPA  Gi0/0/1
Internet  10.220.88.3   -  3333.3333.3333  ARPA  Gi0/0/2
Internet  10.220.88.4 104  4444.4444.4444  ARPA  Gi0/0/3
Internet  10.220.88.5 161  5555.5555.5555  ARPA  Gi0/0/4

Results will look like:
[
 {'interface': 'Gi0/0/0', 'mac_addr': '1111.1111.1111', "Age" : 67},
 {'interface': 'Gi0/0/1', 'mac_addr': '2222.2222.2222'},
  :
  :
]

"""

# import <?>
from pprint import pprint


def parse_fields(blob):
    count = 0
    my_hash = {}
    my_list = []

    for line in blob.split('\n'):
        count += 1
        if line:
            if count == 1:
                continue

            words = line.split(' ')

            my_hash['Protocol'] = words[0]
            my_hash['Address'] = words[1]
            my_hash['Age'] = words[2]
            my_hash['Hardware Addr'] = words[3]
            my_hash['Type'] = words[4]
            my_hash['Interface'] = words[5]

        my_list.append(my_hash)

    return my_list


def main():
    blob = """Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  1111.1111.1111  ARPA  Gi0/0/0
Internet  10.220.88.2  29  2222.2222.2222  ARPA  Gi0/0/1
Internet  10.220.88.3   -  3333.3333.3333  ARPA  Gi0/0/2
Internet  10.220.88.4 104  4444.4444.4444  ARPA  Gi0/0/3
Internet  10.220.88.5 161  5555.5555.5555  ARPA  Gi0/0/4
"""

    print(parse_fields(blob))


if __name__ == "__main__":
    main()