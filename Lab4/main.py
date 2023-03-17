import matplotlib.pyplot as plt
import numpy as np

def len_numb(n):
    leng = 0
    while(n!=0):
        leng += 1
        n //= 10
    return leng

def squreNumbIn(numb, leng):
        iter = 1
        newNumb = 0
        st = 0
        while iter != leng*2:
            if iter <= leng/2:
                iter += 1
                numb //= 10
            elif iter > leng/2 and iter <= (leng + leng/2):
                newNumb = newNumb + (numb%10) * pow(10, st)
                st+=1
                numb //= 10
                iter += 1
            else:
                break
        return newNumb

def squreMethod(numb, leng_n):
    arr_el = [0,1]
    iter = 1
    # Переменная отвечает за то, чтобы числа не повторялись
    cond = 1
    while iter != 1000 and cond != 0:
        numb2 = pow(numb,2)
        newNumb = squreNumbIn(numb2, leng_n)
        if iter != 1:
            if (newNumb/(pow(10,leng_n))) in arr_el:
                cond = 0
                break
        arr_el.append(newNumb/(pow(10,leng_n)))
        iter += 1
        numb = newNumb
    return arr_el

def cump_NumbIn(numb, leng):
    iter = 1
    nextRandNumb = 0
    nextNumb = 0
    st = 0
    while iter != leng * 2:
        if iter <= leng:
            nextNumb = nextNumb + (numb % 10) * pow(10, iter-1)
        if iter <= leng / 2:
            iter += 1
            numb //= 10
        elif iter > leng / 2 and iter <= (leng + leng / 2):
            nextRandNumb = nextRandNumb + (numb % 10) * pow(10, st)
            st += 1
            numb //= 10
            iter += 1
        else:
            break
    return nextNumb,nextRandNumb

def cumpMethod(numb, leng_n, core):
    arr_el = []
    iter = 1
    # Переменная отвечает за то, чтобы числа не повторялись
    cond = 1
    while iter != 1000 and cond != 0 :
        numb2 = numb*core
        newNumb, newRandNumb = cump_NumbIn(numb2, leng_n)
        if iter != 1:
            if (newRandNumb/(pow(10,leng_n))) in arr_el:
                cond = 0
        arr_el.append(newRandNumb/(pow(10,leng_n)))
        iter += 1
        numb = newNumb
    return arr_el

def KongMethod(numb,leng_n,mult, div):
    arr_el = [0,1]
    iter = 1
    # Переменная отвечает за то, чтобы числа не повторялись
    cond = 1
    while iter != 1000 and cond != 0:
        numb2 = numb * mult
        newNumb = numb2 % div
        if iter != 1:
            if (newNumb / (pow(10, leng_n))) in arr_el:
                cond = 0
        arr_el.append(newNumb / (pow(10, leng_n)))
        iter += 1
        numb = newNumb
    return arr_el

def drawGist (arr,title):


    plt.title(title)
    n, bin, patches = plt.hist(arr, bins = 10)
    plt.show()

def generators():
    print("Введите n-разрядное число и ядро для 2-го метода ")
    #numb = int(input())
    numb = 3172
    core = 5167
    leng = len_numb(numb)
    arr_numb1 = squreMethod(numb, leng)
    print("Полученные случайные числа  методом квадратов:", arr_numb1)
    arr_numb2 = cumpMethod(numb, leng, core)
    print("Полученные случайные числа  методом произведений:", arr_numb2)
    print("Введите множитель и делитель для 3 - го метода ")
    mult = 1357
    div = 5689
    arr_numb3 = KongMethod(numb,leng,mult,div)
    print("Полученные случайные числа Конгруэнтный метод :", arr_numb3)
    drawGist(arr_numb1,"Метод квадратов")
    drawGist(arr_numb2,"Метод произведений")
    drawGist(arr_numb3,"Конгруэнтный метод")

generators()

