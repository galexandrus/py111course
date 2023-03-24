from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком
    O(n**2)
    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # DONE реализовать алгоритм сортировки пузырьком
    sorted_cont = container
    n = len(sorted_cont)
    while n > 1:
        for i in range(n - 1):
            if sorted_cont[i] > sorted_cont[i + 1]:
                sorted_cont[i], sorted_cont[i + 1] = sorted_cont[i + 1], sorted_cont[i]
        n -= 1
    return sorted_cont


if __name__ == '__main__':
    seq = [4, 8, 2, 1, 7, 3, 5, 6]
    sorted_seq = sort(seq)
    print(sorted_seq)
