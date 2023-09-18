import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Ошибка: невозможно извлечь корень из отрицательного числа"
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Ошибка: невозможно вычислить факториал отрицательного числа"
    if x == 0:
        return 1
    return x * factorial(x - 1)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

while True:
    try:
        print("\n Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Квадратный корень")
        print("7. Факториал")
        print("8. Синус")
        print("9. Косинус")
        print("10. Тангенс")
        print("0. Выход")
        
        choice = int(input("Введите номер операции: "))
        
        if choice == 0:
            break
        
        if choice in [1, 2, 3, 4, 5]:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        if choice in [6, 7, 8, 9, 10]:
            num1 = float(input("Введите число:"))

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 5:
            result = power(num1, num2)
        elif choice == 6:
            result = square_root(num1)
        elif choice == 7:
            result = factorial(int(num1))
        elif choice == 8:
            result = sine(num1)
        elif choice == 9:
            result = cosine(num1)
        elif choice == 10:
            result = tangent(num1)
        else:
            print("Недопустимый выбор операции")
            continue
        
        print("Результат:", result)
    
    except ValueError:
        print("Ошибка: Введите корректное число")
    except KeyboardInterrupt:
        print("Прервано пользователем")
        break