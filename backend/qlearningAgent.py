import random
import numpy as np

class QLearningAgent:

    def __init__(self, discount, lr, epsilon, num_training, evoke_envir, is_training=False):
        self.is_training = is_training
        self.discount = discount
        self.epsilon = epsilon
        self.evoke_envir = evoke_envir
        self.num_training = num_training
        self.q_value_model = None
        self.cur_episode = 0
        self.equips = []
        self.num_equips = len(self.equips)
        
    def get_q_features(self, state, action):
        equip_job_todo = state.get_jobs_with_equip("pending")
        equit_job_doing = state.get_jobs_with_equip("in progress")
        features = np.zeros((len(equip_job_todo.keys()), 6))
        for i in range(self.num_equips):
            jobs_todo = equip_job_todo[self.equips[i]]
            jobs_doing = equit_job_doing[self.equips[i]]
            # TODO: put all features into mat
        return features.flatten()
            
    def is_training(self):
        return self.is_training
    
    def is_Testing(self):
        return not self.is_training
    
    def get_q_value(self, state, action):
        features = state.get_q_features(state, action)
        return q_value_model.forward(features)

    def get_legal_actions(self, state):
        return state.get_worker_job_pairs()

    def compute_value_from_q_value(self, state):
        return max(self.get_legal_actions(state).map(lambda action: self.get_q_value(state, action)))
    
    def compute_action_from_q_value(self, state):
        sorted_actions = self.get_legal_actions(state).map(lambda action: (action, self.get_q_value(state, action)))
        best_actions = []
        best_val = -float('inf')
        for action, val in sorted_actions:
            if val > best_val:
                best_actions = [action]
                best_val = val
            elif val == best_val:
                best_actions.append(action)
        return random.choice(best_actions)
    
    def get_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.get_legal_actions(state))
        return self.compute_action_from_q_value(state)
    
    def update(self, state, action, nextState, reward):
        expected = reward + self.discount * self.computeValueFromQValues(nextState)
        self.q_value_model.backward(expected)

    def do_action(self, state):
        self.cur_episode += 1
        if self.is_training:
            self.update(state)
        self.evoke_envir(self.get_action(state))
    


            
    

    

