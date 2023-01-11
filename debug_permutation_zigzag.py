#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:22:33 2022
@author: parisbg

Given an array of  distinct integers, transform the array into a zig zag 
sequence by permuting the array elements. A sequence will be called a zig zag 
sequence if the first  elements in the sequence are in increasing order and 
the last  elements are in decreasing order, where . You need to find the 
lexicographically smallest zig zag sequence of the given array.
"""

#sort the array
#define k = (n+1)/2
#Permute the array

a = [2,3,5,1,4,6,7]
n = len(a)
a.sort() #a = [1,2,3,4,5,6,7]
mid = int((n + 1)/2) - 1 #mid = 3
a[mid], a[n-1] = a[n-1], a[mid]#Swapping mid with end | #a = [1,2,3,7,5,6,4]

st = mid + 1 #st = 4
ed = n - 2 #ed = 5
while(st <= ed):
    a[st], a[ed] = a[ed], a[st] #a = [1,2,3,7,6,5,4]
    st = st + 1 #st = 5
    ed = ed - 1 #ed = 4   

for i in range (n):
    if i == n-1:
        print(a[i])
    else:
        print(a[i], end = ' ')
