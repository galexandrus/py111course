"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        DONE Описать, где начало и конец очереди
        Начало очереди - элемент с индексом 0 списка
        Конец очереди - последний элемент списка (индекс -1)
        """
        # DONE инициализировать список
        self.queue = []

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        # DONE реализовать метод enqueue
        self.queue.append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        # DONE реализовать метод dequeue
        if len(self.queue) == 0:
            raise IndexError("Очередь пуста")

        return self.queue.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди,
        1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        # DONE реализовать метод peek
        if not isinstance(ind, int):
            raise TypeError("Индекс должен быть типа int")

        if ind < 0 or ind >= len(self.queue):
            raise IndexError("Индекс вне границ очереди")

        return self.queue[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        # DONE реализовать метод clear
        self.queue.clear()

    def __len__(self) -> int:
        """ Количество элементов в очереди. """
        # DONE реализовать метод __len__
        return len(self.queue)
