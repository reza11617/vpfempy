from vpfem.geometry import Model, Node
from vpfem.element import BeamElement
from vpfem.analyze import run
# params
L = 1.0
EI = 1.0
NUM_ELE = 2

# Build the model
# model.modelbuilder(nDof, nDim)
Model.model_builder(2,1)

# create nodes
# node(tag, x)
nodes = []
for i in range(NUM_ELE+1):
    nodes.append(Node(i*L/NUM_ELE))

# define boundary condition
# nodeObj.fix(dof_i, dof_j, dof_k, ...)
nodes[0].fix(1,1)

# define point load
# nodeObj.pointLoad(dof_i, dof_j, ...)
nodes[len(nodes)-1].point_load(10,0)

# define Element
# BeamElement(NodeObj_i, NodeObj_j, EI)
elements = []
for i in range(NUM_ELE):
    elements.append(BeamElement(nodes[i], nodes[i+1], EI))

print(nodes)
print(elements)

# Analyze
# Analyze.run(elements)
run(elements, 0.0001)
