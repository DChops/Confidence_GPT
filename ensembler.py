from sampler import sampler
from parser.closed_qa import parser

s = sampler(key="abc", type_="closed_qa")
p = parser()

ans = []
iterations = 10
for i in range(iterations):
    ans.append(s.question("Who was the President of India in 2015?"))

ans_dict = p.parse(ans)

majority_ans = max(ans_dict, key=ans_dict.get)

### TODO need to convert to a class; add entropy function for uncertainity in estimation