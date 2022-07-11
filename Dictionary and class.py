#import libirary for pi and inf
from math import pi, inf

def twoMaxes(L):
    #The Max of Rows and Columns
    row = []
    col = []
    m = len(L)
    n = len(L[0])
    for i in L:
        row.append(max(i))
    for i in range(n):
        col_max = L[0][i]
        for j in range(1, m):
            col_max = max(col_max, L[j][i])
        col.append(col_max)
    
    return [row, col]


def dictionaryCollector(L):
    #Accumulate in a Dictionary int and str separately 
    numbersSum = 0
    stringJoin = ''

    for item in L:
        if isinstance(item, int):
            if isinstance(item, bool):
                continue
            else:
                numbersSum += item
        elif isinstance(item, str):
            stringJoin += item
        else:
            continue

    response = dict()
    response['int'] = numbersSum
    response['string'] = stringJoin

    return response


def separateNumbers(L):
    #recursive function to separate even and odd numbers of a list and print them in a list 
    def helperEven(L):
        if not L:
            return []
        if L[0] % 2 == 0:
            return [L[0]] + helperEven(L[1: ])
        return helperEven(L[1: ])

    def helperOdd(L):
        if not L:
            return []
        if L[0] % 2 == 1:
            return [L[0]] + helperOdd(L[1: ])
        return helperOdd(L[1: ])
    
    a = helperEven(L)
    b = helperOdd(L)
    return [b,a]


class Circle:
    #Class and subclass functions to find cirlce and sphere properties
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Radius: {self.radius}"

    def area(self):
        return round(pi * (self.radius ** 2), 2)


class Sphere(Circle):
    def __init__(self, radius):
        return super().__init__(radius)

    def __str__(self):
        return f"Radius: {self.radius}"

    def area(self):
        return round(4 * pi * (self.radius ** 2), 2)

    def volume(self):
        return round((pi * (self.radius ** 3)) * 4/3, 2)


def preciseDivision(a, b):
    #Precise division function
    try:
        if b == 0:
            return  float(inf)
        else:
            return a/b
    except:
        return None
