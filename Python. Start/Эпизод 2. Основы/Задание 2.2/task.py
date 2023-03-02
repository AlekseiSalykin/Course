
import statistics
# Пример 1
def task_1(A):
    # TODO
    sum = 0
    for i in A:
        if i > 0:
            sum += i
    return sum


# Пример 2
def task_2(A):
    # TODO
    sum = 0
    for i in A:
        sum += i
    medium_arithmetik = sum / len(A)
    return medium_arithmetik


# Пример 3
def task_3(A):
    # TODO
    deviation = statistics.pstdev(A)
    return deviation
