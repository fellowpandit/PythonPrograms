# Write a python program to stimulate a simple calculator

def calculator(op1, op2, op):
    if (op == '^'):
        op == '**'

    return eval(op1 + op + op2)


def main():
    try:
        print(calculator('3', '2', '+'))
    except:
        print("Invalid operator")


main()
