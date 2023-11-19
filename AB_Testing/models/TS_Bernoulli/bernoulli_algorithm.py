from AB_Testing.models.base import Bandit

## Bandit Class

class Bandit(ABC):

    @abstractmethod
    def __init__(self, reward):
        self.reward = reward

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def update(self):
        pass

## -------------------------------

## ThompsonArm Class

class ThompsonArm(Bandit):
    """
    An implementation of the Thompson Sampling algorithm for multi-armed bandit problems.

    Inherits from the Bandit class.
    """
    
    def __init__(self, prev_N = 0, prev_x = 0, reward = 1):
        """
        Constructor for the ThompsonSampling class.
        """
        self.N = prev_N
        self.sum_x = prev_x
        self.reward = reward
        
    def __repr__(self):
        """
        String representation of the class.
        """
        return f"A Bandit with {self.m} Win Rate"


    def update(self, x):
        """
        Updates the bandit's posterior mean and precision using the reward received.
        """
        self.N += 1
        self.sum_x += x

## -------------------------------

## ThompsonAlgo Class

class ThompsonAlgo:
    
    def __init__(self, arms):
        
        self.arms = arms
      
    
    def get_best_arm(self):
        
        mean = [(m.sum_x / m.N) * m.reward if m.N > 0 else 0 for m in self.arms] 
        
        return np.argmax(mean)
        