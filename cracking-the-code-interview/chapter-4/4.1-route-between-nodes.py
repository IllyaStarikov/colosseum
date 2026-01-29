#!/usr/local/bin/python3
#
# 4.1-route-between-nodes.py
# chapter-4
#
# Created by Illya Starikov on 07/24/19.
# Copyright 2019. Illya Starikov. MIT License.
#


from graph import Graph


class RoutingGraph(Graph):
    def __init__(self):
        super().__init__()

    def __find(self, goal, current_vertex):
        if current_vertex == goal:
            return True

        if current_vertex not in self._graph.keys():
            return False

        for neighbor in self._graph[current_vertex]:
            if self.__find(goal, neighbor):
                return True

        return False

    def find(self, start, goal):
        return self.__find(goal, start)


graph = RoutingGraph()

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(3, 4)
graph.add_edge(2, 4)
graph.add_edge(4, 5)
graph.add_vertex(6)

assert(graph.find(0, 1))
assert(graph.find(0, 2))
assert(graph.find(0, 4))
assert(not graph.find(0, 6))
