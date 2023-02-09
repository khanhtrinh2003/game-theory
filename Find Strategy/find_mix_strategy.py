import numpy as np
from scipy.optimize import linprog

def find_mix_strategy(payoff):
    payoff_extended = [i + [-1] for i in payoff]
    A_ub = np.array(payoff_extended)
    b_ub = np.zeros(len(payoff))
    A_eq = np.array([[1] * len(payoff[0]) + [0]])
    b_eq = np.array([1])
    c = np.array([0] * len(payoff[0]) + [1])
    res = linprog(c, A_ub=A_ub, b_ub=b_ub,bounds=(0, None), A_eq=A_eq,b_eq=b_eq)
    return f"Kỳ vọng của mình: {res.fun} \nChiến lược đối thủ: {res.x}" 

