import random

class QLearn:
    def __init__(self, actions, epsilon=0.1, alpha = 0.2, gamma=0.9):
        self.q={}
        self.epsilon=epsilon
        self.alpha=alpha
        self.gamma=gamma
        self.actions = actions

    def getQ(self, state, action):
        return self.q.get((state, action), 0.0)

    def learn(self, state, action, reward, state2):
        if self.q.has_key((state, action)) == False:
            update = reward
            self.q[(state, action)] = update
        else:
            maxq = max([self.getQ(state2,a) for a in self.actions])
            update = reward +self.gamma*maxq
            self.q[(state, action)] += update

        return update

    def chooseAction(self, state):
        if random.random() < self.epsilon:
            action = random.choice(self.actions)
        else:
            q = [self.getQ(state, a) for a in self.actions]
            qmax = max(q)
            count = q.count(qmax)
            if count > 1:
                best = [i for i in range(len(self.actions)) if q[i] == qmax]
                i = random.choice(best)
            else:
                i = q.index(qmax)

            action = self.actions[i]

        return action

    