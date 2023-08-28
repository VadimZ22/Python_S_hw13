
class MyException(Exception):
    pass

class FormatError(MyException):

    def __init__(self, name, marker: str):
        self.name = name
        self.marker = marker

    def __str__(self):
        if self.marker == 'not_is_title':
            return f'Неверный формат записи! Фамилия, имя отчество должны начинаться с заглавной буквы! {self.name}'
        if self.marker == 'digit_in_name':
            return f'Неверный формат записи! В ФИО не должно быть цифр! {self.name}'


class ValueTriangleError(MyException):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Длина стороны треугльника должна быть больше 0! {self.a}, {self.b}, {self.c}'

class ObjectError(MyException):

    def __init__(self, obj, cls):
        self.obj = obj
        self.cls = cls

    def __str__(self):
        return f'Объект {self.obj} не является экземпляром класса {self.cls.__name__}'

