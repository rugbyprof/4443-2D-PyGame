import sys
import json

def straightDistance(x1,y1,x2,y2):
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return distance

def taxicabDistance(xA,yA,xB,yB):
    distance = abs(xA-xB) + abs(yA-yB)
    return distance

def mykwargs(argv):
    '''
    Processes argv list into plain args and kwargs.
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}

        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs

def load_colors(infile):
    with open(infile,'r') as f:
        data = f.read()
        colors = json.loads(data)
    return colors