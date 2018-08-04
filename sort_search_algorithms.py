#! /usr/bin/env python

"""
@author Xia Wenwen
@date 2018-08-03
This python script is used to provide quick sort and binary search algorithms
"""

from __future__ import print_function
# randrange is used to pick a random index for pivot
from random import randrange

'''
The chosen pivot value will be placed at the end index
The marker_index is used to trace the value less than the pivot value
After the  for loop, the left side of marker_index has values less than the pivot value
'''
def partition(lst, start, end, pivot):
    # swap pivot and end indices
    lst[pivot], lst[end] = lst[end], lst[pivot]
    marker_index = start

    # start <= i < end, compare lst[i]  with pivot element
    for i in xrange(start, end):
        # if less than the pivot element, do swap to move smaller one to the left
        if lst[i] < lst[end]:
            lst[i], lst[marker_index] = lst[marker_index], lst[i]
            marker_index += 1

    # swap the pivot with marker
    lst[marker_index], lst[end] = lst[end], lst[marker_index]
    # return the real pivot index
    return marker_index

def quick_sort(lst, start, end):
    if start >= end:
        return lst

    # pick a random pivot,  start <= pivot < end+1
    pivot = randrange(start, end+1)

    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot-1)
    quick_sort(lst, new_pivot+1, end )

def sort(lst):
    quick_sort(lst, 0, len(lst)-1)
    return lst

'''
Assumption: list is sorted with ascending order
binary search algorithm to return the index of the target element.
If not found, return -1
'''
def binary_search(lst, start, end, target):
    if end >= start:
        mid = start + (end-start)/2
        # element at middle
        if target == lst[mid]:
            return mid

        elif target < lst[mid]:
            return binary_search(lst, start, mid-1, target)

        else:
            return binary_search(lst, mid+1, end, target)

    else:
        return -1


if __name__ == '__main__':
    lst = [3, 1, 9, 4, 8, 20]
    print (sort(lst))
    print (binary_search(lst, 0, len(lst)-1, 2))


