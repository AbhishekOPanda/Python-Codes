#!/usr/bin/env python
# coding: utf-8

def factorial(n):
    if n<0:
        return ("Error, No factorial possible")
    elif n==0:
        return 1
    else:
        if n==1:
            return n
        else:
            return n*factorial(n-1)


def remove_dups(L):
    a=[]
    i=0
    while i<len(L):
        if len(a)!=0 and a[-1]==L[i]:
            a.pop(-1)
        else:
            a.append(L[i])
            i+=1
    return a


def clamp(L,min,max):
    b=[]   
    for j in L:
        if j<min:
            j = min
            b.append(j)   
        elif j>max:
            j = max
            b.append(j)
        elif j>=min and j<=max:
            b.append(j)
        else:
            None
    return b


def exp(x):   
    sum = 0
    for n in range(100):
        err = abs(((x**n)/factorial(n)) * (x/(n+1)))
        if err > 0.01:
            sum += (x**n)/factorial(n)
            n+=1
        else:
            break
    return sum
