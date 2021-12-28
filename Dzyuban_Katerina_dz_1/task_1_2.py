def sum_list_1(my_list: list) -> int:
    """Вычисляет сумму чисел списка, сумма цифр которых делится нацело на 7"""
    result = 0
    for el in my_list:
        summ = 0
        el_x = 0 + el
        while el_x >= 1:
            summ += el_x % 10
            el_x = el_x // 10
        if (summ % 7) == 0:
            result += el
    return result


def sum_list_2(my_list: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    result = 0
    for el in my_list:
        el += 17
        summ = 0
        el_x = 0 + el
        while el_x >= 1:
            summ += el_x % 10
            el_x = el_x // 10
        if (summ % 7) == 0:
            result += el
    return result


my_list = []
for i in range(1001):
    my_list.append(i ** 3)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
