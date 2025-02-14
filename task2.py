def typeBasedTransformer(**args):
    myresult = {}

    for k, j in args.items():
        if isinstance(j, (int, float)):  
            myresult[k] = j ** 2
        elif isinstance(j, str):  
            myresult[k] = j[::-1]
        elif isinstance(j, bool):  
            myresult[k] = not j
        elif isinstance(j, (list, tuple)):  
            myresult[k] = type(j)(j[::-1])
        elif isinstance(j, dict):  
            if len(set(j.values())) == len(j):  
                myresult[k] = {v: k for k, v in j.items()}
            else:
                myresult[k] = j
        else:
            myresult[k] = j  

    return myresult
