import openai
import json
import os

class sampler:
    def __init__(self, key:str, type_:str) -> None:
        openai.api_key = key
        f = open(os.path.join(os.getcwd(),"prompts",type_+".json"))
        self.diction = json.load(f)
        f.close()

    def question(self, question:str):
        self.diction["messages"].append({"role": "user", "content": question})
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=self.diction["messages"],
        temperature=0.7,
        )
        return response['choices'][0]['message']['content']