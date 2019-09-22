import random
import numpy as np
from copy import deepcopy
# from qScoreModel import LinearQScore

class QLearningAgent:

    def __init__(self, discount, lr, epsilon, num_training, is_training=False):
        self.is_training = is_training
        self.discount = discount
        self.epsilon = epsilon
        self.evoke_envir = None
        self.num_training = num_training
        self.q_value_model = LinearQScore(110, lr)
        self.cur_episode = 0
        self.equips = ['Pump', 'Compressor', 'Seperator', 'Sensor', 'Security', 'Electricity', 'Networking', 'Vehicle', 'HVAC', 'Conveyer']
        self.num_equips = len(self.equips)
        
    def get_q_features(self, state, action):
        equip_job_todo = state.get_jobs_with_equip('pending')
        equip_job_doing = state.get_jobs_with_equip('in progress')
        features = np.zeros((len(equip_job_todo.keys()), 11))
        for i in range(self.num_equips):

            jobs_todo = equip_job_todo[self.equips[i]]
            if jobs_todo == []:
                features[i, 0] = 0
                features[i, 1] = 0
                features[i, 2] = 0
                features[i, 3] = 0
                features[i, 4] = 0
                features[i, 5] = 0
                features[i, 6] = 0
            else:
                todo_priorities = [job.priority for job in jobs_todo]
                todo_duration = [job.duration for job in jobs_todo]
                todo_waited = [job.time_waited for job in jobs_todo]
            
                features[i, 0] = max(todo_priorities)
                features[i, 1] = np.mean(todo_priorities)
                features[i, 2] = max(todo_duration)
                features[i, 3] = np.mean(todo_duration)
                features[i, 4] = max(todo_waited)
                features[i, 5] = np.mean(todo_waited)
                features[i, 6] = len(equip_job_todo) 
            features[i, 7] = len(state.get_available_workers(self.equips[i])) 
            features[i, 8] = len(state.get_available_facilities(self.equips[i]))
            ip_rest = [job.time_rest for job in equip_job_doing[self.equips[i]]]
            if ip_rest == []:
                features[i, 9] = 0
            else:
                features[i, 9] = min([job.time_rest for job in equip_job_doing[self.equips[i]]])
            features[i, 10] = action[0].priority 
        return features.flatten()
    
    def set_evoke_func(self, evoke_func):
        self.evoke_envir = evoke_func
            
    def is_training(self):
        return self.is_training
    
    def is_Testing(self):
        return not self.is_training
    
    def get_q_value(self, state, action):
        features = self.get_q_features(state, action)
        return self.q_value_model.forward(features)

    def get_legal_actions(self, state):
        return state.get_worker_job_pairs()

    def compute_value_from_q_value(self, state):
        if len(self.get_legal_actions(state)) == 0:
            return 0
        return max(map(lambda action: self.get_q_value(state, action), self.get_legal_actions(state)))
    
    def compute_action_from_q_value(self, state):
        sorted_actions = map(lambda action: (action, self.get_q_value(state, action)), self.get_legal_actions(state))
        best_actions = []
        best_val = -float('inf')
        if sorted_actions == []:
            return None
        for action, val in sorted_actions:
            if val > best_val:
                best_actions = [action]
                best_val = val
            elif val == best_val:
                best_actions.append(action)
        return random.choice(best_actions)
    
    def get_action(self, state):
        if self.get_legal_actions(state) == []:
            return None
        if random.random() < self.epsilon:
            return random.choice(self.get_legal_actions(state))
        return self.compute_action_from_q_value(state)
    
    def update(self, state, action, nextState):
        expected = nextState.get_reward() + self.discount * self.compute_value_from_q_value(nextState)
        self.q_value_model.backward(expected, self.get_q_features(state, action))

    def do_action(self, state):
        # print("Doing Action")
        self.cur_episode += 1
        action = self.get_action(state)
        if action == None:
            return
        if self.is_training:
            current_state = deepcopy(state)
            state.update_state(action)
            self.update(current_state, action, state)
        else:
            state.update_state(action)
        self.evoke_envir(action)
    


            
    

    

