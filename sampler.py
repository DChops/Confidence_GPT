import openai
import json
import os

class sampler:
    def __init__(self, key:str, type_:str) -> None:
        openai.api_key = key
        self.diction = json.load(
            os.path.join(os.getcwd(),"prompts",type_+".json")
            )

    def question(self, question:str):
        message = self.diction["messages"].append({"role": "user", "content": question})
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
        )
        return response['choices'][0]['message']['content']