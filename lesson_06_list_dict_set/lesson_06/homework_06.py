# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
unic_elements = set(small_list)
print("Task #1")
print(unic_elements)


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
middle_num = sum(small_list)/len(small_list)
print("Task #2")
print(middle_num)

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
dublicates_in_list = len(big_list) !=len(set(big_list))
print("Task #3")
print(f'У списку є дублікати: {dublicates_in_list}')

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

max_value = max(add_dict.values())
print("Task #4")
print(f'Максимальне значення у словнику: {max_value}')

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})

swaped_base_dict = {value: key for key, value in base_dict.items()}
print("Task #5")
print(swaped_base_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
#base_dict.update(add_dict)
print("Task #6")
str_base_dict = str(base_dict)
str_add_dict = str(add_dict)
print(str_base_dict)
print(str_add_dict)
result = (str_base_dict + str_add_dict)
print(result)


# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"

line_set = set(result)
print("Task #7")
print(line_set)
# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

set_3 = set_1 ^ set_2
sum_set_3 = sum(set_3)
print("Task #8")
print(f'Суму елементів двох множин, які не є спільними: {sum_set_3}')

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_001 = [2,4,9,6,5,3]
list_002 = [7,8,9,5,3,1]
set_001 = set(list_001)
set_002 = set(list_002)
final_set = set_001 ^ set_002
print("Task #9")
print(final_set)


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32), ('David', 28), ('Emma', 22), ('Frank', 45)]
print("Task #10")
person_age_dict = {}
for name, age in person_list:
    if 10 <= age < 20:
        key = '10-19'
    elif 20 <= age < 30:
        key = '20-29'
    elif 30 <= age < 40:
        key = '30-39'
    elif 40 <= age < 50:
        key = '40-49'
    else:
        continue
    if key not in person_age_dict:
        person_age_dict[key] = []
person_age_dict[key].append(name)
print(person_age_dict)
