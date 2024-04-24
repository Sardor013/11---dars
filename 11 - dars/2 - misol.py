def sonlar_soni(list_):
    count = 0
    for element in list_:
        if isinstance(element, int):
            count += 1
    return count

input_list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print("Listda", sonlar_soni(input_list), "ta integer bor.")
