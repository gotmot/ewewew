def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


def main():
    try:
        user_input = input("Введите список чисел через пробел: ")
        numbers = [int(x) for x in user_input.split()]

        if not numbers:
            print("Список пуст.")
            return

        max_val = numbers[0]
        for num in numbers:
            if num > max_val:
                max_val = num
        print(f"Максимальное значение в списке: {max_val}")
        sorted_numbers = selection_sort(numbers.copy())
        print(f"Отсортированный список: {sorted_numbers}")

        search_target = int(input("Введите число для поиска: "))
        count = 0
        for num in numbers:
            if num == search_target:
                count += 1
        print(f"Число {search_target} встречается {count} раз(а) в списке.")

    except ValueError:
        print("Ошибка: Пожалуйста, вводите только целые числа через пробел.")


if __name__ == "__main__":
    main()
