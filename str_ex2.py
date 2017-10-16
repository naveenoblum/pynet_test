#!/usr/bin/env python
ip_addr = raw_input("Input your IP address:")

#ip_list=ip_addr.split(".")
#print("{:<12}{:<12}{:<12}{:<12}".format(ip_list[0],ip_list[1],ip_list[2],ip_list[3]))

ip_list=ip_addr.split(".")
print("{:<12}{:<12}{:<12}{:<12}".format(*ip_list))
