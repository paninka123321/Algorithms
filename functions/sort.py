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


### Sorting by counting

def counting_sort(list1):
    max_list1 = max(list1)
    min_list1 = min(list1)
    length_tab = max_list1 - min_list1 + 1
    tab = [0] * length_tab
    sorted_list = []

    for k in list1:
            tab[k - min_list1] +=1
    
    first_el = min_list1
    for i in tab:
         sorted_list += i * [first_el]
         first_el += 1

    return sorted_list


## with use of import 
# import counting_table  #why it doesnt work?!

#def counting_sort_optimizated(list1):
    
#     tab = counting_table.adv_counting_table(list1)
    
#     first_el = min(list1)
#     for i in tab:
#          sorted_list += i * [first_el]
#          first_el += 1

 #  return sorted_list