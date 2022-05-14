from json import load
from os.path import join
from os import getcwd


def read_json_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        return load(file)


def get_answers(data):
    print('Узнаем какая вы рыба!')
    list_answers = []
    keys_ = []
    for line in data:
        correct = False
        while not correct:
            print(line["text"])
            for key, value in line["options"].items():
                print(f'{key}) {value}')
            answer = input('Введите ответ: ').lower()
            keys_ = list(line["options"].keys())
            question_keys = list(map(str.lower, line["options"].keys()))
            question_answers = list(map(str.lower, line["options"].values()))
            if answer in question_keys:
                list_answers.append(answer.title())
                correct = True
            elif answer.lower() in question_answers:
                for key, value in line["options"].items():
                    if answer.lower() == value.lower():
                        list_answers.append(key)
                        correct = True
            else:
                print('Не верный ввод ответа, проверьте раскладку клавиатуры')
    return list_answers, keys_


def get_result(list_answers):
    user_answers_ = list_answers[0]
    answers_ = list_answers[1]
    dict_counter = {}
    max_count = 1
    max_key = None
    for point in answers_:
        dict_counter[point] = user_answers_.count(point)
    for key, value in dict_counter.items():
        if value > max_count:
            max_count = dict_counter[key]
            max_key = key
    return max_key


def main():
    file_path = join(getcwd(), 'task_five_files', 'questions.json')
    data_file = read_json_file(file_path)
    user_answers = get_answers(data_file)
    user_key = get_result(user_answers)
    answers_dict = {
        'A': 'Вы — стайная селедка.',
        'B': 'Вы — задумчивая камбала.',
        'C': 'Вы — активная щука.',
    }
    if user_key is None:
        print('Мы не смогли определить, кто вы. Будете лещом!')
    else:
        print(answers_dict[user_key])


if __name__ == '__main__':
    main()
