
value = 110
new_value = value / 2 if value < 100 else -(value)

########################################

value = 1010
new_value = 1 if value < 100 else 0

########################################

value = 10
new_value = True if value < 100 else False

########################################

my_str = "0123456789"
print(my_str[0::2])

########################################

my_str = "0123456789"
print(my_str[0::2])

########################################
my_str = "01234"

print(my_str + my_str) if len(my_str) < 5 else print(my_str)

########################################

print(my_str + my_str[::-1]) if len(my_str) < 5 else print(my_str)