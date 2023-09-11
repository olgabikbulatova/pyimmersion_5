# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def file_info(a: str) -> tuple:
    *_, name_ext = a.split('\\')
    name, ext = name_ext.split('.')
    return a, name, ext


a = "C:\\Users\\obikb\\PycharmProjects\\sem 5\\task5_1.py"
print(file_info(a))