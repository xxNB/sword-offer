# -*- coding: utf-8 -*-

# 归并排序

import sys


def merge(nums, first, middle, last):
    lnums = nums[first:middle + 1]
    rnums = nums[middle + 1:last + 1]
    print ("lnums", lnums)
    print ("rnums", rnums)
    lnums.append(sys.maxint)
    rnums.append(sys.maxint)
    l = 0
    r = 0
    for i in range(first, last + 1):
        if lnums[l] < rnums[r]:
            nums[i] = lnums[l]
            l += 1
        else:
            nums[i] = rnums[r]
            r += 1


def merge_sort(nums, first, last):
    if first < last:
        middle = (first + last) / 2
        merge_sort(nums, first, middle)
        merge_sort(nums, middle + 1, last)
        print nums, first, middle, last
        merge(nums, first, middle, last)
        print "================================"


nums = [10, 8, 4, -1, 2, 6, 7, 3]
print ("nums is:", nums)
merge_sort(nums, 0, 7)
print ("merge sort:", nums)

n*logn