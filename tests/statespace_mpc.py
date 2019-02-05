from superplus import workspace
from superplus.statespace import model
import numpy

ws = workspace.Workspace(timestep=0.2)
a = numpy.array([[0, 1], [0, 0]])
b = numpy.array([[0], [1]])
c = numpy.array([[1, 0]])
d = numpy.array([[0]])

model = model.ContinuousLTI(a, b, c, d, 0.2)
