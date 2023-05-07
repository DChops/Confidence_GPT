import streamlit as st
from ensembler import ensembler

ens = ensembler(key="<Your key here>", kind="closed_qa")

st.title("Farmer-GPT")
st.markdown("## A 24/7 agricultural science aid to Farmers")

text = st.text_area(label="Ask your questions here")

if st.button(label="Submit"):
    ans, conf, prob = ens.decode(question=text)
    st.write("The answer is "+ans+", occuring with probability "+str(prob)+", and with scaled entropy value (0-best,1-worst) "+str(conf)+".")