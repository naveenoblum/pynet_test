#! /usr/bin/env python
my_list=list(range(50))
for i in my_list:
    if i==13:
       continue
    elif i==39:
       break
    print i
