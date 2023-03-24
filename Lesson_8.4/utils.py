import random
#from data import questions_data
import sqlite3
from question import Question


def load_questions():
    # Настраиваем подключение к базе данных:
    conn = sqlite3.connect('DATA.db')
    # Настраиваем "курсор", с помощью которого будем обращаться к БД:
    cursor = conn.cursor()
    
    questions = []
    #for question_data in questions_data:
    #    questions.append(Question(
    #        question_data["q"],
    #        int(question_data["d"]),
    #        question_data["a"]
    #    ))
    cursor.execute("SELECT id, question, level, answer FROM questions")
    for line in cursor.fetchall():
        questions.append(Question(
            line[1],
            int(line[2]),
            line[3]
        ))

    random.shuffle(questions)
    return questions


def correct_answers_count(questions):
    correct_counter = 0
    for question in questions:
        if question.is_correct():
            correct_counter += 1
    return correct_counter


def points_count(questions):
    points_counter = 0
    for question in questions:
        if question.is_correct():
            points_counter += question.get_points()
    return points_counter
