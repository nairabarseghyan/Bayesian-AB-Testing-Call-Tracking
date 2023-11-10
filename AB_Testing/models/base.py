class Bandit(ABC):
    
    """
    Abstract base class for bandit algorithms.

    Methods:
    - __init__(self, true_mean): Initialize the bandit with a true mean value.
    - __repr__(self): Provide a string representation of the bandit.
    - pull(self): Simulate pulling an arm of the bandit.
    - update(self, x): Update the bandit based on an observed reward.
    - experiment(self): Conduct an experiment with the bandit.
    - report(self): Report results, such as storing data and printing statistics.

    Attributes:
    - true_mean: The true mean value of the bandit.
    """

    @abstractmethod
    def __init__(self, true_mean):
        self.true_mean = true_mean

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def pull(self):
        pass
    
    @abstractmethod
    def update(self, x):
        pass
        
        
    @abstractmethod
    def experiment(self):
        pass

    @abstractmethod
    def report(self):
        # store data in csv
        # print average reward (use f strings to make it informative)
        # print average regret (use f strings to make it informative)
        pass
    

#--------------------------------------#