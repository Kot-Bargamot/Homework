from itertools import zip_longest
from random import choices, sample

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "ром"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int, *args, uniq=False) -> list:
    """
    Возвращает список шуток в количестве count.
    Для уникальных шуток используйте именованный аргумент uniq
    """
    if uniq:
        list_out = list(zip_longest(*tuple(map(lambda el: sample(el, k=len(el)), args)), fillvalue='-'))[:count]
    else:
        list_out = list(zip(*tuple(map(lambda el: choices(el, k=count), args))))
    list_out = list(map(lambda el: ' '.join(list(el)), list_out))
    return list_out


print(get_jokes(10, nouns, adverbs, adjectives))
print(get_jokes(10, nouns, adverbs, adjectives, uniq=True))
