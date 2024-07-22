

"""
[2:29 PM] Savin Viswanath
Interface IP_address Netmask   Link  Protocol
Gig1/1  1.1.1.1  255.255.255.0  UP UP
Gig1/2  2.2.2.2  255.255.255.0  DOWN UP
Gig1/3  1.1.2.1  255.255.255.0  DOWN DOWN
Gig1/4  3.3.3.3  255.255.255.0  UP DOWN
Gig1/5  4.4.4.4  255.255.255.0  UP UP


Write a class and methods for the above table

The methods should return:
The link and the protocol status for a given interface
The name of the interface which is UP based on Link or protocol or both

"""

class Solution:

    def link_proto_given_interface(self, interface_name_query , device_fw_output, interface_string_query):

        my_dict = {}
        interface_names = []

        for line in device_fw_output:
            if line == interface_string_query:
                continue

            interface_name          = line.split(" ")[0]
            interface_ip            = line.split(" ")[1]
            interface_netmask       = line.split(" ")[2]
            interface_link          = line.split(" ")[3]
            interface_protocol      = line.split(" ")[4]

            if interface_protocol == 'UP':
                interface_names.append(interface_name)


            my_dict[interface_name] = [interface_ip , interface_netmask, interface_link, interface_protocol]



        res_interface_ip        = my_dict[interface_name_query][0]
        res_interface_netmask   = my_dict[interface_name_query][1]
        res_interface_link      = my_dict[interface_name_query][2]
        res_interface_protocol  = my_dict[interface_name_query][3]

        return  res_interface_link,  res_interface_protocol

    """
    Status format: Link/Protocol
    Name IP_address       Netmask                           Status                      LACP
    Gig1/1     1.1.1.1        255.255.255.0           UP/UP                True
    Gig1/2     2.2.2.2        255.255.255.0           DOWN/UP              False
    Gig1/3     1.1.2.1        255.255.255.0           DOWN/DOWN            False
    Gig1/4     3.3.3.3        255.255.255.0           UP/DOWN              True
    """
    def link_proto_given_interface_2(self,  interface_name_query , device_fw_output, interface_string_query):

        my_dict = {}
        interface_names = []

        for line in device_fw_output:
            if line == interface_string_query:
                continue

            interface_name = line.split(" ")[0]
            interface_ip = line.split(" ")[1]
            interface_netmask = line.split(" ")[2]
            interface_link = line.split(" ")[3]
            interface_protocol = line.split(" ")[4]

            if interface_protocol == 'UP':
                interface_names.append(interface_name)

            my_dict[interface_name] = [interface_ip, interface_netmask, interface_link, interface_protocol]

        res_interface_ip = my_dict[interface_name_query][0]
        res_interface_netmask = my_dict[interface_name_query][1]
        res_interface_link = my_dict[interface_name_query][2]
        res_interface_protocol = my_dict[interface_name_query][3]

        return res_interface_link, res_interface_protocol

#
#
# {} .
#
# tubles are immutable .
#
#
# sets will have uniqu
#
# L  = [1,2,2,3,5,6,3]
#
# set_of_L = set(L)
# set_of_L = ( 1, 2, 3, 5, 6)
#
# my_dict = {'a' : 1 ,
#            'b' : 2,
#            'c' : 3
#            tuple : [1,2,3,5],
#            tuple : dict,
#            object : // Object can be a key.
#
#            }
#
#            args , kwargs**
#            k , (k,v)
#
#
#
#
#
#
#
# val = my_dict['a']
#
# L = [1,2,4 ]
#     L[0], L[2], L[3]
#
# l = len(L)
#
# for i in range(L):
#     print( i  , L[i])
#
#
# for k, v in my_dict.values():
#     k