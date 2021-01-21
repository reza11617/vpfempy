#!/usr/bin/env python3
from vpfem.utils import tools

class model:
    __nDof = 0
    __nDim = 0

    @classmethod
    def modelbuilder(cls, nDof, nDim):
        cls.__nDof = tools.int_type_checker(nDof)
        cls.__nDim = tools.int_type_checker(nDim)

    @classmethod
    def get_nDof(cls):
        return cls.__nDof
    @classmethod
    def get_nDim(cls):
        return cls.__nDim


class node:
    __totalNode = -1
    __fixedDofs = []

    def __init__(self, *coordinate, **masss):
        self.dim = tools.dimension_checker(coordinate, model.get_nDim())
        self.coordinate = coordinate
        self.generate_node_number()

    def generate_node_number(self):
        node.__totalNode += 1
        self.number = node.__totalNode

    def fix(self, *dofs):
        self.bc = tools.check_size(dofs, model.get_nDof()) # Boundary condition

    def pointLoad(self, *pointLoads):
        self.pointLoads = tools.check_size(pointLoads, model.get_nDof())

    @classmethod
    def get_fixedDofs(cls):
        return cls.__fixedDofs

    def __str__(self):
        return "#{num} co={coordinate}".format(num = self.number, coordinate = self.coordinate)

    def __repr__(self):
        return str(self)
