import itertools


def solution(a_list):
    """Enter code here"""
    sub = [[]]

    for i in range(len(a_list)):
        for j in range(len(a_list)):
            if(i == j):
                sub.append([a_list[i]])
            elif(i > j):
                sub.append([a_list[j],a_list[i]])
    sub.append(a_list)
    return sub


solution([10, 20, 30])
