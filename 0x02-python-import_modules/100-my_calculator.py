#!/usr/bin/python3
def main():
    import sys
    import calculator_1 as calc
    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print(f"{a} {sys.argv[2]} {b} = {calc.add(a, b)}")
        elif sys.argv[2] == '-':
            print(f"{a} {sys.argv[2]} {b} = {calc.sub(a, b)}") 
        elif sys.argv[2] == '/':
            print(f"{a} {sys.argv[2]} {b} = {calc.div(a, b)}") 
        elif sys.argv[2] == '*':
            print(f"{a} {sys.argv[2]} {b} = {calc.mul(a, b)}") 
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)


if __name__ == "__main__":
    main()
