from utils import load_random_word
from player import Player


def main():
    
    flag = True

    word_and_subwords_tuple = load_random_word()
    subwords_count = load_random_word().subwords_count()
    word = load_random_word().word
    print(subwords_count)
    print(word)
    #subwords_count = word_and_subwords_tuple.subwords_count()

    #print(f"Составьте {wordcount} слов из слова {word}")

    while flag:
    
        username = input("Введите Ваше имя:\n")
        player = Player(username)
        print(f"Здравствуйте, {player.name}!")
        print(f"Составьте {subwords_count} слов из слова {word.upper()}")
        print("Слова должны быть не короче 3 букв")
        print('Чтобы закончить игру, угадайте все слова или введите слово "stop" и нажмите на "Enter"')
        
        print("Введите слово")
        user_input = input()

        if word_and_subwords_tuple.has_subwords(user_input):
            print("Слово есть!")
        else:
            print("Слова нет!")


if __name__ == "__main__":
    main()
