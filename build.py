from itertools import permutations,combinations
def solution(a_list):
    sublist=[]
    # if a_list==None: print '[]'
    for length in range(len(a_list) + 1):
        for case in combinations(a_list, length):
            # if case==None:
            #     print '[]'
            # else:
                sublist.append(list(case))
    return sublist
print solution([10, 20, 30])
#     sub_list = [[]]
#
#     for i in range(len(a_list)):
#         for j in range(len(a_list)):
#             if(i == j):
#                 sub_list.append([a_list[i]])
#             elif(i > j):
#                 sub_list.append([a_list[j],a_list[i]])
#     sub_list.append(a_list)
#     print sub_list
#     return sub_list
#
#
# solution([10, 20, 30])
