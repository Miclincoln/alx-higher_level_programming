#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    temp_set = []
    for x in set_1:
        if x not in set_2:
            temp_set.append(x)
    for y in set_2:
        if y not in set_1:
            temp_set.append(y)
    return temp_set
