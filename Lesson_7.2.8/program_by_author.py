from utils import load_questions_from_json, show_field, parse_input, print_question, show_stats, save_results_to_file, get_number_of_questions


questions = load_questions_from_json()
points, correct, incorrect = 0, 0, 0
questions_asked = 0
questions_total = get_number_of_questions(questions)


while questions_asked < questions_total:
    
    show_field(questions)
    
    user_input = input().title()
    user_data = parse_input(user_input)
    
    if not user_data:
        print("Нет такой категории или вопроса")
        continue

    category, price = user_data["category"], user_data["price"]

    question = questions[category][price]

    if question["asked"]:
        print("Этот вопрос уже был!")
        continue

    print_question(question["question"])
    user_answer = input().lower()

    if user_answer == question["answer"]:
        print("Ответ верный!")
        points += int(price)
        correct += 1
    else:
        print("Ответ неверный!")
        points -= int(price)
        incorrect += 1
    
    question["asked"] = True
    questions_asked += 1

show_stats(points, correct, incorrect)
save_results_to_file(points, correct, incorrect)
