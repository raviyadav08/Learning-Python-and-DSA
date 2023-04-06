"""
1.create any set anf try to use frozenset(setname)
"""
fruits = {'apple','banana',"mango",'banana','apple'}
fs = frozenset(fruits)
print(f'Fruits : {fruits}')
print(f'Frozen set of Fruits : {fs}')

"""
Find the elements in a given set that are not in another set

    set1 = {1,2,3,4,5}
    set2 = {4,5,6,7,8}

    diffrence between set1 and set2 is {1,2,3}
"""
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print('Union : ',set1|set2)
print('Difference : ',set1-set2)
print('Intersection : ',set1&set2)
print('Subset : ',set1<set2)