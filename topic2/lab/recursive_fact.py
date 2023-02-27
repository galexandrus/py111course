def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # DONE реализовать рекурсивный алгоритм нахождения факториала
    if not isinstance(n, int):
        raise TypeError("n должно быть типа int")

    if n < 0:
        raise ValueError("Факториал можно вычислить от неотрицательного числа")
    elif n == 0:
        return 1
    else:
        factorial = factorial_recursive(n - 1) * n

    return factorial


if __name__ == '__main__':
    print(factorial_recursive(0))
    print(factorial_recursive(1))
    print(factorial_recursive(2))
    print(factorial_recursive(3))
    print(factorial_recursive(4))
    print(factorial_recursive(5))
    print(factorial_recursive(6))
    print(factorial_recursive(7))
    print(factorial_recursive(8))
