immutable_var = (1, 5, 'Енот', False)
print(immutable_var)
#immutable_var[0] = 'Дерево' # В кортеже нельзя изменить элементы. Только если в него входит изменяемый элемент, например список, можно внести изменения в этот список, а остальные элементы изменить не получится. Записала в итоге всю строку как комментарий, тк после ошибки не выполнялись последующие команды.
mutable_list = [3, 8.6, 'Лютик', True]
mutable_list[1] = 'Одуванчик'
print(mutable_list)