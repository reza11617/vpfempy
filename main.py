from vpfem.geometry import model, node

# params
L = 1.0
EI = 1.0
numElement = 2

# Build the model
# model.modelbuilder(nDof, nDim)
model.modelbuilder(2,1)

# create nodes
# node(tag, x)
nodes = []
for i in range(numElement+1):
    nodes.append(node(i*L/numElement))

# define boundary condition
# nodeObj.fix(dof_i, dof_j, dof_k, ...)
nodes[0].fix(1,1)

# define point load
# nodeObj.pointLoad(dof_i, dof_j, ...)
nodes[2].pointLoad(1,0)

# define Element
#


# Analyze
#


print(nodes)
