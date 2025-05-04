import sys


def search_in_file(filename, keyword):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование программы: python3 extract_path_value.py <имя файла> <искомое слово>")
        sys.exit(1)

    search_in_file(sys.argv[1], sys.argv[2])
