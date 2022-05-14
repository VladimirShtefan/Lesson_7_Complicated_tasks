from itertools import combinations


dictionary = {
    'Носят шапочку': {'Бычок', 'Сельдь', 'Лосось', 'Скумбрия', 'Толстолобик', 'Карась'},
    'Любят гулять': {'Карась', 'Анчоус', 'Карп', 'Треска', 'Лещ', 'Лосось'},
    'Поют': {'Лещ', 'Камбала', 'Толстолобик', 'Сельдь', 'Бычок'},
    'Задумчивые': {'Окунь', 'Щука', 'Осетр', 'Бычок', 'Сельдь', 'Скумбрия'}
}


dictionary_keys = list(dictionary.keys())
combinations_list_two = list(combinations(dictionary_keys, 2))


for comb in combinations_list_two:
    print(f'{comb[0]} и {comb[1]}:')
    intersections = list(dictionary[comb[0]] & dictionary[comb[1]])
    if not intersections:
        print('Нет таких рыб')
    else:
        print('\n'.join(list(intersections)))


for key, value in dictionary.items():
    fishes_set = set()
    all_fishes = list(dictionary.keys())
    all_fishes.remove(key)
    for fishes in all_fishes:
        fishes_set |= dictionary[fishes]
    print(f'Не {key}:')
    result = '\n'.join(list(fishes_set.difference(dictionary[key])))
    print(result)

