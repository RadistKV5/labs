# TODO импортировать необходимые молули

import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла

    input_file = open(INPUT_FILENAME, "r")
    output_file = open(OUTPUT_FILENAME, "w")
    reader = csv.DictReader(input_file)
    csv_to_json = []
    for i in reader:
        csv_to_json.append(i)


    ...  # TODO Сериализовать в файл с отступами равными 4
    json.dump(csv_to_json, output_file, indent=4)
    output_file.close()
    input_file.close()


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
