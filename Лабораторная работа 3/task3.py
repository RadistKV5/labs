# TODO  Напишите функцию count_letters
def count_letters(strn):
    string = strn.lower()
    letters = []
    for i in range(len(string)):
        if string[i].isalpha():
            letters.append(string[i])
    string = letters
    letters_new = []
    for i in range(len(letters)):
        if letters[i] not in letters_new:
            letters_new.append(letters[i])
    letters = list(letters_new)
    letters_count = []
    for i in range(len(letters)):
        count = 0
        for n in range(len(string)):
            if letters[i] == string[n]:
                count += 1
        letters_count.append(count)
    letters_dict = {}
    for i in range(len(letters)):
        letter = letters[i]
        letters_dict[letter] = letters_count[i]
    return letters_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dictionary):
    string = main_str.lower()
    str_new = []
    for i in range(len(string)):
        if string[i].isalpha():
            str_new.append(string[i])
    letters_new = []
    for i in range(len(str_new)):
        if str_new[i] not in letters_new:
            letters_new.append(str_new[i])
    list_new = list(letters_new)
    for i in range(len(dictionary)):
        letter = list_new[i]
        dictionary[letter] = round(dictionary.get(letter)/len(str_new), ndigits=2)
        dictionary[letter] = "{:.2f}".format(dictionary[letter])
    for i in range(len(dictionary)):
        letter = list_new[i]
        print(letter + ":", dictionary[letter])


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
calculate_frequency(count_letters(main_str))