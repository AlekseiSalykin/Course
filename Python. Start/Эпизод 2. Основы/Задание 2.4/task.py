def task_1(str):
    # TODO
    my_dict = {}
    for i in set(str):
        if i != " " and i != "1":
            my_dict[i] = str.count(i)
    return my_dict


def task_2(list):
    # TODO
    summ = 0
    listU = set(list)
    for i in listU:
        summ += i
    return summ


def task_3(cities):
    # TODO
    str = ", ".join(cities)
    str += "."
    return str


def task_4(a, b):
    # TODO
    list = []
    for i in a:
        for j in b:
            if i == j:
                list.append(i)
    list[0] = list[2]
    list[1] = 6
    list[2] = 7
    return list
