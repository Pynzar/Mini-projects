import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!#$%&*+-=?@^_"
same = "il1Lo0O"

chars = ""


count_pass = input("Сколько паролей Вы бы хотели создать?\n")
while not count_pass.isdigit():
    count_pass = input(
        "Введите корректный ответ, который должен состоять из целого числа: \n"
    )
count_pass = int(count_pass)

length = input("Какая длина пароля Вам нужна?\n")
while not length.isdigit():
    length = input(
        "Введите корректный ответ, который должен состоять из целого числа: \n"
    )
length = int(length)


has_digits = input("Включать ли цифры?\n")
while has_digits.lower() not in ["да", "нет"]:
    has_digits = input('Ответ должен содержать "Да" или "Нет"\n')
if has_digits == "да":
    chars += digits

has_upper_letters = input("Включать ли прописные буквы?\n")
while has_upper_letters.lower() not in ["да", "нет"]:
    has_upper_letters = input('Ответ должен содержать "Да" или "Нет"\n')
if has_upper_letters == "да":
    chars += uppercase_letters


has_lower_letters = input("Включать ли строчные буквы?\n")
while has_lower_letters.lower() not in ["да", "нет"]:
    has_lower_letters = input('Ответ должен содержать "Да" или "Нет"\n')
if has_lower_letters == "да":
    chars += lowercase_letters

has_symbols = input("Включать ли символы?\n")
while has_symbols.lower() not in ["да", "нет"]:
    has_symbols = input('Ответ должен содержать "Да" или "Нет"\n')
if has_symbols == "да":
    chars += symbols

del_symbols = input("Исключать ли неоднозначные символы?\n")
while del_symbols.lower() not in ["да", "нет"]:
    del_symbols = input('Ответ должен содержать "Да" или "Нет"\n')
if del_symbols == "да":
    for i in same:
        chars = chars.replace(i, "")


def generate_password(length, chars):
    for i in range(count_pass):
        password = ""
        for x in range(length):
            password += random.choice(chars)
        print(password)


generate_password(length, chars)
