from question import Question
from utils import load_questions, correct_answers_count, points_count


def main():
    
    questions = load_questions()
    
    for question in questions:
        print(question.build_question())
        user_answer = input()
        question.user_answer = user_answer
        if question.is_correct():
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())

    correct_counter = correct_answers_count(questions)
    points = points_count(questions)
    
    print(f"Вот и всё!")
    print(f"Вы правильно ответили на {correct_counter} вопроса из {len(questions)}")
    print(f"Набрано баллов: {points}")


main()
