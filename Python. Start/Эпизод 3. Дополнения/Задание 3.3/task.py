def task_1(list):
    count_max = max(list, key=list.count)
    return count_max

def task_2(x, y):
    n = 8
    for i in range(n):
        new_x, new_y = i, i
        x.append(new_x)
        y.append(new_y)
    correct = True
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        a = "NO"
    else:
        a = "YES"

    return a

def task_3(x, y, xc, yc, r):
    if (x - xc) ** 2 + (y - yc) ** 2 <= r * r:
        correct = True
    else:
        correct = False
    return correct

def task_4(list_var):
    count = 0
    i = 0
    while i < len(list_var):
        if list_var[i-1] >= list_var[i-2] + list_var[i]:
            count += 1
        i += 1
    return count

def task_5(key):
    f = open('file.txt', 'r')
    my_list = []
    a = ""
    stroka1 = ""
    stroka2 = ""
    stroka3 = ""
    for i in f:
        a += i
    a = a.lower()
    a = a.split('\n')
    for c in a[0]:
        if c.isupper():  # проверить, является ли символ прописным
            c_index = ord(c) - ord('A')
            # сдвиг текущего символа на позицию key
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            stroka1 += c_new
        elif c.islower():  # проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            stroka1 += c_new
        elif c.isdigit():
            # если это число, сдвинуть его фактическое значение
            c_new = (int(c) + key) % 10
            stroka1 += str(c_new)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            stroka1 += "b"
    for c in a[1]:
        if c.isupper():  # проверить, является ли символ прописным
            c_index = ord(c) - ord('A')
            # сдвиг текущего символа на позицию key
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            stroka2 += c_new
        elif c.islower():  # проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            stroka2 += c_new
        elif c.isdigit():
            # если это число, сдвинуть его фактическое значение
            c_new = (int(c) + key) % 10
            stroka2 += str(c_new)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            stroka2 += "b"
    for c in a[2]:
        if c.isupper():  # проверить, является ли символ прописным
            c_index = ord(c) - ord('A')
            # сдвиг текущего символа на позицию key
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            stroka3 += c_new
        elif c.islower():  # проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            stroka3 += c_new
        elif c.isdigit():
            # если это число, сдвинуть его фактическое значение
            c_new = (int(c) + key) % 10
            stroka3 += str(c_new)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            stroka3 += "b"
    my_list.append(stroka1)
    my_list.append(stroka2)
    my_list.append(stroka3)
    return my_list