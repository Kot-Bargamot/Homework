def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    el = 0  # счетчик
    while el < len(list_in):
        starts = ''
        if list_in[el].startswith(('+', '-')):
            starts = list_in[el][0]
            list_in[el] = list_in[el].strip('+-')
        if list_in[el].isdigit():  # находим числа
            list_in[el] = f"{starts}{int(list_in[el]):02d}"
            list_in.insert(el, '"')
            list_in.insert(el + 2, '"')
            el += 2
        el += 1
    str_out = ' '.join(list_in)
    count = 0
    while ' " ' in str_out:  # убираем лишние пробелы
        if count % 2 == 0:
            str_out = str_out.replace(' " ', ' "', 1)
        if count % 2 != 0:
            str_out = str_out.replace(' " ', '" ', 1)
        count += 1
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
