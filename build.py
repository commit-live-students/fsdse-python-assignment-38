import itertools


def solution(a_list):
    """Creation of sublist contains the check of possibility of new member
        which is lying inside the orignal list,
        then forming up the new list taking length of the as a constraint
    """
    sub_list = [[]]

    for i in range(len(a_list)):
        for j in range(len(a_list)):
            if(i == j):
                sub_list.append([a_list[i]])
            elif(i > j):
                sub_list.append([a_list[j],a_list[i]])
    sub_list.append(a_list)
    print sub_list
    return sub_list


solution([10, 20, 30])
