def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский, регистр первой буквы имеет значение """
    dictionary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if value.istitle():
        str_out = dictionary.get(value.lower()).title()
    else:
        str_out = dictionary.get(value)
    return str_out


print(num_translate_adv("one"))
print(num_translate_adv("Eight"))
