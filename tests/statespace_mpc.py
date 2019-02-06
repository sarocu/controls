from superplus import workspace
from superplus.statespace import model
import numpy

ws = workspace.Workspace(timestep=0.2)
a = numpy.array([[1, 1, 1]])
b = numpy.array([[1, 0.5, 1]])
c = numpy.array([[1, 1]])
d = numpy.array([[0.7, 0.5, 1]])

model = model.ContinuousLTI(a, b, c, d, 0.2)
print(model.eval())