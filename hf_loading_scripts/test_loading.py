from datasets import (
    load_dataset
)
import json

### VAW dataset ###

## from local dataset loading script
# dataset = load_dataset("./vaw") # automatically download files and generate dataset specified by the .py script

## from huggingface dataset hub: https://huggingface.co/datasets/mikewang/vaw
# dataset = load_dataset("mikewang/vaw") 

# print(dataset['train'][0])
# print(dataset['train'][108395]) # first instance in part2
# print(dataset['validation'][0])
# print(dataset['test'][0])


### imSitu dataset ###

# from local dataset loading script
# dataset = load_dataset("./imsitu") # automatically download files and generate dataset specified by the .py script

# from huggingface dataset hub: 
dataset = load_dataset("mikewang/imsitu") 

print(dataset['train'][0])
frames = [json.loads(obj) for obj in dataset['train'][0]['frames']]
print(frames)
print(dataset['validation'][0])
print(dataset['test'][0])

