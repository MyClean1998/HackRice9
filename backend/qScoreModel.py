import numpy as np

class QScoreModel:

    def __init__(self, num_features, lr):
        self.num_features = num_features
        self.learning_rate = lr

    def forward(self, features):
        raise Exception("Forward method must be implemented by subclasses.")
    
    def backward(self, loss):
        raise Exception("Forward method must be implemented by subclasses.")

class LinearQScore(QScoreModel):
    
    def __init__(self, num_features, lr):
        super().__init__(num_features, lr)
        self.weights = np.random.normal(size=(num_features))
        
        
    def forward(self, features):
        return np.inner(features, self.weights)
    
    def backward(self, expected, features):
        # print(features)
        self.weights += self.learning_rate * (expected - self.forward(features)) * features
    
    def print_weights(self):
        print(self.weights)