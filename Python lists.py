# Exercise 1: Returns the sum of all the numberrs in a given list.

def sum_list(thelist):
    if len(thelist)==0:
        return 0
    elif len(thelist) == 1:
        return thelist[0]
    return thelist[0] + sum_list(thelist[1:])


# Exercise 2: Returns a reverse list

def reverse(s):
    if s == '':
        return s
    return reverse(s[1:])+s[0]


# Exercise 3: Returns a list with no adjecent duplicate numbers

def remove_adj_dups(thelist):
    if len(thelist)>1:
        if thelist[0] != thelist[1]:
            return [thelist[0]] + remove_adj_dups(thelist[1:])
        del thelist[1]
        return remove_adj_dups(thelist)
    return thelist


# Exercise 4: 

def into(n, c):
    if n%c != 0:
        return 0
    else:
        return 1 + into(n/c,c)
