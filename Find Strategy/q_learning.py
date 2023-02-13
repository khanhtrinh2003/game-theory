import random

EPISODE = 10000
EPSILON = 0.1

class Chien_luoc():
    def __init__(self,strate,payoff,prob_rival):
        self.k = 0
        self.q = 0
        self.strate = strate

        self.payoff = payoff
        self.num_strategy_rival = len(self.payoff[0])
        self.prob_rival = prob_rival

    def get_reward(self):
        stra2 = random.choices(list(range(self.num_strategy_rival)), weights=self.prob_rival, k=1)[0]
        return self.payoff[self.strate][stra2]
    
class find_best_strategy():
    def __init__(self,payoff,num_strategy,prob_rival):
        self.payoff = payoff
        self.num_strategy = num_strategy
        self.prob_rival = prob_rival

        self.list_strategy = [Chien_luoc(i,payoff=self.payoff, prob_rival=self.prob_rival) for i in range(self.num_strategy)]


    def run(self):
        for i in range(EPISODE):
            index = self.get_strategy()
            stra = self.list_strategy[index]
            reward = stra.get_reward()
            self.update(stra,reward)
            print(f'Iteration {i}, strategy {index} with Q value {stra.q}')        
    def get_strategy(self):
        if random.random() < EPSILON:
            return random.randint(0, self.num_strategy-1)
        else:
            return self.get_best_strategy_index()
        
    def get_best_strategy_index(self):
        best_index = 0
        best = self.list_strategy[best_index].q
        for i in range(1,self.num_strategy):
            if self.list_strategy[i].q>=best:
                best = self.list_strategy[i].q
                best_index = i
        return best_index
    
    def update(self, stra, reward):
        stra.k = stra.k+1
        stra.q = stra.q*0.9+0.1*reward 

    def show_statistics(self):
        for i in range(self.num_strategy):    
            print(f'Strategy {i} with k: {self.list_strategy[i].k}')           
