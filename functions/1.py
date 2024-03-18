def adv_counting_table(list1):
    max_list1 = max(list1)
    min_list1 = min(list1)
    length_tab = max_list1 - min_list1 + 1
    tab = [0] * length_tab
    for k in list1:
            tab[k - min_list1] +=1

    return tab

a=[6,5,7,5,8,13,4,5,7,2,4,0,0]
def sort_by_count(a):
    d=adv_counting_table(a)
    print(adv_counting_table(a))

    e=0
    c = [0] * len(a)
    for j in range(0,len(d)):
        for i in range(0,d[j]):
             c[i+e]=min(a)+j
        e=e+d[j]     
    return c
print(sort_by_count(a))

def universal_count_table(min_val,max_val,list):
     length_tab = max_val - min_val + 1
     tab = [0] * length_tab
     for k in list:
            tab[k - min_val] +=1

     return tab
     
        

# zad 1
a=[1,1,1,4]
c=adv_counting_table(a)
for i in range (0,len(a)):
     if c[i]==0 :
          print("Ciag nie jest permutacją")
          break
print("Ciag jest permutacjia")

# zad 2

import random
list=[]
b=random.randint(0,10)
for i in range(0,b):
    list.append(random.randint(0,b))
print(b)
print(list)
l=0
print(universal_count_table(0,b,list))
for j in range(0,1000):   
    for i in range(0,b):
        if universal_count_table(0,b,list)[i]==0:
            list.append(random.randint(0,b))
            print(universal_count_table(0,b,list))
            l=l+1
else:
    print("succ")
    print(l)

# zad 2 metoda lepsza

import random
list=[]
b=random.randint(0,10)
for i in range(0,b):
    list.append(random.randint(0,b))
print(list)
l=0
print(universal_count_table(0,b,list))
while universal_count_table(0,b,list).count(0)!=0:
    list.append(random.randint(0,b))
    l=l+1       
else:
    print(l)
    print(universal_count_table(0,b,list))
   

# zad 3   jak sie zabezpieczyc przed zla liczba????????????
    

n= int(input("Podaj liczbe przycisków:"))
m= int(input("Podaj liczbe prób:"))
lista=[]
tab=[0]*n
for i in range(0,m):
    x=int(input("Podaj wyraz listy"))
    lista.append(x)
    if x in range(1,n+1):
        tab[x-1]=tab[x-1]+1
    elif x==n+1:
        for j in range(0,n):
            tab[j]=max(tab)
print(n)
print(m)
print(lista)
print(tab)

   



