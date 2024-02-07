#!/usr/local/bin/python3
#
# graph.py
# chapter-4
#
# Created by Illya Starikov on 07/24/19.
# Copyright 2019. Illya Starikov. MIT License.
#


class Graph:
    def __init__(self):
        # hash table to store nodes
        self._graph = {}

    def add_vertex(self, vertex):
        self._graph[vertex] = set()

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 not in self._graph.keys():
            self.add_vertex(vertex_1)

        self._graph[vertex_1].add(vertex_2)

