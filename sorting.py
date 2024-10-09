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
    gap = len(lst) // 2
    while gap > 0:
        # loops through all gap indices
        for i in range(gap, len(lst)):
            current = lst[i]
            
            temp_indice=i
            # this arranges all gap items, like a modified insertion sort
            while temp_indice >= gap and lst[temp_indice - gap] > current:
                lst[temp_indice] = lst[temp_indice-gap]
                temp_indice-=gap
                
            lst[temp_indice] = current
        gap//=2
    return lst
        

#quicksort(list) -> sorted list
def quicksort(lst, low_index = 0, high_index = None) -> list:
    if high_index is None:
        high_index = len(lst) - 1
    # run until low index and high index overlap
    if low_index < high_index:
        pivot = _partition(lst, low_index, high_index)
        quicksort(lst, low_index, pivot-1)
        quicksort(lst, pivot+1, high_index)
    return lst

def _partition(lst, low, high) -> int:
    pivot = lst[high] # Putting the pivot at the end so I only sort one side
    small_index = low-1
    # Loops through the list section and swaps items so all items to the right of pivot are smaller
    for i in range(low, high):
        if lst[i] <= pivot:
            small_index += 1
            lst[small_index], lst[i] = lst[i], lst[small_index]
    
    lst[small_index+1], lst[high] = lst[high], lst[small_index+1]
    
    return small_index + 1
        
        