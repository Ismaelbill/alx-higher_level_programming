#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(list_length):
        try:
            newList.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            newList.append(0)
            print("division by 0")
            continue
        except (TypeError, ValueError):
            newList.append(0)
            print("wrong type")
            continue
        except IndexError:
            newList.append(0)
            print("out of range")
            continue
        finally:
            pass
    return newList
