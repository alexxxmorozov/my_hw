#  Задача 1
my_str = "10305670554033400"
my_list = []
my_list.append(my_str)
my_str.count("0")

# Задача 2
a = 103000000
b = str(int(str(a)[::-1]))
c = len(str(a))-len(b)

# Задача 3
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_2 = ['Alex', 'John', 'Liza', 'Edward']
my_result = []
my_result.extend(my_list_1[1::2])
my_result.extend(my_list_2[::2])

# Задача 4
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = []
new_list.extend(my_list[1::])
new_list.extend(my_list[0:1:])

# Задача 5
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list.extend(my_list[0:1:])
my_list.pop(0)

Задача 6
my_string = 'У меня 15 яблок и 27 груш'
my_list = my_string.split()
result = 0

for index in range(len(my_list)):
    if my_list[index].isdigit():
        result += int(my_list[index])

# Задача 7
my_str = 'Сегодня я выучил прекрасный стих'
l_limit = 'д'
r_limit = 'т'

sub_str = my_str[(my_str.find(l_limit) + 1):my_str.rfind(r_limit)]

# Задача 8

my_str = '8163264128'
my_list = list()

for index in range(0, len(my_str), 2):
    if index < len(my_str) - 1:
        my_list.append(my_str[index] + my_str[index + 1])
    else:
        my_list.append(my_str[index] + "_")

print(my_list)

Задача 9
my_list = [4, 6, 1, 7, 2, 8, 2, 5, 2, 6, 7, 1, 9, 3, 5, 0, 0, 7, 2]
result = 0

for index in range(1, len(my_list) - 1):
    if my_list[index] > my_list[index - 1] + my_list[index + 1]:
        result += 1

print('Результат:', result)