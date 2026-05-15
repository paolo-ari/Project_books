import json
import os
from datetime import datetime

# Путь к файлу с данными
BOOKS_FILE = 'books.json'


def load_books():
    """Загружает список книг из файла books.json.
    Если файла нет или он пустой, возвращает пустой список."""
    if os.path.exists(BOOKS_FILE):
        try:
            with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                else:
                    print("Предупреждение: файл books.json содержит некорректные данные. Создаётся новый список.")
                    return []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при чтении файла: {e}. Создаётся новый список.")
            return []
    else:
        # Если файла нет, создаём его с пустым списком
        save_books([])
        return []

def save_books(books):
    """Сохраняет список книг в файл books.json."""
    try:
        with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=4)
        print("Данные успешно сохранены.")
    except IOError as e:
        print(f"Ошибка при сохранении файла: {e}")

def main():
    books = load_books()

    while True:
        print("\n" + "="*40)
        print("ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
        print("="*40)
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        print("-"*40)

        choice = input("Выберите пункт меню (1–6): ").strip()

        if choice == '1':
            print("→ Реализация в ветке feature/add-book")
            # Здесь будет вызов функции добавления книги
            pass

        elif choice == '2':
            print("→ Реализация в ветке feature/list-and-stats")
            # Здесь будет вывод всех книг
            pass

        elif choice == '3':
            print("→ Реализация в ветке feature/list-and-stats")
            # Здесь будет расчёт и вывод средней оценки
            pass

        elif choice == '4':
            print("→ Реализация в ветке feature/list-and-stats")
            # Здесь будет статистика по авторам
            pass

        elif choice == '5':
            print("→ Реализация в ветке feature/delete")
            # Здесь будет удаление книги
            pass

        elif choice == '6':
            print("Выход из программы. До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()
