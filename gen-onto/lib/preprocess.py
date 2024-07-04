
import re

def preprocess(inputs):
    outputs = []
    for i in inputs:
        i = i.lower()
        x = i.replace('"', " ")
        a = x.replace("(", " ")
        b = a.replace(")", " ")
        c = re.sub('\s+',' ',b)

        if(c == " "):
            continue
        
        if (c == ' s'):
            outputs.append(c.strip())        
        else:
            outputs.append(c)
    return outputs

