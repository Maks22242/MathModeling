import numpy as np
from matplotlib import pyplot as plt
import math
import numpy
# Входные параметры
e = 0.0001  # Точность
#y = [1.0, 1.5, 3.0, 4.5, 7.0, 8.5]
y = [0.5, 4.0, 6.9, 8.8, 10.9, 12.1]
x = [1, 2, 3, 4, 5, 6]

def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

# Линейная функция
def lin_func(x,y):
    n = len(x)
    xy = []  # Массив содержащий произведение элементов массивов x и y
    x2 = []  # Массив содержащий еементы массива x возведённые в квадрат
    for i in range(n):
        el = x[i]*y[i]
        xy.append(el)
    for i in range(n):
        el = x[i]*x[i]
        x2.append(el)

    a = (n * sum(xy) - sum(x)*sum(y))/(n * sum(x2)-sum(x)*sum(x))
    b = (1/n) * sum(y)-a*(1/n)*sum(x)
    a = round(a, 2)
    b = round(b, 2)
    print('Коофициенты линейной фенуции:\n a = ',a," b = ",b )
    new_y = []
    for i in range(n):
        el = a*x[i]+b
        new_y.append(el)
    return new_y

# Степенная функция
def pow_func(x,y):
    n = len(x)
    X = []
    Y = []
    for i in range(n):
        el_x = math.log(x[i])
        el_y = math.log(y[i])
        X.append(el_x)
        Y.append(el_y)
    xy = []  # Массив содержащий произведение элементов массивов x и y
    x2 = []  # Массив содержащий еементы массива x возведённые в квадрат
    for i in range(n):
        el = X[i]*Y[i]
        xy.append(el)
    for i in range(n):
        el = X[i]*X[i]
        x2.append(el)

    a = (n * sum(xy) - sum(X)*sum(Y))/(n * sum(x2)-sum(X)*sum(X))
    b = (1/n) * sum(Y)-a*(1/n)*sum(X)
    b = math.pow(math.e,b)
    a = round(a,2)
    b = round(b,2)
    print('Коофициенты линейной фенуции:\n a = ', a, " b = ", b)
    new_y = []
    for i in range(n):
        pow_x = math.pow(x[i],a)
        el = b*pow_x
        new_y.append(el)
    return new_y

# Показательная функция
def exp_func(x,y):
    n = len(x)
    Y = []
    for i in range(n):
        el_y = math.log(y[i])
        Y.append(el_y)
    xy = []  # Массив содержащий произведение элементов массивов x и y
    x2 = []  # Массив содержащий еементы массива x возведённые в квадрат
    for i in range(n):
        el = x[i]*Y[i]
        xy.append(el)
    for i in range(n):
        el = x[i]*x[i]
        x2.append(el)

    a = (n * sum(xy) - sum(x)*sum(Y))/(n * sum(x2)-sum(x)*sum(x))
    b = (1/n) * sum(Y)-a*(1/n)*sum(x)
    b = math.pow(math.e, b)
    a = round(a, 2)
    b = round(b, 2)
    print('Коофициенты показательной фенуции:\n a = ', a, " b = ", b)
    new_y = []
    for i in range(n):
        pow_x = math.pow(math.e, a*x[i])
        el = b*pow_x
        new_y.append(el)
    return new_y

def qoud_func(x,y):
    n = len(x)
    xy, x2y = [], []  # Массив содержащий произведение элементов массивов x и y
    x2, x3, x4 = [], [], []

    for i in range(n):
        el = x[i] * y[i]
        xy.append(el)
        el = x[i] * x[i]
        x2.append(el)
        el = x[i] * x[i] * x[i]
        x3.append(el)
        el = x[i] * x[i] * x[i] * x[i]
        x4.append(el)
        el = x[i] * y[i] * x[i]
        x2y.append(el)
    arr1 = [sum(x4), sum(x3), sum(x2)]
    arr2 = [sum(x3), sum(x2), sum(x)]
    arr3 = [sum(x2), sum(x), n]
    vec1 = [sum(x2y), sum(xy), sum(y)]
    M3 = numpy.array([arr1, arr2, arr3])
    v3 = numpy.array(vec1)
    res = numpy.linalg.solve(M3, v3)
    np.round(res, 2)
    a = round(res[0], 2)
    b = round(res[1], 2)
    c = round(res[2], 2)

    print('Коофициенты квадратичной функции фенуции:\n a = ', a, " b = ", b, " с = ", c)

    new_y = []
    for i in range(n):
        el = res[0]*x2[i]+res[1]*x[i]+res[2]
        new_y.append(el)
    return new_y

def del_y(arr_y, arr_func_y):
    err_rate = 0
    for i in range(len(arr_y)):
        err_rate += math.pow((arr_y[i]-arr_func_y[i]), 2)
    return round(err_rate,2)

#Ключ по значению
def get_key(map, value):
    for k, v in map.items():
        if v == value:
            return k

def comp_res(arr_y,y1,y2,y3,y4):
    map_res = {'lin':del_y(arr_y,y1),'pow':del_y(arr_y,y2),'exp':del_y(arr_y,y3),'qoud':del_y(arr_y,y4),}
    min_res = min(map_res.values())
    print('Точность: ')
    print(map_res)
    bet_key = get_key(map_res,min_res)
    if(bet_key == 'lin'):
        return 'Линейная функция'
    elif (bet_key == 'pow'):
        return 'Степенная функция'
    elif (bet_key == 'exp'):
        return 'Показательная функция'
    elif (bet_key == 'qoud'):
        return 'Квадратичная функция'

def draw():
    y1 = lin_func(x,y)
    y2 = pow_func(x,y)
    y3 = exp_func(x,y)
    y4 = qoud_func(x,y)
    fig, ax = plt.subplots()
    res = 'Лучшая - ' + comp_res(y, y1, y2, y3, y4)
    plt.grid()  # Строим сетку

    ax.plot(x, y,'p')
    ax.plot(x, y1, 'y', label='Линейная ф.',color = 'y')
    #plt.text(x[5],y1[5],'Линейная ф.')
    ax.plot(x, y2, 'g', label='Степенная ф.')
    #plt.text(x[5],y2[5],'Степенная ф.')
    ax.plot(x, y3, 'r', label='Показат. ф.')
    #plt.text(x[5],y3[5],'Показат. ф.')
    ax.plot(x, y4, 'grey', label='Квадрат. ф.')
    #plt.text(x[5], y4[5],'Квадрат. ф.')

    ax.legend()

    plt.title(res)
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()

draw()