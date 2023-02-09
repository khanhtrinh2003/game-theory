import numpy as np
import matplotlib.pyplot as plt
import random

class Calculation():
    def __init__(self,chien_luoc_1,chien_luoc_2,payoff1):
        self.chien_luoc_1 = np.array(chien_luoc_1)
        self.chien_luoc_2 = np.array(chien_luoc_2)
        self.payoff1 = payoff1

    def expected_value(self):
        E = np.dot(np.dot(self.chien_luoc_1.T, self.payoff1), self.chien_luoc_2)
        return E
    
    def variance(self):
        V = np.dot((np.dot(self.chien_luoc_1.T, self.payoff1)-self.expected_value())**2,self.chien_luoc_2)
        return V
    
class Graph():
    def __init__(self, A, p2):
        self.A = A
        self.p2 = [i/sum(p2) for i in p2]
        self.n = 50000
        
        num =len(self.p2)
        ra1 = np.random.rand(self.n, num)
        ra2 = np.random.rand(self.n, num)
        self.x = ra1 / np.sum(ra1, axis=1, keepdims=True)
        self.y = ra2 / np.sum(ra2, axis=1, keepdims=True)

        self.max_index = 0
        
    def relation(self):
        e1 = []
        v1 = []       
        for i in range(self.n):
            c = Calculation(payoff1=self.A, chien_luoc_1=self.x[i], chien_luoc_2=self.y[i])
            e1.append(c.expected_value())
            v1.append(c.variance())
        plt.scatter(v1, e1)
        plt.xlabel("Variance")
        plt.ylabel("Expected Value")

    def curve(self):
        e1 = []
        v1 = []

        for i in range(self.n):
            c = Calculation(payoff1=self.A, chien_luoc_1=self.x[i], chien_luoc_2=self.p2)
            e1.append(c.expected_value())
            v1.append(c.variance())
        plt.scatter(v1, e1,color="pink")
        
        num = len(self.p2)
        self.o =np.eye(num)
        for i in range(num):
            p = np.array(self.o[i])
            c = Calculation(payoff1=self.A, chien_luoc_1=p, chien_luoc_2=self.p2)
            plt.scatter(c.variance(),c.expected_value(), label=f"Chiến lược {i}")
            plt.legend()

        self.max_index = np.argmax(np.array(e1)-np.array(v1))
        plt.scatter(v1[self.max_index],e1[self.max_index],color="black", label="E-V max")
        plt.legend()

    def e_minus_v_values(self):
        return f"Chiến lược để E-V max là {self.x[self.max_index]}"