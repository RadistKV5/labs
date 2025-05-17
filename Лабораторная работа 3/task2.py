# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, sp=","):
    participants1 = str1.split(sp)
    participants2 = str2.split(sp)
    common = list(set(participants1).intersection(participants2))
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, sp="|"))