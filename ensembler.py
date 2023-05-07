from typing import Tuple
from sampler import sampler
from parser.closed_qa import parser
import math

class ensembler:
    def __init__(self, key:str, kind:str):
        self.s = sampler(key=key, type_=kind)
        self.p = parser()
    
    def decode(self, question:str, iterations:int=3)->Tuple[str,float,float]:
        ans = []
        for i in range(iterations):
            ans.append(self.s.question(question))
        ans_dict = self.p.parse(ans)
        majority_ans = max(ans_dict, key=ans_dict.get)
        maj_freq = max(ans_dict.values())
        maj_prob = maj_freq/sum(ans_dict.values())
        entropy = self.get_entropy(ans_dict)
        if(entropy==0):
            scaled_entropy=0
        else:
            scaled_entropy = entropy/math.log(len(ans_dict))
        return majority_ans,scaled_entropy,maj_prob

    def get_entropy(self, ans_dict:dict)->float:
        N = sum(ans_dict.values())
        entropy = 0
        for i in ans_dict:
            p = ans_dict[i]/N
            entropy += p*math.log(p)
        return (-1*entropy)