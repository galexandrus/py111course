from stack import Stack


def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    # DONE реализовать проверку скобочной группы
    brackets_stack = Stack()
    for sign in brackets_row:
        if sign == "(":
            brackets_stack.push(sign)
        elif sign == ")":
            try:
                brackets_stack.pop()
            except IndexError:
                return False

    if brackets_stack:
        return False

    return True

    # Альтернативный вариант решения
    # total = 0
    # for sign in brackets_row:
    #     if sign == "(":
    #         total += 1
    #     elif sign == ")":
    #         total -= 1
    #
    #     if total < 0:
    #         return False
    #
    # if total != 0:
    #     return False
    #
    # return True


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
