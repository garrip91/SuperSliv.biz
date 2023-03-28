from utils import load_random_word


def main():
    
    main_word = load_random_word()

    while game_is_on:
    
        print("Введите слово")
        user_input = input()

        if main_word.has_subword(user_input):
            print("Слово есть!")
        else:
            print("Слова нет!")


if __name__ == "__main__":
    main()
