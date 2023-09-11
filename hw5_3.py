# Создайте функцию генератор чисел Фибоначчи


def fibon(n):
    a, b = 0, 1
    # lst = [a,b]
    for i in range(n):
        a, b = b, a + b
        # lst.append(b)
    yield b

n = 10
for i in range(n):
     print(next(fibon(i)), end=' ')
print(next(fibon(n)))