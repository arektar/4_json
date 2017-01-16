import json


def load_data(file_path):
    with open(file_path) as json_file:
        bars_data = json_file.read()
    return json.loads(bars_data)


def pretty_print_json(data):
    to_print = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
    return to_print


if __name__ == '__main__':
    my_file_path = input("Введите полное имя файла .json: ")
    json_data = load_data(my_file_path)
    to_show_data = pretty_print_json(json_data)
    print(to_show_data)
