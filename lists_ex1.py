#! /usr/bin/env python

my_list = []
for i in range(5):
    name=raw_input("Enter name: ")
    my_list.append(name)
print my_list

print("PoP Element:{}".format(my_list.pop()))
print("length of list:{}".format(len(my_list)))
#len(my_list)
my_list.sort()
print my_list
