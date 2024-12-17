import math # підключення бібліотеки

def task1():
    
    A = int(input("Введіть двозначне число: ")) # Вхідні данні

    if 10 <= A <= 99: # Перевірка, на двозначність
        
        desyatki = A // 10 # Знаходження десятків
        odinici = A % 10 # Знаходження одиниць

    # Відповідь
        print("Десятки: ", desyatki)
        print("Одиниці: ", odinici)
    else:
        print("Помилка: число не двозначне")

def task2():

    
    x = float(input("Введіть x : ")) # Вхідні данні
    # Обчислення
    y_top    = 2 * math.tan(x) * math.sin(x) + 1/4 * math.sqrt(abs(1 - math.sin(x)**2 * math.tan(x)))
    y_bottom = (1/4) ** (1 + (x**3) / 3) + 2 * math.log(x**3 , 4)

    y = y_top / y_bottom
    
    # Відповідь
    print("y = ", y)

def task3():

    # Вхідні данні
        A = int(input())
        B = int(input())
        C = int(input())

    # Відповідь
        if (A > 0) or (B > 0) or (C > 0):
            print(True)
        else:
            print(False)
