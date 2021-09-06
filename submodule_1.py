import json

def input_reader(s):
    
    f = open(s,)

    data = json.load(f)

    return data

