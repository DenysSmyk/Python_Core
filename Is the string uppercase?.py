def is_uppercase(inp):
    inp_j = "".join(inp.split())
    res=True
    for i in inp_j:
        if i.islower():
            res = False
    return res