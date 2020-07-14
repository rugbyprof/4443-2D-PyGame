import sys
import os
import json # not necessary
import pprint

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

def main(**kwargs):
    print("Printing kwargs from main function")
    pprint.pprint(kwargs)

def usage():
    # Params in square brackets are optional
    # The kwargs function script needs key=value to NOT have spaces
    print("Usage: python basic.py title=string img_path=string width=int height=int [jsonfile=string]")
    print("Example:\n\n\t python basic.py title='Game 1' img_path=./sprite.png width=640 height=480 \n")
    sys.exit()

if __name__=='__main__':
    """
    This example has 4 required parameters, so after stripping the file name out of
    the list argv, I can test the len() of argv to see if it has 4 params in it.
    """
    argv = sys.argv[1:]

    if len(argv) < 4:
        print(len(argv))
        usage()

    args,kwargs = mykwargs(argv)

    # here you have a dictionary with all your parameters in it
    print("Printing dictionary from name == main:")
    pprint.pprint(kwargs)

    # you could send all of them to a main function
    main(**kwargs)