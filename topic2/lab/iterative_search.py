"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    # DONE реализовать итеративный линейный поиск
    if not arr:
        raise ValueError("Нельзя искать в пустом массиве")

    min_val = arr[0]
    min_ind = 0
    for i in range(0, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_ind = i

    return min_ind


if __name__ == '__main__':
    # print(min_search([]))
    print(min_search([3, 7, 1, 9, 2, 7, 1, 10]))

    # seq1 = [i for i in range(3, 10)] + [1]
    # print(seq1)
    # print(min_search(seq1))
    # print(seq1.index(min(seq1)))
    #
    # seq2 = [i for i in range(10, -3, -1)]
    # print(seq2)
    # print(min_search(seq2))
    # print(seq2.index(min(seq2)))
