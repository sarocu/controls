from scipy import signal

class ContinuousLTI:
    """
    Initiates a continuous, linear, time-invariant state space model. 
    """
    def __init__(self, A=None, B=None, C=None, D=None, dt=None):
        self.system = signal.StateSpace(A, B, C, D, dt=dt)


    def eval(self):
        return self.system.zeros