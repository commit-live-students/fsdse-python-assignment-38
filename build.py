import itertools
def solution(a_list):
    sublist = []
    for i in range(0,len(a_list)+1):
        sublist += map(list,itertools.combinations(a_list,i))

    return sublist
solution([10, 20, 30])
