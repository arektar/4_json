import json

def load_data(filepath):
    with open(filepath) as json_file:
        bars_data = json_file.read()
    return json.loads(bars_data)


def pretty_print_json(data):
    to_print=json.dumps(data, indent=4, sort_keys=True)
    return to_print


if __name__ == '__main__':
    filepath=input("Введите полное имя файла .json: ")
    json_data = load_data(filepath)
    to_show_data=pretty_print_json(json_data)
    print(to_show_data)
