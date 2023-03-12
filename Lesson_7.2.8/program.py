from utils import load_questions, show_field, parse_input, show_question, show_stats


def main():
    
    #flag = True
    user_score = 0
    #while flag == True:
    print(show_field())
    label_for_show_table = input("Введите через пробел название выбранной Вами категории и 1 из чисел, относящихся к данной категории:\n")
        #flag = False

    if label_for_show_table:
        parse_input_data = parse_input(label_for_show_table)
        user_input = input(f"{show_question(parse_input_data)[1]}\n").lower()
        if user_input == show_question(parse_input_data)[0]["answer"]:
            user_score += int(parse_input_data[1])
            print(f"Верно, +{parse_input_data[1]}. Ваш счёт = {user_score}")
        else:
            user_score -= int(parse_input_data[1])
            print(f"Неверно, на самом деле - {show_question(parse_input_data)[0]['answer']}. - {parse_input_data[1]}. Ваш счёт = {user_score}")


main()
