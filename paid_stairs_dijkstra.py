from typing import Hashable, Union
import matplotlib.pyplot as plt
import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # DONE c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы

    starting_vertex = 0

    # Решение с помощью функции из модуля networkx
    # check = nx.dijkstra_predecessor_and_distance(graph, starting_vertex)[1][max(graph.nodes.keys())]

    # Самостоятельное решение
    cost_dict = {vertex: float("inf") for vertex in graph}
    starting_vertex_cost = 0
    cost_dict[starting_vertex] = starting_vertex_cost

    visited = []
    to_visit_dict = {starting_vertex: starting_vertex_cost}

    while to_visit_dict:
        current_vertex = min(to_visit_dict, key=to_visit_dict.get)
        to_visit_dict.pop(current_vertex)
        visited.append(current_vertex)
        neighbours = graph.neighbors(current_vertex)
        current_cost = cost_dict[current_vertex]
        for neighbour in neighbours:
            neighbour_cost = graph.get_edge_data(current_vertex, neighbour)["weight"] + current_cost
            if cost_dict[neighbour] > neighbour_cost:
                cost_dict[neighbour] = neighbour_cost
            if neighbour not in visited:
                if neighbour not in to_visit_dict \
                        or to_visit_dict[neighbour] > neighbour_cost:
                    to_visit_dict[neighbour] = neighbour_cost

    answer = cost_dict.pop(max(graph.nodes.keys()))

    return answer


if __name__ == '__main__':
    stairway_price = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    # DONE записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней

    def graf_creator(weights: tuple):
        graph = nx.DiGraph()
        graph.add_node(0, weight=0)
        for i in range(len(weights)):
            graph.add_node(i + 1, weight=weights[i])
        for i in range(len(weights)):
            first_price = graph.nodes.get(i + 1)['weight']
            graph.add_edge(i, i + 1, weight=first_price)
            if i < len(weights) - 1:
                second_price = graph.nodes.get(i + 2)['weight']
                graph.add_edge(i, i + 2, weight=second_price)
        return graph

    stairway_graph = graf_creator(stairway_price)

    print(stairway_path(stairway_graph))  # 72
    # nx.draw(stairway_graph, with_labels=True)
    # plt.savefig("my_graph_02.png")
