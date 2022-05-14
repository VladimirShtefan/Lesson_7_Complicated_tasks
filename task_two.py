from task_one import read_json_file
from os.path import join
from os import getcwd


def get_dict_with_pk(list_dict):
    new_dict = {}
    for citi in list_dict:
        new_dict[str(citi['pk'])] = citi['fields']
    return new_dict


def main():
    file_path = join(getcwd(), 'task_two_files', 'cities.json')
    cities_list = read_json_file(file_path)
    cities_dict = get_dict_with_pk(cities_list)
    print(cities_dict)


if __name__ == '__main__':
    main()
