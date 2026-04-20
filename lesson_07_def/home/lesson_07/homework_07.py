# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier * number <= 25:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def two_numbers_sum(a,b):
    return a+b
print(two_numbers_sum(7,9))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_num(a,b,c,d,e,f,g):
    numbers = [a,b,c,d,e,f,g]
    return sum(numbers)/len(numbers)
print(average_num(3,6,8,9,2,1,7))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_str(letters):
    return letters[::-1]
print(reverse_str('iweyuwey'))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    return max(words, key = len)
print(longest_word(["planet", "Earth", "Sun", "Mars"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7 Знайдіть всі унікальні елементи в списку small_list
def unic_list(numbers):
    unique = set(numbers)
    return list(unique)
print(unic_list([1,6,4,7,8,7,5,7,8,9,4,6,7]))

# task 8 Обчисліть суму елементів двох множин, які не є спільними

def sum_of_set_elements(set_1,set_2):
        result = set_1 | set_2
        return result
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
print(sum_of_set_elements(set_1, set_2))

# task 9 Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
def sum_dict(base_dict, add_dict):
    str_1 = str(base_dict)
    str_2 = str(add_dict)
    return str_1 + str_2
print(sum_dict(base_dict, add_dict))
# task 10 Обчисліть площу кола з радіусом 7.5. Використайте значення π = 3.14159
def area_of_circle(r):
    π = 3.14159
    s = π * r**2
    return s
r = 7.5
print(area_of_circle(r))
    
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""