import math

#bubble(list) - > sorted list
def bubble(lst):
    for i in range(len(lst)-1):
        for i, v in enumerate(lst[0:-1]):
            if v > lst[i+1]:
                lst[i], lst[i+1]= lst[i+1], lst[i]
    return lst


#selection(list) -> sorted list
def selection(lst):
    for full_index in range(len(lst)-1):
        index_smallest = full_index+1
        for index, value in enumerate(lst[full_index:]):
            if value < lst[index_smallest]:
                index_smallest = index+full_index
        lst[index_smallest], lst[full_index] = lst[full_index], lst[index_smallest]
    return lst


#insertion(list) > sorted list
def insertion(lst:list):   
    for main_index, main_value in enumerate(lst[1:]):
        index = 0
        while main_value > lst[index]:
            index+=1
        popped = lst.pop(main_index+1)
        lst.insert(index, popped)
    return lst

#shell(List) -> sorted list
def shell(lst):
    gaps = []
    length = len(lst)
    while length > 1:
        length = length//2
        gaps.append(length)
    print(gaps)
    for gap in gaps:
        lst_starting_indices = list(range(len(lst)-1-gap))
        for i in lst_starting_indices:
            

#quicksort(list) -> sorted list
def quicksort(lst):
    pass


print(shell([5,4,3,2,1]))