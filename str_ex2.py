#!/usr/bin/env python
ip_addr = raw_input("Input your IP address:")

#ip_list=ip_addr.split(".")
#print("{:<12}{:<12}{:<12}{:<12}".format(ip_list[0],ip_list[1],ip_list[2],ip_list[3]))

ip_list=ip_addr.split(".")
ip_list[-1]=0
for i in range(len(ip_list)):
    print("Decimal: {:<12}".format(ip_list[i]))
    print("Binary: {:<12}".format(bin(int(ip_list[i]))))
#print("{:<12}{:<12}{:<12}{:<12}".format(*ip_list))
