from random import randrange
wrong_answers_list = []


def main():
    print("hey kids do you want to play?")
    game_play_request = input("answer: ")
    game_on = game_play_request == "yes"
    count_right_answers, count_wrong_answers = 0, 0
    while game_on:
        answer = current_qusetion()
        if answer == True:
            count_right_answers += 1
            print("right!")
            game_on = play_again()
        if answer == False:
            count_wrong_answers += 1
            print("wrong :(")
            game_on = play_again()
        if answer == "nan":
            print("thats not a number buddy.., lets try again")

    print(
        f"right answers: {count_right_answers} wrong answers: {count_wrong_answers}")
    for fixed_answer in wrong_answers_list:
        print(fixed_answer)


def current_qusetion():
    num_one, num_two = (randrange(20)), (randrange(20))
    operator_list = ["+", "-", "*", "/"]
    current_operator = operator_list[randrange(4)]
    if current_operator == "-" and num_two > num_one:
        num_one, num_two = num_two, num_one
    if current_operator == "/" and num_two == 0:
        num_two = (randrange(1, 20))
    if current_operator == "/" and num_one % num_two != 0:
        num_one = division_logic(num_two)
    answer = current_answer(num_one, num_two, current_operator)
    user_answer = input(f"{num_one} {current_operator} {num_two}= ")
    if not user_answer.isdigit():
        is_answer_right = "nan"
    else:
        is_answer_right = True if int(user_answer) == answer else False
    if not is_answer_right:
        wrong_answers_list.append(
            f"{num_one} {current_operator} {num_two}= {int(user_answer)} (right answer: {answer})")
    return is_answer_right


def current_answer(num_one, num_two, operator):
    if operator == "+":
        return num_one + num_two
    if operator == "-":
        return num_one - num_two
    if operator == "*":
        return num_one * num_two
    if operator == "/":
        return num_one / num_two


def division_logic(num_two):
    return num_two * (randrange(1, 5))


def play_again():
    game_play_request = input("again?: ")
    game_on = True if game_play_request == "yes" else False
    return game_on


main()
