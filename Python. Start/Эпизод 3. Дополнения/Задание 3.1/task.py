import math
def task_1(text):
    my_dict = {}
    tx = text.split(".")
    tx0 = tx[0].split()
    tx1 = tx[1].split()
    tx2 = tx[2].split()
    my_dict[tx[0]] = len(tx0)
    my_dict[tx[1][1:]] = len(tx1)
    my_dict[tx[2][1:]] = len(tx2)
    return my_dict

def task_2(x1,y1,x2,y2):
    distance_x = x1 - x2
    distance_y = y1 - y2
    distance = math.sqrt(distance_x**2 + distance_y**2)
    return distance