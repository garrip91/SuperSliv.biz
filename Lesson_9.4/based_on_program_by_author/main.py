from utils import load_random_word
from player import Player


def main():
    
    correct_counter = 0
    flag = True

    while flag:

        word_and_subwords = load_random_word()
        subwords_count = word_and_subwords.subwords_count()
        word = word_and_subwords.word
    
        username = input("Введите Ваше имя:\n")
        player = Player(username)
        print(f"Здравствуйте, {player.name}!")
        print(f"Составьте {subwords_count} слов из слова {word.upper()}")
        
        #print(f"ПОДСКАЗКА: {word_and_subwords.sub_words}")

        print("Слова должны быть не короче 3 букв")
        print('Чтобы закончить игру, угадайте все слова или В ПРОЦЕССЕ ИГРЫ введите слово "stop" (или "стоп") и нажмите на "Enter"')
        
        print("Поехали! Ваше первое слово:\n")

        while correct_counter < len(word_and_subwords.sub_words):
            user_input = input()
            if (user_input == "stop") or (user_input == "стоп"):
                flag = False
                break
            elif len(user_input) < 3:
                print("Слишком короткое слово!")
            else:
                if player.has_used(user_input):
                    print("Уже использовано!")
                else:
                    if word_and_subwords.has_subword(user_input):
                        print("Верно!")
                        correct_counter += 1
                    else:
                        print("Неверно!")
                    player.add_word(user_input)
        flag = False
    
    print(f"Игра завершена, Вы угадали {correct_counter} слов!")


if __name__ == "__main__":
    main()
