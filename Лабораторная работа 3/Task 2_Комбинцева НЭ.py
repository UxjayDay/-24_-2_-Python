def find_common_participants(first_group, second_group, separator = ","): # TODO Напишите функцию find_common_participants
    first_group_list = first_group.split(separator) # Разделяем строки на списки участников
    second_group_list = second_group.split(separator)
    common_participants = list(set(first_group_list) & set(second_group_list))  # Находим пересечение двух списков
    common_participants.sort() # Сортируем по алфавиту
    return common_participants # Возвращаем значение


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)

# TODO Провеьте работу функции с разделителем отличным от запятой
