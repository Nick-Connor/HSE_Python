documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
]

directories = {"1": ["2207 876234", "11-2"], "2": ["10006"], "3": []}


def get_owner_by_document_number(doc_number):
    """Найти владельца документа по номеру"""
    for doc in documents:
        if doc["number"] == doc_number:
            return doc["name"]
    return None


def get_shelf_by_document_number(doc_number):
    """Найти полку документа по номеру"""
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return None


def handle_p_command():
    """Обработка команды p - поиск владельца документа"""
    doc_number = input("Введите номер документа: ")
    owner = get_owner_by_document_number(doc_number)

    if owner:
        print(f"Владелец документа: {owner}")
    else:
        print("Владелец документа: владелец не найден")


def handle_s_command():
    """Обработка команды s - поиск полки документа"""
    doc_number = input("Введите номер документа: ")
    shelf = get_shelf_by_document_number(doc_number)

    if shelf:
        print(f"Документ хранится на полке: {shelf}")
    else:
        print("Документ не найден на полках")


def main():
    """Основная функция программы"""
    print("Добро пожаловать в систему управления документами!")
    print("Доступные команды:")
    print("p - найти владельца документа")
    print("s - найти полку документа")
    print("q - выйти из программы")

    while True:
        command = input("\nВведите команду: ").strip().lower()

        if command == "q":
            print("Выход из программы. До свидания!")
            break
        elif command == "p":
            handle_p_command()
        elif command == "s":
            handle_s_command()
        else:
            print("Неизвестная команда. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()
