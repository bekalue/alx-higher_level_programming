#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        try:
            div_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            div_list.append(0)
            print("division by 0")
        except TypeError:
            div_list.append(0)
            print("wrong type")
        except IndexError:
            div_list.append(0)
            print("out of range")
    return div_list
