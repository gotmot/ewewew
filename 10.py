import os


def notes_app():
    file_name = "notes.txt"

    while True:
        print("\nДоступные команды: create, add, view, exit")
        choice = input("Введите команду: ").strip().lower()

        if choice == "create":
            with open(file_name, "w", encoding="utf-8") as f:
                pass
            print(f"Файл '{file_name}' создан и очищен.")

        elif choice == "add":
            note = input("Введите текст заметки: ")
            with open(file_name, "a", encoding="utf-8") as f:
                f.write(note + "\n")
            print("Заметка добавлена.")

        elif choice == "view":
            if not os.path.exists(file_name):
                print("Файл не найден. Сначала создайте файл.")
                continue

            with open(file_name, "r", encoding="utf-8") as f:
                lines = f.readlines()

                if not lines:
                    print("Файл пуст.")
                else:
                    print("Ваши заметки:")
                    for i, line in enumerate(lines, 1):
                        print(f"{i}. {line.strip()}")

        elif choice == "exit":
            print("Программа завершена.")
            break

        else:
            print("Неизвестная команда. Попробуйте снова.")


if __name__ == "__main__":
    notes_app()
