import argparse
import sys
def foltycalc(args):
    if args.c=="add":
            if args.a==78 or args.a==23 and args.b==23 or args.b==78: 
                return print(f"{args.a}+{args.b} is :",666)
            else:
                return print(f"{args.a}+{args.b} is :",args.a+args.b)
    elif args.c=="sub":
            if args.a==45 or args.a==12 and args.b==12 or args.b==45:        
                return print(f"{args.a}+{args.b} is :",79)
            else:
               return print(f"{args.a}-{args.b} is :",args.a-args.b)
    elif args.c=="mul":
            if args.a==56 or args.a==3 and args.b==3 or args.b==56:        
             return print(f"{args.a}+{args.b} is :",555)
            else:
                return print(f"{args.a}x{args.b} is :",args.a*args.b)
    elif args.c=="div":   
            if args.a==45 or args.a==6 and args.b==6 or args.b==45:        
                return print(f"{args.a}+{args.b} is :",80) 
            else:
             return print(f"{args.a}/{args.b} is :",args.a/args.b)
    elif args.c=="per":
            if args.a==34 or args.a==4 and args.b==4 or args.b==34:        
                return print(f"{args.a}%{args.b} is :",78)
            else:
                return print(f"{args.a}%{args.b} is :",args.a%args.b)
    else:
        return print("Somthig is wrong please take and reEnter")

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--a',type=float,default=1.0,help="this is a utility for calculatin,please contract with kksingh.")
    
    parser.add_argument('--b',type=float,default=3.0,help="this is a utility for calculatin,please contract with kksingh.")
    
    parser.add_argument('--c',type=str,default="add",help="this is a utility for calculatin,please contract with kksingh.")
    
    args=parser.parse_args()
    sys.stdout.write(str(foltycalc(args)))
          

