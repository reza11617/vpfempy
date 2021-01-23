import numpy as np
from scipy import sparse

from vpfem.utils import tools
from vpfem.geometry import Model,Node

class Element:
    """This class creates element"""
    __total_element = 0

    def __init__(self, nodes):
        self.nodes = nodes
    @classmethod
    def add_total_elemment(cls):
        """This fucntion adds to total number of element"""
        cls.__total_element += 1

    @classmethod
    def get_element_number(self):
        return Element.__total_element

    def load_vector(self):
        load = []
        for node in self.nodes:
            load.extend(node.get_load_vector())
        return np.array(load)

    def get_global_dof(self):
        dofs = []
        for node in self.nodes:
            dofs.extend(node.get_global_dof())
        return dofs

    def get_local_vector(self, vector_global):
        return vector_global[self.get_global_dof()]

class BeamElement(Element):
    """This class created Beam Element"""
    def __init__(self,node_i, node_j, EI):
        self.nodes = [node_i, node_j]
        self.EI = EI
        self.node_size = len(self.nodes)
        self.dof_size = self.node_size * Model.get_number_dof()
        self.length = tools.distance_nodes(node_i, node_j)
        Element.add_total_elemment()
        self.number = Element.get_element_number()

    def stiffness_matrix(self):
        return (2*self.EI/self.length**3) * np.array([[6, 3*self.length, -6, 3*self.length],
                                                [3*self.length, 2*self.length*self.length, -3*self.length, self.length*self.length],
                                                [-6, -3*self.length, 6, -3*self.length],
                                                [3*self.length, self.length*self.length, -3*self.length, 2*self.length*self.length]])
    def get_dof_size(self):
        return self.dof_size
    def __str__(self):
        return "#{num} nodes({ni}, {nj})".format(num=self.number, ni = self.nodes[0].number, nj = self.nodes[1].number)
    def __repr__(self):
        return str(self)
