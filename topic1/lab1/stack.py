from typing import Any


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, elem: Any) -> None:
        """
        Добавление элемента в вершину стека

        :param elem: Элемент, который должен быть добавлен
        """
        self._stack.append(elem)

    def pop(self) -> Any:
        """
        Извлечение элемента из вершины стека.

        :raise: IndexError - Ошибка, если стек пуст

        :return: Извлеченный с вершины стека элемент.
        """
        if not self._stack:
            raise IndexError("Стек пустой, нельзя извлечь элемент")

        return self._stack.pop(-1)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в стеке, без его извлечения.

        :param ind: индекс элемента (отсчет с вершины, 0 - вершина, последний добавленный элемент,
        1 - предпоследний элемент, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ стека

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Индекс должен быть типа int")

        if not 0 <= ind < len(self._stack):
            raise IndexError("Индекс находится вне допустимого диапазона")

        invert_ind = -1 - ind
        return self._stack[invert_ind]

    def clear(self) -> None:
        """ Очистка стека. """
        self._stack.clear()

    def __len__(self) -> int:
        """ Количество элементов в стеке. """
        return len(self._stack)
