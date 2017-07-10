import itertools


def solution(a_list):
     array = []
     a_list.sort()
     for i in range(len(a_list)+1):
        for j in itertools.combinations(a_list,i):
            array.append(list(j))
     #print list(comb)
     return array
