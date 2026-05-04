"""
Тести для файлу tasks.py
Запуск: pytest test_tasks.py
"""
from functions_for_test import *

"""
📝 Завдання 1. Перевірка додавання чисел 
Напиши тест на функцію add(a, b), яка повертає суму двох чисел. 
Створи тест, який перевіряє кілька випадків: додавання додатних, від’ємних і нуля.
"""
def test_add():
    actual_result = add(9,6)
    expected_result = 15
    assert actual_result == expected_result
    actual_result = add(-9, -6)
    expected_result = -15
    assert actual_result == expected_result
    actual_result = add(-9, 0)
    expected_result = -9
    assert actual_result == expected_result 
    # TODO: додай тести для функції add

"""
📝 Завдання 2. Перевірка парності 
Функція is_even(n) повертає True, якщо число парне, інакше False. 
Напиши тести для кількох чисел: парних, непарних, від’ємних.
"""
def test_is_even():
    actual = is_even(4)
    expected = True
    assert actual == expected
    actual = is_even(5)
    expected = False
    assert actual == expected
    actual = is_even(-6)    
    expected = True
    assert actual == expected
    actual = is_even(-7)
    expected = False
    assert actual == expected 
    #TODO: додай тести для функції is_even


"""
📝 Завдання 3. Розворот рядка 
Функція reverse_string(s) повинна повертати рядок у зворотному порядку. 
Перевір: звичайний рядок, порожній рядок, рядок з одним символом.
"""
def test_reverse_string():
    string = "d,f,g,h,j"
    actual = reverse_string(string)
    expected = "j,h,g,f,d"
    print(actual)
    assert actual == expected
    # TODO: додай тести для функції reverse_string



"""
📝 Завдання 4. Мінімум у списку 
Функція find_min(nums) повертає найменший елемент списку. 
Протестуй для: звичайного списку, списку з одним елементом, списку з від’ємними числами.
"""
def test_find_min():
    nums = [3,6,9,6,2,7]
    actual = find_min(nums)
    expected = 2
    assert actual == expected
    nums = [9]
    actual = find_min(nums)
    expected = 9
    assert actual == expected
    nums = [-3,-6,-9,-6,-2,-7]
    actual = find_min(nums)
    expected = -9
    assert actual == expected 
    # TODO: додай тести для функції find_min


"""
📝 Завдання 5. Перевірка підрядка 
Функція contains_substring(s, sub) повертає True, якщо sub є в s. 
Протестуй випадки: підрядок є, підрядка нема, порожній підрядок.
"""
def test_contains_substring():
    actual = contains_substring("Wonderful Day", "Day")
    excepted = True
    assert actual == excepted
    actual = contains_substring("Wonderful Day", "Sunny")
    expected = False
    assert actual == expected
    actual = contains_substring("Wonderful Day", "")
    expected = True
    assert actual == expected
    # TODO: додай тести для функції contains_substring



"""
📝 Завдання 6. Факторіал 
Функція factorial(n) обчислює факторіал числа n. 
Протестуй: factorial(0), factorial(1), factorial(5).
"""
def test_factorial():
    actual = factorial(0)
    excepted = 1
    assert actual == excepted
    actual = factorial(1)
    excepted = 1
    assert actual == excepted
    actual = factorial(5)
    excepted = 120
    assert actual == excepted
    # TODO: додай тести для функції factorial


"""
📝 Завдання 7. Ділення з винятком 
Функція divide(a, b) ділить a на b. 
Перевір: звичайне ділення, ділення на від’ємне число, ділення на нуль (очікуваний ZeroDivisionError).
"""
def test_divide():
    actual = divide(9, 3)
    expected = 3
    assert actual == expected
    actual = divide(9, -3)
    expected = -3
    assert actual == expected
    actual = divide(9, 0)
    expected = ValueError("Ділення на нуль неможливе")
    assert actual == expected
    # TODO: додай тести для функції divide


"""
📝 Завдання 8. Паліндром 
Функція is_palindrome(s) перевіряє, чи є рядок паліндромом. 
Протестуй: паліндром, непаліндром, порожній рядок.
"""
def test_is_palindrome():
    word = "radar"
    actual = is_palindrome(word)
    expected = True
    assert actual == expected
    word = "random"
    actual = is_palindrome(word)
    expected = False
    assert actual == expected
    word = ""
    actual = is_palindrome(word)
    expected = True
    assert actual == expected

    # TODO: додай тести для функції is_palindrome



"""
📝 Завдання 9. Сума елементів списку 
Функція sum_list(nums) повертає суму всіх чисел у списку. 
Протестуй: звичайний список, порожній список, список з від’ємними числами.
"""
def test_sum_list():
    nums = 3,4,7,2,9,7,6
    actual = sum_list(nums)
    expected = 38
    nums = ()
    actual = sum_list(nums)
    expected = 0
    assert actual == expected
    nums = -3,-4,-7,-2,-9,-7,-6
    actual = sum_list(nums)
    expected = -38
    assert actual == expected 
    # TODO: додай тести для функції sum_list


"""
📝 Завдання 10. Конвертація в верхній регістр 
Функція to_upper(s) повертає рядок у верхньому регістрі. 
Протестуй: звичайний рядок, вже великими літерами, порожній рядок.
"""
def test_to_upper():
    text = "what a wonderful day"
    actual = to_upper(text)
    expected = "WHAT A WONDERFUL DAY"
    assert actual == expected
    text = "What A Wonderful Day"
    actual = to_upper(text)
    expected = "WHAT A WONDERFUL DAY"
    assert actual == expected
    text = ""
    actual = to_upper(text)
    expected = ""
    assert actual == expected

    # TODO: додай тести для функції to_upper

