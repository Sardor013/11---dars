def bosh_tupl(list_):
    return [tupl for tupl in list_ if tupl]

list1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
list2 = bosh_tupl(list1)
print("Bajarildi!:", list2)
