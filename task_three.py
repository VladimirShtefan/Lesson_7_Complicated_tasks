def mapper(data, data_map):
    mapped_data = {}
    for key, value in data.items():
        mapped_data[data_map[key]] = value
    return mapped_data


def main():
    keys_map = {"f": "surname", "i": "name", "o": "patronymic"}
    user_data = {
        "f": "Альшевский",
        "i": "Марк",
        "o": "Игоревич"
    }
    print(mapper(user_data, keys_map))


if __name__ == '__main__':
    main()
