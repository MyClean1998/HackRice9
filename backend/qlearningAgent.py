class QLearningAgent:

    def __init__(self, discount, lr, epsilon, num_training, is_training=False):
        self.is_training = is_training
        self.discount = discount
        self.learning_rate = lr
        self.epsilon = epsilon
        self.num_training = num_training
        self.cur_episode = 0
    
    def is_training(self):
        return self.is_training
    
    def is_Testing(self):
        return not self.is_training
    
    def get_q_value(self, state, action):
        # TODO: implement a feature-based q-value function.
        pass

    def get_legal_actions(self, state):
        pass

    def compute_value_from_q_value(self, state):
        action_q_pair = self.get_legal_actions(state).map(lambda action: (action, self.get_q_value(state, action)))
        return sorted(action_q_pair, key=1, reverse=True)[0]
    

    

