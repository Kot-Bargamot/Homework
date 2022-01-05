def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    dictionary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    str_out = dictionary.get(value)
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
