def adv_counting_table(list1):
    max_list1 = max(list1)
    min_list1 = min(list1)
    length_tab = max_list1 - min_list1 + 1
    tab = [0] * length_tab
    for k in list1:
            tab[k - min_list1] +=1

    return tab

a=[6,5,7,5,8,13,4,5,7,2,4]
def sort_by_count(a):
    d=adv_counting_table(a)
    print(adv_counting_table(a))
    i=0
    e=0
    c = [0] * len(a)
    for j in range(0,len(d)):
        for i in range(0,d[j]):
             c[i+e]=min(a)+j
        e=e+d[j]     
    return c
print(sort_by_count(a))
        

