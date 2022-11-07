
def get_count_char(str_main):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_

    # Здесь раньше был записан main_str =

    get_count_char = {}
    str_main = "".join(str_main.lower().split())

    DEFAULT_COUNT = 0

    for grade in str_main:
        if grade.isalpha():
            if grade in str_main:
                get_count_char[grade] = get_count_char.get(grade, DEFAULT_COUNT) + 1

    return get_count_char
main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """

print(get_count_char(main_str))
def get_char(dict_):
    dict_sum = sum(dict_.values())
    dict1_ = {}

    for grade in dict_:
        dict1_[grade] = dict1_[grade]/dict_sum * 100
    dict1_ = get_count_char(main_str)
    return dict1_
print(dict1_)