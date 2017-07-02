import itertools

def solution(a_list):
    sublist1 = []
    for i in range(0,len(a_list)+1):
        sublist1 += map(list,itertools.combinations(a_list,i))
    return sublist1
