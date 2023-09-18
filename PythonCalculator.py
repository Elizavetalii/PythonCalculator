import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "������: ������� �� ����"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "������: ���������� ������� ������ �� �������������� �����"
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "������: ���������� ��������� ��������� �������������� �����"
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
        print("\n �������� ��������:")
        print("1. ��������")
        print("2. ���������")
        print("3. ���������")
        print("4. �������")
        print("5. ���������� � �������")
        print("6. ���������� ������")
        print("7. ���������")
        print("8. �����")
        print("9. �������")
        print("10. �������")
        print("0. �����")
        
        choice = int(input("������� ����� ��������: "))
        
        if choice == 0:
            break
        
        if choice in [1, 2, 3, 4, 5]:
            num1 = float(input("������� ������ �����: "))
            num2 = float(input("������� ������ �����: "))
        if choice in [6, 7, 8, 9, 10]:
            num1 = float(input("������� �����:"))

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
            print("������������ ����� ��������")
            continue
        
        print("���������:", result)
    
    except ValueError:
        print("������: ������� ���������� �����")
    except KeyboardInterrupt:
        print("�������� �������������")
        break
