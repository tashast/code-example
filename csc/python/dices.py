# DICES - список костей (каждая кость - список чисел на гранях).
# Найдите моды суммы, чётности суммы и младшей цифры суммы
# и выведите их каждую в своей строке.
# Если мод несколько, выведите их по возрастанию, через пробел
import collections
import itertools

def print_most_common(count_list):
    top_count = count_list[0][1]
    counts = []
    for element in count_list:
        if element[1] == top_count:
            counts.append(element[0])
    print(*(sorted(counts)))
    return

prod = itertools.product(DICES[0], DICES[1], DICES[2])

prod_list = list(prod)

list_sum = [sum(x) for x in prod_list]
list_elem = [x % 10 for x in list_sum]
list_even = [x % 2 for x in list_elem]

ans_1 = collections.Counter(list_sum).most_common()
print_most_common(ans_1)
ans_2 = collections.Counter(list_even).most_common()
print_most_common(ans_2)
ans_3 = collections.Counter(list_elem).most_common()
print_most_common(ans_3)
