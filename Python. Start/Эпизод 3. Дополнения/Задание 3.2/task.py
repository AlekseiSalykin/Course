def task_1(group_list, variable):
    start = 0
    end = len(group_list)
    while start <= end:
        i = (start + end)//2
        if group_list[i] == variable:
            return str(i)
        if variable < group_list[i]:
            end = i - 1
        else:
            start = i + 1
        return -1

def task_2(var):
    start = 1
    while start <= var:
        if var % start == 0:
            check = True
        else:
            check = False
        start += 1
    return check