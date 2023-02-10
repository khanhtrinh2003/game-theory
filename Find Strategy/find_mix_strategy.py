import numpy as np
from scipy.optimize import linprog

def find_mix_strategy_in_zero_sum(payoff):
    payoff_extended = [i + [-1] for i in payoff]
    A_ub = np.array(payoff_extended)
    b_ub = np.zeros(len(payoff))
    A_eq = np.array([[1] * len(payoff[0]) + [0]])
    b_eq = np.array([1])
    c = np.array([0] * len(payoff[0]) + [1])
    res = linprog(c, A_ub=A_ub, b_ub=b_ub,bounds=(0, None), A_eq=A_eq,b_eq=b_eq)
    return f"Kỳ vọng của mình: {res.fun} \nChiến lược đối thủ: {res.x}" 

def find_mix_strategy(payoff1, payoff2):
    payoff11 = [i + [0]*len(payoff2) +[-1,0] for i in payoff1]
    payoff21 = [[0]*len(payoff1) +i + [0,-1] for i in payoff2]
    t=payoff11+payoff21
    A_ub = np.array(t)
    b_ub = np.zeros(len(t))
    
    e = [[1]*len(payoff1) + [0]*len(payoff2) +[0,0]] + [[0]*len(payoff1) +[1]*len(payoff2) + [0,0]]
    A_eq = np.array(e)
    b_eq = np.ones(2)
    c = np.array([0] * len(t) + [1,1])
    res = linprog(c, A_ub=A_ub, b_ub=b_ub,bounds=(0, None), A_eq=A_eq,b_eq=b_eq)
    return f"Chiến lược của người 1:{res.x[len(payoff1):len(payoff1)+len(payoff2)]}\nChiến lược của người 2:{res.x[:len(payoff1)]},\nKỳ vọng của người 1: {res.x[len(payoff1)+len(payoff2):len(payoff1)+len(payoff2)+1]},\nKỳ vọng của người 2: {res.x[len(payoff1)+len(payoff2)+1:len(payoff1)+len(payoff2)+2]}"