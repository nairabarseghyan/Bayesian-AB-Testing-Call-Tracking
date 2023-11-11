from AB_Testing.models.base import Bandit

class BernoulliThomsponSampling():
    def __init__(self, true_mean):
        super().__init__(true_mean)
        self.a = 1
        self.b = 1
        self.N = 0