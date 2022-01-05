

def thesaurus(args) -> dict:
    dict_out = {}
    for el in args:
        if el[0] in dict_out and el not in dict_out[el[0]]:
            dict_out[el[0]].append(el)
        else:
            dict_out[el[0]] = [el]
    return dict_out


def thesaurus_adv(*args) -> dict:
    my_dict = {}
    for el in args:
        idx = el.find(' ') + 1
        if el[idx] not in my_dict:
            my_dict[el[idx]] = [el]
        else:
            my_dict[el[idx]].append(el)
    result = {}
    for el in my_dict:
        result[el] = thesaurus(my_dict.get(el))
    return result


my_sort = thesaurus_adv("Иван Сергеев", "Инна Серова", "Юлия Абрикосова", "Петр Алексеев", "Илья Иванов",
                        "Анна Савельева")
bask = []
for elem in my_sort:
    bask += elem
bask.sort()
for elem in bask:
    print(elem, my_sort.get(elem))
