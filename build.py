"""
# Write a Python program to generate all sublists of a list.

Define a function that takes a list as a parameter and returns a list of all the sublists of the list.
The **sublists** should be sorted. Empty list is also a sublist.

_Example:_

**Input**

`[10, 20, 30]`


**Output**

[[], [10], [20], [30], [10, 20], [10, 30], [20, 30], [10, 20, 30]]
"""

import itertools
def solution(a_list):
    sublist1 = []
    for i in range(0,len(a_list)+1):
        sublist1 += map(list,itertools.combinations(a_list,i))

    return sublist1
