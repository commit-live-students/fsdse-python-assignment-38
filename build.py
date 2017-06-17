# import itertools

def solution(a_list):
    """Enter code here"""
    lst = [[]]
    for i in range(len(a_list)):
        for j in range(len(a_list)):
            if (i == j):
                lst.append([a_list[i]])
            elif (i > j):
                lst.append([a_list[j],a_list[i]])
    lst.append(a_list)
    return lst

a_list = [10, 20, 30]
print(solution(a_list))
