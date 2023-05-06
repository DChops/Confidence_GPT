# Confidence_GPT
Adding confidence scores to Chat-GPT's predictions to detect hallucinations

## Project Specifications:
We are attempting to build upon the ideas of [Wang et. al.](https://arxiv.org/pdf/2203.11171.pdf) & [Lakshminarayanan et. al.](https://proceedings.neurips.cc/paper/2017/file/9ef2ed4b7fd2c810847ffa5fa85bce38-Paper.pdf) in this project.

To improve the accuracy of the LLM, we use Wang et. al.'s idea of 'self-consistency', which involves sampling the answer to the same question multiple times and using the answer with the maximum frequency as the answer returned t othe user. The whole process can be though of as a majority vote, which amplifies the chances to arrive at the correct answer and discards unfrequent 'hallucinations'.

Next, we extend this by using Lakshminarayanan et. al.'s ideas on uncertainity in prediction to quantify how sure the LLM is about the final answer. This metric can be used to set a threshold that prevents hallucinatory answers from being displayed to the user.

## Files and their usage
1. sampler.py -> makes a single query to Open AI's ChatGPT
2. prompts/ -> folder containing exemplar prompts for different tasks
3. ensembler.py -> uses sampler's results to cast a majority vote among answers
4. parser/ -> folder contains parsers corresponding to different input prompts
5. example_usage.py -> demonstration on how to use the provided codes

##### Note: We'll provide the codes for the "Closed QA" use case first, and other use cases can be subsequently appended