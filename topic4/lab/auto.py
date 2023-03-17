from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    # DONE решить задачу с помощью динамического программирования

    route_count = [[-1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        route_count[i][0] = 1
    for j in range(1, m):
        route_count[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            route_count[i][j] = route_count[i - 1][j] + route_count[i][j - 1] + route_count[i - 1][j - 1]

    return route_count


if __name__ == '__main__':
    n = 5
    m = 7
    paths = car_paths(n, m)
    for i in range(n):
        print(paths[i])
    print(paths[-1][-1])  # 7
