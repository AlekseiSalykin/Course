# todo: replace this with an actual task
def task_1(str):
    # TODO
    count = 0
    for i in str:
        if i != " ":
            count += 1
        else:
            count = 0
    return count


def task_2(str):
    # TODO
    x = str.split(' ')
    stroka = x[1] + " " + x[0] + " " + x[3] + " " + x[2] + " " + x[5] + " " + x[4] + " " + x[6]
    return stroka


def task_3(str):
    # TODO
    count = 0
    for i in range(len(str)):
        if str[i-1].find(" ") and str[i] == (str[i - 2]):
            count += 1

    return count
