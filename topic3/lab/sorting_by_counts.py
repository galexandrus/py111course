from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами
    O(n**2) при создании списка ключей путём сортировки существующих значений и отбрасывая дубли.
    O(n) при создании списка ключей по диапазону.

    1. Определите максимальное значение в массиве и заполните вспомогательный массив
    с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    # DONE реализовать алгоритм сортировки подсчетами

    if not container:
        return []

    # Создание сортированного списка ключей - медленне, но требует меньше памяти
    # keys = [container[0]]
    # for value in container:
    #     for j in range(len(keys)):
    #         if value < keys[j]:
    #             keys.insert(j, value)
    #             break
    #     if value > keys[-1]:
    #         keys.append(value)

    # Создание списка ключей по диапазону - быстрее, но требует больше памяти
    min_val = container[0]
    max_val = container[-1]
    for value in container:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
    keys = [i for i in range(min_val, max_val + 1)]

    count_dict = {key: 0 for key in keys}
    for value in container:
        count_dict[value] += 1
    sorted_seq = []
    for key in count_dict:
        while count_dict[key] > 0:
            sorted_seq.append(key)
            count_dict[key] -= 1
        if count_dict[key] == 0:
            continue

    return sorted_seq


if __name__ == '__main__':
    seq = [15, 3, 4, 1, -2, 2, 9, -8, 12]
    print(sort(seq))
    print(seq)
