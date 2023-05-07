from ensembler import ensembler

ens = ensembler(key="<Put your key here>", kind="closed_qa")
ans, conf, prob = ens.decode(question="Who was the president of India in when 9/11 happened?")
print("The answer is "+ans+", occuring with probability "+str(prob)+", and with scaled entropy value (0-best,1-worst) "+str(conf)+".")