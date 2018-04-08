# -*- coding: utf-8 -*-

# 希尔排序


def shell_sort(a):
    a_len = len(a)
    gap = a_len / 2
    while gap > 0:
        for i in range(a_len):
            m = i
            j = i + 1
            while j < a_len:
                if a[j] < a[m]:
                    m = j
                j += gap
            if m != i:
                a[m], a[i] = a[i], a[m]
        gap /= 2


A = [10, -3, 5, 7, 1, 3, 7]
print "Before sort:", A
shell_sort(A)
print "After sort:", A
