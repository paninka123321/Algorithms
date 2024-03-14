### Basic counting table - elements in the table start at 0 and end at the maximum number in the list

def basic_counting_table(list1):
    m=max(list1) + 1
    tab = [0] * m # filling table wits zeros

    for j in list1:
        tab[j]=tab[j]+1

    return tab

### Adv counting table - elements in the table start at minimum number and end at the maximum number in the list

def adv_counting_table(list1):
    max_list1 = max(list1)
    min_list1 = min(list1)
    length_tab = max_list1 - min_list1 + 1
    tab = [0] * length_tab
    for k in list1:
            tab[k - min_list1] +=1

    return tab

