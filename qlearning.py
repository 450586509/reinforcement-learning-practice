from collections import defaultdict
import random
import math
import numpy as np


class QLearningAgent:
    def __init__(self, alpha, epsilon, discount, get_legal_actions):
        """
        Q-Learning Agent
        based on https://inst.eecs.berkeley.edu/~cs188/sp19/projects.html
        Instance variables you have access to
          - self.epsilon (exploration prob)
          - self.alpha (learning rate)
          - self.discount (discount rate aka gamma)

        Functions you should use
          - self.get_legal_actions(state) {state, hashable -> list of actions, each is hashable}
            which returns legal actions for a state
          - self.get_qvalue(state,action)
            which returns Q(state,action)
          - self.set_qvalue(state,action,value)
            which sets Q(state,action) := value
        !!!Important!!!
        Note: please avoid using self._qValues directly.
            There's a special self.get_qvalue/set_qvalue for that.
        """

        self.get_legal_actions = get_legal_actions
        self._qvalues = defaultdict(lambda: defaultdict(lambda: 0))
        self.alpha = alpha
        self.epsilon = epsilon
        self.discount = discount

    def get_qvalue(self, state, action):
        """ Returns Q(state,action) """
        return self._qvalues[state][action]

    def set_qvalue(self, state, action, value):
        """ Sets the Qvalue for [state,action] to the given value """
        self._qvalues[state][action] = value

    # ---------------------START OF YOUR CODE---------------------#

    def get_value(self, state):
        """
        Compute your agent's estimate of V(s) using current q-values
        V(s) = max_over_action Q(state,action) over possible actions.
        Note: please take into account that q-values can be negative.
        """
        possible_actions = self.get_legal_actions(state)

        # If there are no legal actions, return 0.0
        if len(possible_actions) == 0:
            return 0.0

        action_value_dict = self._qvalues[state]
        max_value = -100
        # for action, value in action_value_dict.items():
        #    if value > max_value:
        #        max_value = value
        for action in possible_actions:
            if self._qvalues[state][action] >= max_value:
                max_value = self._qvalues[state][action]

        return max_value

    def update(self, state, action, reward, next_state):
        """
        You should do your Q-Value update here:
           Q(s,a) := (1 - alpha) * Q(s,a) + alpha * (r + gamma * V(s'))
        """

        # agent parameters
        nextState = next_state
        gamma = self.discount
        learning_rate = self.alpha

        qsa = self._qvalues[state][action]
        # print("nextState={0}".format(nextState))
        # all nextState
        state_value = self.get_value(next_state)
        updated_qvalue = (1 - learning_rate) * qsa + learning_rate * (reward + gamma * state_value)
        # (state, action, value)
        self.set_qvalue(state, action, updated_qvalue)

    def get_best_action(self, state):
        """
        Compute the best action to take in a state (using current q-values).
        """
        possible_actions = self.get_legal_actions(state)

        # If there are no legal actions, return None
        if len(possible_actions) == 0:
            return None
        best_action = None
        action_value_dict = self._qvalues[state]
        # print("action_value_dict={0}".format(action_value_dict))
        max_value = -100
        # for action, value in action_value_dict.items():
        for action in possible_actions:
            # print("action={0}\tvalue={0}".format(action, value))
            if self._qvalues[state][action] > max_value:
                max_value = self._qvalues[state][action]
                best_action = action
        # print("get policy best action = {0}".format(best_action))
        return best_action

    def get_action(self, state):
        """
        Compute the action to take in the current state, including exploration.
        With probability self.epsilon, we should take a random action.
            otherwise - the best policy action (self.get_best_action).

        Note: To pick randomly from a list, use random.choice(list).
              To pick True or False with a given probablity, generate uniform number in [0, 1]
              and compare it with your probability
        """

        # Pick Action
        possible_actions = self.get_legal_actions(state)
        possibleActions = possible_actions
        action = None

        # If there are no legal actions, return None
        if len(possible_actions) == 0:
            return None

        # agent parameters:
        epsilon = self.epsilon

        best_action = self.getPolicy(state=state)
        vals = random.choices([1, 2], k=1, weights=[epsilon, 1 - epsilon])
        # print("epsilon={0}\tval={1}".format(epsilon, vals[0]))
        if vals[0] == 1:
            action = random.choice(possibleActions)
        else:
            # print("get action by policy")
            action = best_action
        # print("chosen action={0}".format(action))

        return action

    def getPolicy(self, state):
        """
          Compute the best action to take in a state.

        """
        possibleActions = self.get_legal_actions(state)
        # print("possibleActions={0}".format(possibleActions))

        # If there are no legal actions, return None
        if len(possibleActions) == 0:
            return None

        best_action = None

        "*** YOUR CODE HERE ***"
        max_value = -100
        best_action = None
        for action in possibleActions:
            if self._qvalues[state][action] >= max_value:
                max_value = self._qvalues[state][action]
                best_action = action

        return best_action