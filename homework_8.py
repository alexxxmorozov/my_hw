# Homework 8 by Morozov Alex
# Задача 01

my_list = ['Сегодня', 'амам', 'приготовит,', 'енм', 'икичнилб']
new_list = list()

for index in range(0, len(my_list)):
    if not index % 2:
        new_list.append(my_list[index])
    else:
        new_list.append(my_list[index][::-1])

# Задача 02

my_list = ['iPhone', 'Android', 'Kinder', 'Armani', 'Alpha', 'NASA', 'Aliexpress']
results_list = list()

for value in my_list:
    if value[0] == 'A':
        result_list.append(value)

# Задача 3

my_list = ['iPhone', 'Android', 'Kinder', 'Armani', 'Alpha', 'NASA', 'Aliexpress']
results_list = list()

for letter in my_list:
    if 'a' in letter:
        result_list.append(letter)

# Задача 4

my_list = ['Киев', 64, 32, 8, 'Украина','Беларусь', 0, -20]
results_list = list()

for str_value in my_list:
    if type(str_value) == str:
        result_list.append(str_value)

# Задача 5

my_str = 'bbbkggffhhgymnmnmnicccxxv'
result_list = list()

for char in set(my_str):
    if my_str.count(char) == 1:
        result_list.append(char)

# Задача 6

my_str1 = 'AlexJonhMorozov'
my_str2 = 'AlexMattMorozov'

result_list = list(set(my_str1) & set(my_str2))

# Задача 7

my_str1 = '123qwert890'
my_str2 = '890dfghj123'
result_list = list()

for char in set(my_str2):
    if my_str1.count(char) == my_str2.count(char) == 1:
        result_list.append(char)

# Задача 8

residence_dict = {'Страна': 'Украина',
                  'Город': 'Киев',
                  'Улица': 'Анны Ахматовой'}

work_dict = {'Наличие': True,
             'Должность': 'Грузчик'}

my_dict = {'Фамилия': 'Андрейченко',
           'Имя': 'Евгений',
           'Возраст': '25',
           'Проживание': residence_dict,
           'Работа': work_dict}

# Задача 9

cake_dict = {'Мука': 500,
             'Молоко': 250,
             'Масло': 150,
             'Яйцо': 4}

cream_dict = {'Сахар': 100,
              'Масло': 100,
              'Ваниль': 50,
              'Сметана': 250}

glaze_dict = {'Какао': 150,
              'Сахар': 150,
              'Масло': 100}

ingredients_dict = {'Коржи': cake_dict,
                    'Крем': cream_dict,
                    'Глазурь': glaze_dict}

# Задача 10

persons = [{"name": "John", "age": 21},
           {"name": "Alex", "age": 15},
           {"name": "Samuel", "age": 37},
           {"name": "Andrew", "age": 15}]

# а)
min_age = 9999
min_age_names = list()

for human in persons:
    if human.get('age') == min_age:
        min_age_names.append(human.get('name'))
    elif human.get('age') < min_age:
        min_age = human.get('age')
        min_age_names.clear()
        min_age_names.append(human.get('name'))

print('Самый молодой человек из списка:')
for name in min_age_names:
    print(name, '-', min_age, 'лет')
print()

# б)
max_len_name = 0
max_len_names = list()

for human in persons:
    if len(human.get('name')) == max_len_name:
        max_len_names.append(human.get('name'))
    elif len(human.get('name')) > max_len_name:
        max_len_name = len(human.get('name'))
        max_len_names.clear()
        max_len_names.append(human.get('name'))

print('Самое длинное имя из списка:')
for name in max_len_names:
    print(name, '- длинна', max_len_name, 'букв')

# в)
average_age = 0

for human in persons:
    average_age += human.get('age')

average_age /= len(persons)

# Задача 11

my_dict_1 = {'Key1': 'Value1',
             'Key2': 'Value2',
             'Key3': 'Value3'}

my_dict_2 = {'Key1': 77777777,
             'Key4': 'Value4',
             'Key5': 'Value5'}

# а)
result_list1 = list(set(list(my_dict_1.keys()) + list(my_dict_2.keys())))

# б)
result_list2 = list(set(my_dict_1.keys()) - set(my_dict_2.keys()))

# в)
result_dict = dict()

for value in result_list2:
    result_dict[value] = my_dict_1.get(value)

# г)
new_dict = dict()

for key in result_list1:
    if key in my_dict_1 and key in my_dict_2:
        new_dict[key] = [my_dict_1.get(key), my_dict_2.get(key)]
    elif key in my_dict_1:
        new_dict[key] = my_dict_1.get(key)
    else:
        new_dict[key] = my_dict_2.get(key)