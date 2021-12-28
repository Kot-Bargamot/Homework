def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    result = ''
    if 10 < number < 15:
        result = f"{number} процентов"
    elif number % 10 == 1:
        result = f"{number} процент"
    elif 1 < (number % 10) < 5:
        result = f"{number} процента"
    else:
        result = f"{number} процентов"
    return result


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
