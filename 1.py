# -*- coding: utf-8 -*-

class First: # создал класс
    color = 'red' # отрибут со значением
    def out(self): # метод вывод color + !
        print(self.color + '!') # чет ничего не вывел

obj1 = First() # создали обхект который умеет делать все что умеет делать класс
obj2 = First() # второй объект который тоже все делает что и класс
# отрибуты obj1 и obj2 имеют два одинаковых отрибута color(ввиде свойства) и out (ввиде метода)

print(obj1.color) # red применили функцию print к свойствам объектов
#доступ через объект к отрибуту
obj1.out() # red!
# результат применения метода out к объектам


class Second:
    color = "red"
    form = "circle" # овал

    def changecolor(self, newcolor):
        self.color = newcolor

    def changeform(self, newform):
        self.form = newform


obj1 = Second()
obj2 = Second()

print(obj1.color, obj1.form)  # вывод на экран "red circle"
print(obj2.color, obj2.form)  # вывод на экран "red circle"

obj1.changecolor("green")  # изменение цвета первого объекта
obj2.changecolor("blue")  # изменение цвет второго объекта
obj2.changeform("oval")  # изменение формы второго объекта

print(obj1.color, obj1.form)  # вывод на экран "green circle"
print(obj2.color, obj2.form)  # вывод на экран "blue oval"


class Sek:
    color11 = 'red'
    form11 = 'oval'

    def fucolor (self, newcolor): # создал функцию которая при указании newcolor будет менять цвет в обхекте color
        self.color11 = newcolor

    def fuform (self, newform):
        self.form11 = newform

obj11 = Sek()
obj22 = Sek()

print (obj11.color11, obj11.form11)
print (obj22.color11, obj22.form11)

obj11.fucolor ('green')
obj11.fuform ('krug')
print(obj11.color11, obj11.form11)