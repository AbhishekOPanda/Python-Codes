import random
import time
import sys
sys.setrecursionlimit(100000)

def random_numbers_generator(num=1000, min=0, max=10000):
    new_list = []
    for _ in range(num):
        if max > num:
            new_list.append(random.randint(min, max))
    return new_list


def insertion_sort(random_list):
    new_list = []
    new_list = random_list.copy()
    for i in range(1,len(new_list)):
        if new_list[i] >= new_list[i-1]:
            continue
        for j in range(i):
            if new_list[i] < new_list[j]:
                new_list[j],new_list[j+1:i+1] = new_list[i],new_list[j:i]
                break
    return random_list, new_list


def Quick_sort_first(random_list):
    new_list = []
    new_list = random_list.copy() 
    def quick_sort_first(new_list):
        lesser = []
        greater = []
        equal = []
        if len(new_list) > 1:
            pivot = new_list[0]
            for x in new_list:
                if x < pivot:
                    lesser.append(x)
                if x > pivot:
                    greater.append(x)
                if x == pivot:
                    equal.append(x)    
            return quick_sort_first(lesser) + equal + quick_sort_first(greater)
        else:
            return new_list
    return random_list, quick_sort_first(new_list) 

def Quick_sort_random(random_list):
    new_list = []
    new_list = random_list.copy()
    def quick_sort_random(new_list):
        if len(new_list) < 2:
            return new_list
        lesser = [] 
        greater = []
        equal = []
        pivot = new_list[random.randint(0, len(new_list) - 1)]
        for i in new_list:
            if i < pivot:
                lesser.append(i)
            elif i > pivot:
                greater.append(i)
            elif i == pivot:
                equal.append(i)    
        return quick_sort_random(lesser) + equal + quick_sort_random(greater)
    return random_list, quick_sort_random(new_list) 


def oneIteration():
    Start = time.time()
    Random_list = random_numbers_generator(num=100000, max=100000 * 10)
    print('Generating random list, time{}'.format(time.time() - Start))
    print(Random_list)

    Start = time.time()
    _, sorted_list = insertion_sort(Random_list)
    print('Sort random list by insertion, time{}'.format(time.time() - Start))

    Start = time.time()
    _, sorted_list = Quick_sort_first(Random_list)
    print('Sort random list by Quick Sort using the first as pivot, time{}'.format(time.time() - Start))

    Start = time.time()
    _, sorted_list = Quick_sort_random(Random_list)
    print('Sort random list by Quick Sort using a random num as pivot, time{}'.format(time.time() - Start))
