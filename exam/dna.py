"""
Задача консенсуса DNA ридов
При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
Т.е. для строк
ATTA
ACTA
AGCA
ACAA
консенсус-строка будет ACTA
(в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т, в четвертой – снова А).
Для входного списка из N строк одинаковой длины построить консенсус-строку
"""


def dna_func(dna_list: list) -> str:
    str_len = len(list(dna_list[0]))
    symbols_list = [[] for _ in range(str_len)]
    for dna_str in dna_list:
        for j in range(str_len):
            symbols_list[j].append(dna_str[j])

    consensus_list = []

    for one_symbol_list in symbols_list:
        one_symbol_dict = {}
        for symbol in one_symbol_list:
            if symbol not in one_symbol_dict:
                one_symbol_dict[symbol] = 1
            else:
                one_symbol_dict[symbol] += 1

        consensus_list.append(max(one_symbol_dict, key=one_symbol_dict.get))

    return "".join(consensus_list)


if __name__ == '__main__':
    dna1 = [
        'ATTA',
        'ACTA',
        'AGCA',
        'ACAA',
        'CGCT',
        'CGCT',
    ]
    print(dna1)
    print(dna_func(dna1))
