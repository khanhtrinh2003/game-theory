import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Kiem_dinh():
    def __init__(self, 
                so_chien_luoc1, 
                so_chien_luoc2, 
                payoff1, 
                payoff2,
                mix_stra1,
                mix_stra2
                ):
        self.so_chien_luoc1 = so_chien_luoc1
        self.so_chien_luoc2 = so_chien_luoc2
        self.payoff1 = payoff1
        self.payoff2 = payoff2
        self.mix_stra1 = mix_stra1
        self.mix_stra2 = mix_stra2

        self.Peo1 = list(range(self.so_chien_luoc1))
        self.Peo2 = list(range(self.so_chien_luoc2))

    def mat_do_loi_ich(self): 
        
        u1 =[]
        u2 = []
        
        for i in range(100000):
            s1 = random.choices(self.Peo1, weights=self.mix_stra1, k=1)
            s2 = random.choices(self.Peo2, weights=self.mix_stra2, k=1)    
            
            chien_luoc = [list(e) for e in zip(s1, s2)]
            u1.append(sum(list(map(self.thu_hoach1, chien_luoc))))
            u2.append(sum(list(map(self.thu_hoach2, chien_luoc))))                        
        u = pd.DataFrame({f"Lợi ích của người 1": u1,f"Lợi ích của người 2": u2})
        
        fig= plt.subplots(1,1)
        u[f"Lợi ích của người 1"].plot(kind='hist')
        u[f"Lợi ích của người 2"].plot(kind='hist')
        plt.legend()
        plt.xlabel("Lợi ích thu được được")
        plt.savefig(fname='test')
        return fig
    
    def thu_hoach1(self,s):
        return self.payoff1[s[0]][s[1]]

    def thu_hoach2(self,s):
        return self.payoff2[s[0]][s[1]]

