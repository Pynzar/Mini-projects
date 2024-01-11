def direction():
    direction = input("Что будет делать программа: шифровать или дешифровать?\n")
    while direction.lower() not in ["шифровать", "дешифровать"]:
        direction = input("Выберите корректный вариант ответа: \n")
    if direction.lower() == "шифровать":
        return True
    else:
        return False


def language():
    language = input("На каком языке будет текст: русский или английский?\n")
    while language not in ["русский", "английский"]:
        language = input("Выберите корректный вариант ответа: \n")
    if language.lower() == "русский":
        return True
    else:
        return False


def rotation():
    rot = input("Выберите шаг шифра: \n")
    while not rot.isdigit():
        rot = input("Введите корректный ответ: \n")
    return int(rot)

en_alphabet = [chr(i) for i in range(65,91)] + [chr(j) for j in range(97,123)]
ru_alphabet = [chr(i) for i in range(1040,1104)]


def cipher():
    if direction():
        if language():
            alphabet = ru_alphabet; moch = 32
        else:
            alphabet = en_alphabet; moch = 26
        
        rot = rotation()
        text = input('Введите Ваш текст: \n')
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].isupper():
                    print(alphabet[(alphabet.index(text[i]) + rot) % moch], end='')
                else:
                    print(alphabet[(alphabet.index(text[i]) + rot) % moch + moch], end='')
            else:
                print(text[i], end = '')
    else:
        if language() == True:
            alphabet = ru_alphabet; moch = 32
        else:
            alphabet = en_alphabet; moch = 26
        rot = rotation()
        text = input('Введите Ваш текст: \n')
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i].isupper():
                    print(alphabet[(alphabet.index(text[i]) - rot) % moch], end='')
                else:
                    print(alphabet[(alphabet.index(text[i]) - rot) % moch + moch], end='')
            else:
                print(text[i], end = '')


cipher()