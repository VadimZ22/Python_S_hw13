from myErrors import ValueTriangleError, ObjectError

class Triangle:

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <=0:
            raise ValueTriangleError(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b},{self.c}'

    def __eq__(self, other):
        if isinstance(other, Triangle):
            first = sorted((self.a, self.b, self.c))
            second = sorted((other.a, other.b, other.c))
            return first == second
        raise ObjectError(other, Triangle)

a = Triangle(2,2,2)
print(a == 10)




