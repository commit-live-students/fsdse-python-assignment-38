from itertools import combinations


def solution(a_list):
    output = sum([map(list, combinations(a_list, i)) for i in range(len(a_list) + 1)], [])
    return output

print solution([10,20,30])    
