from utils import load_random_word


def main():
    
    game_is_on = True
    main_word = load_random_word()

    word = main_word.word
    wordcount = main_word.count_subwords()

    print(f"Составьте {wordcount} слов из слова {word}")

    while game_is_on:
    
        print("Введите слово")
        user_input = input()

        if main_word.has_subwords(user_input):
            print("Слово есть!")
        else:
            print("Слова нет!")


if __name__ == "__main__":
    main()
