def number_sequence(start, end, even=True):
    for num in range(start, end + 1):
        if even and num % 2 == 0:
            yield num
        elif not even and num % 2 != 0:
            yield num


def main():
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))

        print("Выберите тип последовательности:")
        print("1 — Чётные числа")
        print("2 — Нечётные числа")
        choice = input("Ваш выбор: ")

        is_even = True if choice == "1" else False

        result = list(number_sequence(start, end, even=is_even))

        if result:
            label = "чётных" if is_even else "нечётных"
            print(f"Последовательность {label} чисел: {result}")
        else:
            print("В данном диапазоне подходящих чисел не найдено.")

    except ValueError:
        print("Ошибка: Пожалуйста, вводите только целые числа.")


if __name__ == "__main__":
    main()
