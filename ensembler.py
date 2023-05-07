from typing import Tuple
from sampler import sampler
from parser.closed_qa import parser
import math

class ensembler:
    def __init__(self, key:str, kind:str):
        self.s = sampler(key=key, type_=kind)
        self.p = parser()
    
    def decode(self, question:str, iterations:int=10)->Tuple[str,float]:
        ans = []
        for i in range(iterations):
            ans.append(self.s.question(question))
        ans_dict = self.p.parse(ans)
        majority_ans = max(ans_dict, key=ans_dict.get)
        entropy = self.get_entropy(ans_dict)
        return majority_ans,entropy

    def get_entropy(self, ans_dict:dict)->float:
        N = sum(ans_dict.values())
        entropy = 0
        for i in ans_dict:
            p = ans_dict[i]/N
            entropy += p*math.log(p)
        return (-1*entropy)

### TODO need to convert to a class; add entropy function for uncertainity in estimation