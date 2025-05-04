## Задания от Радиочастотных сиситем

## 2) **Написать команду в Linux которая будет:**
- Будет печать строку "Hello, DevOps!"
- Записывать её в файл hello.txt  в домашней директории
- Выводить содержимое файла на экран

**Реализовал команду следующим образом:**
   ```
  #!/bin/bash
  echo "Hello, DevOps!" > ~/hello.txt && cat ~/hello.txt
  ```
**Как работает:**
- Перенаправляет вывод команды echo в файл hello.txt и с помощью логического оператора &&(И) вызывает команду cat для отображения содержимого файла hello.txt

## 3) **Написать команду в Linux которая будет:**
- Читать /var/log/syslog (или любой другой лог или файл).
- Искать строки с "error" или любым другим словом.
- Выводить 5 первых совпавших с шаблоном строк.
- Это нужно сделать одной командой, используя конвейеры (pipes).

**Реализовал команду следующим образом:**
   ```
  #!/bin/bash
  grep -i "Нужное слово" /var/log/syslog | head -n 5
   ```
**Как работает:**
- Перенаправляет вывод команды grep(ключ -i делает поиск регистронезависимым) на ввод команды head(где она в свою очередь выводит первые 5 строк)

## 4) **Bash/python-скрипт**
- Имеется файл в котором следующий набор строк:

name: test \
path: /home/user/data \
file: data.txt \
port:8080 \
log path: /var/log/app
- Необходимо написать скрипт на bash или python, который будет искать в этом файле конкретные слова (например, path) и выводить найденные строки.

Реализовал сложный вариант: с передачей имени файла и искомого слова как параметры функции.

**Реализация скрипта:**

   ```
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
        print("Использование программы: python3 extract_path_value.py <имя файла> <искомое слово> ")
        sys.exit(1)

    search_in_file(sys.argv[1], sys.argv[2])
   ```
# Запуск скрипта

Запуск осуществляется командой:

   ```
   python3 extract_path_value.py <имя файла> <искомое слово>
   ```
## 5) **Оптимизировать следующий Dockerfile, в котором прописан запуск скриптов из пункта 2:**

```
   FROM ubuntu:latest
   RUN apt-get update
   RUN apt-get install -y wget
   RUN apt-get install -y pytho3
   RUN apt-get install -y python3-pip
   COPY search_path.sh /tmp/search_path.sh
   COPY extract_path_value.py /tmp/extract_path_value.py
   COPY config.txt /tmp/config.txt
   RUN chmod +x /tmp/search_path.sh
   RUN chmod +x /tmp/extract_path_value.py
   ```
**Реализация задания**

К этому заданию я приложу 2 решения основанных на взятии разных образов для сборки.

- 1 решение(на базе образа ubuntu):

```
FROM ubuntu:22.04 AS builder

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

FROM builder

COPY search_path.sh extract_path_value.py config.txt /tmp/
```
Чтобы сборка была быстрее разделил установку пакетов и копирование файлов по шагам(stage). \
В первом шаге(stage) установка пакетов, а во втором переиспользую образ из первого stage в финальный образ с копированием необходимых файлов. \
Из мелочей хочу отметить: явное указание версии образа(небезопасно использовать latest(может быть проблема с зависимостями)), убрал установку пакета wget т.к. не вижу надобности его использования, убрал слои с назначением прав на использование скриптов(они и так запустятся).
- 2 решение(на базе образа alpine):

```
FROM alpine:3.21.3 AS builder

RUN apk update && \
    apk add --no-cache \
    python3 \
    py3-pip \
    bash \
    && rm -rf /var/cache/apk/*

FROM builder

COPY search_path.sh extract_path_value.py config.txt /tmp/
```
Ничего принципиально нового по сравнению с предыдущим решением, но решил дать шанс т.к. финальный размер образа будет меньше благодаря использованию alpine.

# Сухие числа

**Как можем видеть, финальный размер образов сильно отличаются.**
```
REPOSITORY     TAG       IMAGE ID       CREATED              SIZE
base_build     latest    406bba81f09a   28 minutes ago       557MB
ubuntu_build   latest    16b8399a33cb   About a minute ago   127MB
alpine_build   latest    04edf8d20ea3   About a minute ago   68.5MB
```