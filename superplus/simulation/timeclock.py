

class Timeclock:
    """
    Timeclock is the central point of control for the simulation
    """

    def __init__(self, workspace):
        # TODO check that the workspace is the right object:
        self.workspace = workspace
        self.states = {}


    def configure(self, timestep=1, min_time=0, max_time=1000):
        # Setting global simulation params:
        # TODO: assert that these are floats
        # TODO: assert that timestep is positive
        self.timestep = timestep
        self.min_time = min_time
        self.max_time = max_time
        self.now = min_time
        

    def run(self, initial_conditions):
        # run the simulation, starting by ticking the timeclick
        pass


    def tick(self):
        # Increment the simulation one time step    
        self.now = self.min_time + self.timestep

        # call the workspace to run all components in order and update the states:
        self.states = self.workspace.execute(self.states)