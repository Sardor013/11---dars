def orta_arifmetik(list1, list2):
    total_sum = sum(list1) + sum(list2)
    total_count = len(list1) + len(list2)
    return total_sum / total_count


list1 = [1, 1, 3, 4, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

print("Ikkala listning o'rta arifmetigi:", orta_arifmetik(list1, list2))

