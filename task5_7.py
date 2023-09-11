# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def is_prime(num):
    if num == 2:
        return True
    elif not num % 2:
        return False
    else:
        for dev in range(3, num // 2 + 1, 2):
            if not num % dev:
                return False
                break
        else:
            return True

def prime_number(n):
    count = 0
    num = 2
    lst = []
    while count <= n:
        if is_prime(num):
            lst.append(num)
        count += 1
        num += 1
    yield lst

n = 7
print(is_prime(n))
print(next(prime_number(n)))
