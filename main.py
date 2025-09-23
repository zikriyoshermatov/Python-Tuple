from calculator.add import add
from calculator.sub import subs
from calculator.div import div
from calculator.mult import mult


def main():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    op = input("Operator: ")

    if op == '+':
        r = add(num1, num2)
    elif op == "-":
        r = subs(num1, num2)
    elif op == "/":
        r = div(num1, num2)
    elif op == "*":
        r = mult(num1, num2)

    print(r)

main()
