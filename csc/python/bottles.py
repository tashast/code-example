# Значения, с которых начинается строка:
NUM_DICT = {1: "Одна", 2: "Две", 3: "Три", 4: "Четыре", 5: "Пять",\
            6: "Шесть", 7: "Семь", 8: "Восемь", 9: "Девять", 10: "Десять",\
            11: "Одиннадцать", 12: "Двенадцать", 13: "Тринадцать", \
            14: "Четырнадцать", 15: "Пятнадцать", 16: "Шестнадцать",\
            17: "Семнадцать", 18: "Восемнадцать", 19: "Девятнадцать",\
            20: "Двадцать", 30: "Тридцать", 40: "Сорок", 50: "Пятьдесят",\
            60: "Шестьдесят", 70: "Семьдесят", 80: "Восемьдесят", 90: "Девяносто"}
RETURN = '\n'
# Массив для перевода: первый индекс 0 -- singular, 1 -- paucal, 2 -- plural.
# Второй индекс 0 -- слово, 1 -- фраза в начале куплета, 2 -- фраза в конце куплета.
GRAMMARS = [[" бутылка", " стояла на столе,", " осталась на столе."],\
           [" бутылки", " стояли на столе,", " остались на столе."],\
           [" бутылок", " стояло на столе,", " осталось на столе."]]
# Фраза для окончания всех куплетов, кроме последнего:
END_LINE = "Одна из них упала,"
# Фраза для окончания последнего куплета:
THE_END = ["И вот она упала,", "Ни одной бутылки не осталось на столе!"]


def number_in_words(value_num):
    """" Перевести число value в текст по словарю NUM_DICT:
    если число есть в словаре, оно пишется с большой буквы,
    иначе составляется из двух элементов словаря, где единицы с маленькой буквы
    """
    if value_num in NUM_DICT:
        return NUM_DICT[value_num]
    digit_ones = value_num % 10
    digit_tens = value_num - digit_ones
    return ' '.join([NUM_DICT[digit_tens], NUM_DICT[digit_ones].lower()])


def get_grammar(value_num):
    """" Получить грамматическое число по value для массива GRAMMARS:
    от 11 до 19 plural, дальше в зависимости от числа единиц:
    1 -- singular; 2, 3, 4 -- paucal; 5, 6, 7, 8, 9, 0 -- plural
    """
    if 10 < value_num < 20:
        return 2
    res = value_num % 10
    if res == 1:
        return 0
    if res in [2, 3, 4]:
        return 1
    return 2


def print_lines(value_num):
    """" Составить куплет по value:
    первая строчка: X бутылок стояло на столе,
    вторая строчка: Х бутылок!
    # последние 2 строчки зависят от числа бутылок
    """
    grammar_begin = get_grammar(value_num)
    words = number_in_words(value_num)
    line_1 = ''.join([words, GRAMMARS[grammar_begin][0], GRAMMARS[grammar_begin][1]])
    line_2 = ''.join([words, GRAMMARS[grammar_begin][0], '!'])

    if value_num == 1:
        line_3 = RETURN.join(THE_END)
    else:
        value_end = value_num - 1
        grammar_end = get_grammar(value_end)
        words_end = number_in_words(value_end)
        line_3 = ''.join([END_LINE, RETURN, words_end,\
                          GRAMMARS[grammar_end][0], GRAMMARS[grammar_end][2], RETURN])

    return RETURN.join([line_1, line_2, line_3])


NUMBER_INPUT = int(input())

while NUMBER_INPUT > 0:
    print(print_lines(NUMBER_INPUT))
    NUMBER_INPUT -= 1