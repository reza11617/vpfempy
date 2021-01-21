#!/usr/bin/env python3

class element:
    __totalElement = 0

    @classmethod
    def add_total_elemment(cls):
        __totalElement += 1

class beamElement:
    def __init__(node_i, node_j, EI):
        self.nodes = [node_i, node_j]
        self.EI = EI
