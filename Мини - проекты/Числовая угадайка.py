import random

print("Добро пожаловать в числовую угадайку!")


def is_valid(player_guess, finish):
    if 1 <= player_guess <= finish:
        return True
    else:
        return False


def game():
    finish = input("Выберите диапазон, в котором я буду загадывать число - от 1 до ")
    while not finish.isdigit():
        finish = input(
            "Введите корректное значение! Правая граница должна быть целым числом!\n"
        )
    finish = int(finish)
    r = random.randint(1, finish + 1)
    print(
        f"Я загадал определенное число в диапазоне от 1 до {finish}\nПопробуйте отгадать его!"
    )
    count = 0
    while True:
        player_guess = input()
        while not player_guess.isdigit():
            player_guess = input(
                "Упс. Я Вас не понимаю. Введите корректное значение:\n"
            )
        player_guess = int(player_guess)

        if is_valid(player_guess, finish) != True:
            print(f"А может быть все-таки введем целое число в выбранном диапазоне?")
            continue
        else:
            count += 1
            if player_guess < r:
                print("Ваше число меньше загаданного, попробуйте еще разок")
            elif player_guess > r:
                print("Ваше число больше загаданного, попробуйте еще разок")
            else:
                print(f"Вы угадали, поздравляем!\nКоличество Ваших попыток: {count}")
                restart = input(f"Хотели бы Вы сыграть еще раз?\n")
                while restart.lower().strip() not in ["да", "нет"]:
                    restart = input("Упс. Я Вас не понимаю. Выберите: Да или Нет\n")
                if restart.lower().strip() == "да":
                    print("Отлично! Сыграем еще раз!")
                    game()
                else:
                    print("Жаль, что Вы передумали играть! Всего доброго!")
                break


game()
