from json import load
from os.path import join
from os import getcwd


def read_json_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        return load(file)


def get_sort_dict(list_dict):
    country_dict = {}
    for citi in list_dict:
        citi_param = citi['fields']
        if citi_param['country_ru'] not in country_dict.keys():
            country_dict[citi_param['country_ru']] = [citi_param['name']]
        else:
            country_dict[citi_param['country_ru']].append(citi_param['name'])
    return country_dict


def get_result_text(result_dict):
    for key, value in result_dict.items():
        citi_in_country = '\n- '.join(value)
        print(f"""{key}:
- {citi_in_country}
""")


def main():
    file_path = join(getcwd(), 'task_one_files', 'cities.json')
    cities_list = read_json_file(file_path)
    cities_dict = get_sort_dict(cities_list)
    get_result_text(cities_dict)


if __name__ == '__main__':
    main()
