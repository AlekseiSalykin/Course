def task_1(N):
    # TODO
    for i in range(1, N, 1):
        N = N * i
    return N


def task_2(N):
    # TODO
    f1 = 1
    f2 = 1
    for i in range(2, N):
        f1, f2 = f2, f1 + f2
    return f1


def task_3(N):
    # TODO
    num_list = []
    for i in range(1, N+1):
        if N % i == 0:
            num_list.append(i)
    return num_list
