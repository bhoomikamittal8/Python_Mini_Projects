def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def rem(n1, n2):
    return n1 % n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": rem,
}


def calculator():
    num1 = float(input("What's the First Number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_choice = input("Pick an Operation: ")
        num2 = float(input("What's the next Number?: "))
        calculation_function = operations[operation_choice]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_choice} {num2} = {answer}")

        more = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, type S to stop: ")
        if more == "y":
            num1 = answer
        elif more == "n":
            should_continue = False
            calculator()
        else:
            break


calculator()