from module_5_1 import House

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1.__str__())
print(h2.__str__())
print(h1.__len__())
print(h2.__len__())

# Чтобы не копировать код класса и не занимать память дополнила класс методами нужными для решения задания
# и импортировала его из модуля где он прописан.



# Само задание:
#
# Домашняя работа по уроку "Специальные методы классов"
# Если вы решали старую версию задачи, проверка будет производиться по ней.
#
# Цель: понять как работают базовые магические методы на практике.
#
# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# # __str__
# print(h1)
# print(h2)
#
# # __len__
# print(len(h1))
# print(len(h2))
#
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20
