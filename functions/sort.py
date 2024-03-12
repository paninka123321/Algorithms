### Selection sort

def selection_sort(list1):
    for k in range(len(list1)-1):
        for j in range(k+1,len(list1)):
            if list1[k]> list1[j]:
                helper = list1[k]
                list1[k] = list1[j]
                list1[j] = helper
    return list1

### Another option:

def another_sort(list1):
    length = len(list1)
    consecutive_min_list = []
    
    for i in range(length):
        consecutive_min_list.append(min(list1))
        list1.remove(min(list1))
    
    return consecutive_min_list