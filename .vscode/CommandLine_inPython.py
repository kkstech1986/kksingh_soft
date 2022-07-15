# Is project ko chalane ke liye cmd command line me jana hai our apne folder ko select karne ke bad usme apko d:\PythonProject\pytitorial\.vscode\CommandLine_inPython.py --x 5 --y 8 --o add iske bad Enter karna hai.
import argparse
import sys

def calc(args):
    if args.o=='add':
        return args.x+args.y
    elif args.o=='mul':
        return args.x*args.y
    elif args.o=='sub':
        return args.x-args.y
    elif args.o=='div':
        return args.x/args.y
    else:
        return "somthin went wrong"    
    
if __name__== "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,help="this is a utility for calculatin,please contract with kksingh.")
    
    parser.add_argument('--y',type=float,default=3.0,help="this is a utility for calculatin,please contract with kksingh.")
    
    parser.add_argument('--o',type=str,default="add",help="this is a utility for calculatin,please contract with kksingh.")
    
    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))
    