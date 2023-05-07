from ensembler import ensembler

ens = ensembler(key="", kind="closed_qa")
ans, conf = ens.decode(question="Who was the president of India in 2012?")
print("The answer is "+ans+", with entropy value "+str(conf)+".")