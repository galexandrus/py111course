def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # DONE реализовать итеративный алгоритм нахождения факториала
    if not isinstance(n, int):
        raise TypeError("n должно быть типа int")

    if n < 0:
        raise ValueError("Факториал можно вычислить от неотрицательного числа")
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i

    return factorial


if __name__ == '__main__':
    print(factorial_iterative(0))
    print(factorial_iterative(1))
    print(factorial_iterative(2))
    print(factorial_iterative(3))
    print(factorial_iterative(4))
    print(factorial_iterative(5))
    print(factorial_iterative(6))
    print(factorial_iterative(7))
    print(factorial_iterative(8))
