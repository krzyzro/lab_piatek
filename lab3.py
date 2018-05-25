import numpy
import random
import time

tablica = [random.randint(1, 100) for x in range(5000)]
print('Tablica nieposortowana')
print(tablica)




def sortowanie_babel(tablica):
    start = time.time()
    zmiana = True
    while (zmiana == True):
        zmiana = False
        for x in range(0, 4999):
            if (tablica[x] > tablica[x + 1]):
                a = tablica[x]
                b = tablica[x + 1]
                tablica[x] = b
                tablica[x + 1] = a
                zmiana = True
    end = time.time()
    print("time:", end - start)
    return tablica


tablica1 = sortowanie_babel(tablica)
print('Tablica posortowana metoda babelkowa')
print(tablica1)


def sortowanie_przez_wym(tablica):
    start = time.time()
    for y in range(0, 5000):
        min = tablica[y]
        index_min = y
        for x in range(y, 5000):
            if (tablica[x] < min):
                min = tablica[x]
                index_min = x
        pierw = tablica[y]
        tablica[y] = min
        tablica[index_min] = pierw
    end = time.time()
    print("time:", end - start)
    return tablica


tablica2 = sortowanie_przez_wym(tablica)
print('Tablica posortowana metoda przez wymiane')
print(tablica2)


def quicksort(tablica):
    start = time.time()

    quick_sortowanie(tablica, 0, len(tablica) - 1)
    
    end = time.time()
    print("time:", end - start)


def quick_sortowanie(tablica, min, max):
    if min < max:
        p = podzial(tablica, min, max)
        quick_sortowanie(tablica, min, p - 1)
        quick_sortowanie(tablica, p + 1, max)


def pivot_indeks(tablica, min, max):
    mid = (max + min) // 2
    pivot = max
    if tablica[min] < tablica[mid]:
        if tablica[mid] < tablica[max]:
            pivot = mid
    elif tablica[min] < tablica[max]:
        pivot = min

    return pivot


def podzial(tablica, min, max):
    pivotIndex = pivot_indeks(tablica, min, max)
    pivotValue = tablica[pivotIndex]
    tablica[pivotIndex], tablica[min] = tablica[min], tablica[pivotIndex]
    border = min

    for i in range(min, max + 1):
        if tablica[i] < pivotValue:
            border += 1
            tablica[i], tablica[border] = tablica[border], tablica[i]
            tablica[min], tablica[border] = tablica[border], tablica[min]
    return border

quicksort(tablica)
print('Tablica posortowana metoda przez quicksort')
print(tablica)
