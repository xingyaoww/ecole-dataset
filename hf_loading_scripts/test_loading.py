from datasets import (
    load_dataset
)


### VAW dataset ###

## from local dataset loading script
# dataset = load_dataset("./vaw") # automatically download files and generate dataset specified by the .py script

## from huggingface dataset hub: https://huggingface.co/datasets/mikewang/vaw
dataset = load_dataset("mikewang/vaw") 

print(dataset['train'][0])
print(dataset['train'][108395]) # first instance in part2
print(dataset['validation'][0])
print(dataset['test'][0])
