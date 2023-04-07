#!/usr/bin/python3
def uniq_add(my_list=[]):
    list2 = []
    for x in my_list:
        if x not in list2:
            list2.append(x)
    return sum(list2)
