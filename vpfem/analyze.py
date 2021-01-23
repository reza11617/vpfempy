import numpy as np
from scipy import sparse
from vpfem.geometry import Model,Node

def precondition_unit(total_dofs):
    return np.ones(total_dofs)


class Analyze:
    def __init__(self, elements):
        print ("Analyze started")

def run(elements, tol):
    total_dofs = Model.get_number_dof() * (Node.get_total_node() + 1)
    U0 = precondition_unit(total_dofs)
    U0[Node.get_fix_dofs()] = 0
    diff = 1
    #R0 = sparse.csr_matrixR0 = sparse.coo_matrix((np.zeros(total_dofs))
    R0 = sparse.coo_matrix((np.array([0]),(np.array([0]),np.array([0]))), shape=(1,total_dofs))
    Q0 = sparse.coo_matrix((np.array([0]),(np.array([0]),np.array([0]))), shape=(1,total_dofs))
    for ele in elements:
        temp = ele.load_vector() - ele.stiffness_matrix() @ ele.get_local_vector(U0)
        R0 += sparse.coo_matrix((temp, (np.zeros(ele.get_dof_size()), np.array(ele.get_global_dof()))), shape=(1,total_dofs))
    R0 = R0.toarray()[0]
    R0[Node.get_fix_dofs()] = 0
    P0 = R0

    while diff > tol:
        Q0 = sparse.coo_matrix((np.array([0]),(np.array([0]),np.array([0]))), shape=(1,total_dofs))
        for ele in elements:
            temp = ele.stiffness_matrix() @ ele.get_local_vector(P0)
            Q0 += sparse.coo_matrix((temp, (np.zeros(ele.get_dof_size()), np.array(ele.get_global_dof()))), shape=(1,total_dofs))
        Q0 = Q0.toarray()[0]
        Q0[Node.get_fix_dofs()] = 0
        print(Q0)
        alpha0 = (np.transpose(R0) @ R0)/(np.transpose(P0) @ Q0)
        U1 = U0 + alpha0 * P0
        R1 = R0 - alpha0 * Q0
        betha0 = (np.transpose(R1) @ R1)/(np.transpose(R0) @ R0)
        P1 = R1 + betha0 * P0
        P0 = P1
        R0 = R1
        diff = abs(max(U1 - U0))
        U0 = U1
    print(U1)
