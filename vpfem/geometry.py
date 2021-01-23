import numpy as np
from vpfem.utils import tools

class Model:
    """This class creates the model."""
    __number_dof = 0
    __number_dim = 0

    @classmethod
    def model_builder(cls, number_dof, number_dim):
        """This function defined number number_dof and number_dim."""
        cls.__number_dof = tools.int_type_checker(number_dof)
        cls.__number_dim = tools.int_type_checker(number_dim)

    @classmethod
    def get_number_dof(cls):
        """This funciton returns the number_dof in the FE analysis"""
        return cls.__number_dof
    @classmethod
    def get_number_dim(cls):
        """This funtion returns the number_dim if the FE analysis"""
        return cls.__number_dim


class Node:
    """This class creates node in the FE model."""
    __total_node = -1
    __fix_dofs = []

    def __init__(self, *coordinate, **mass):
        self.dim = tools.dimension_checker(coordinate, Model.get_number_dim())
        self.coordinate = coordinate
        self.mass = mass
        self.generate_node_number()
        self.boundary_condition = []
        self.point_load_list = []

    def generate_node_number(self):
        """This function generate the node number"""
        Node.__total_node += 1
        self.number = Node.__total_node

    def fix(self, *dofs):
        """This function generate list of fixed dofs"""
        self.boundary_condition = tools.check_size(dofs,
                                                   Model.get_number_dof())
        dof_counter = -1
        for i in dofs:
            dof_counter += 1
            if i:
                Node.__fix_dofs.append(self.number*Model.get_number_dof() + dof_counter)

    def point_load(self, *pointLoads):
        """This function create point load on the DOFs of this node"""
        self.point_load_list = tools.check_size(pointLoads,
                                           Model.get_number_dof())

    def get_load_vector(self):
        if self.point_load_list:
            return self.point_load_list
        else:
            return [0] * Model.get_number_dof()

    def get_global_dof(self):
        start_dof = self.number*Model.get_number_dof()
        stop_dof = start_dof + Model.get_number_dof()
        return [i for i in range(start_dof, stop_dof, 1)]

    @classmethod
    def get_fix_dofs(cls):
        """This function returns fixed dofs"""
        return cls.__fix_dofs
    @classmethod
    def get_total_node(cls):
        return cls.__total_node
    def get_dim(self):
        """This function returns the dimention of the node"""
        return self.dim

    def __str__(self):
        return "#{num} co={coordinate}".format(num = self.number, coordinate = self.coordinate)

    def __repr__(self):
        return str(self)
