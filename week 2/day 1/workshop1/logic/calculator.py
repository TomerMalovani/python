from logic.numbers_generate import generate_two_numbers


def add_generated_numbers():
    num1, num2 = generate_two_numbers()
    return add(num1, num2)


def add(num1, num2):
    return num1 + num2
