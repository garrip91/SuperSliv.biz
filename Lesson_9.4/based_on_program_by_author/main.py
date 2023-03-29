from utils import load_random_word
from player import Player


def main():
    
    flag = True

    while flag:

        word_and_subwords = load_random_word()
        subwords_count = word_and_subwords.subwords_count()
        word = word_and_subwords.word
    
        username = input("Введите Ваше имя:\n")
        player = Player(username)
        print(f"Здравствуйте, {player.name}!")
        print(f"Составьте {subwords_count} слов из слова {word.upper()}")
        
        print(f"ПОДСКАЗКА: {word_and_subwords.sub_words}")

        print("Слова должны быть не короче 3 букв")
        print('Чтобы закончить игру, угадайте все слова или введите слово "stop" и нажмите на "Enter"')
        
        print("Поехали! Ваше первое слово:\n")
        user_input = input()

        if word_and_subwords.has_subword(user_input):
            print("Слово есть!")
        else:
            print("Слова нет!")


if __name__ == "__main__":
    main()
