import time
import random
import string
import webbrowser
import pyshorteners
import wikipedia

adjectives = ['sleepy', 'slow', 'hot',
              'cold', 'big', 'red',
              'orange', 'yellow', 'green',
              'blue', 'good', 'old',
              'white', 'free', 'brave']
nouns = ['apple', 'dinosaur', 'ball',
         'cat', 'goat', 'red',
         'car', 'duck', 'panda']

adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0, 10000)
special_char = random.choice(string.punctuation)

s = pyshorteners.Shortener()

i = 0
ii = 0
iii = 0


a = input('Выбери язык: RUS, ENG')

if a.lower() == 'rus':
    print("Привет! Добро пожаловать в бета версию пайтон бота Василий!👍")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("🔥UPDATE: Добавлен Тест Животные, а также калькулятор!😎")

    time.sleep(2)
    print("Но перед тем как начать пройди вход в систему!✌️")
    time.sleep(2)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    reg_a = input("Как тебя зовут?")
    reg_b = input("Сколько тебе лет?")
    reg_b = int(reg_b)

    if reg_b > 18:
        print("Ты уже взрослый этот бот создан для детей от 1 до 18 лет. Попробуй еще раз!😡")
    if reg_b <= 18:
        print("Окей, продолжаем!😁, " + reg_a)
        time.sleep(1)
        print('Вот что я умею:')
        time.sleep(0.5)
        while True:
            print('▷ 1. Генератор паролей 🥸')
            print('▷ 2. MEGA OBBY 🤪')
            print('▷ 3. YouTube 🙂')
            print('▷ 4. Не залипни 😳')
            print('▷ 5. Таймер 🤔')
            print('▷ 6. AirPods Pro 😑')
            print('▷ 7. Тест животные 🐯(BETA)')
            print('▷ 8. Калькулятор 😏')
            print('▷ 9. Искать в интернете 💥')
            print('▷ 10. Искать на известных маркетплейсах 😎')
            print('▷ 11. Какая погода в вашем городе? 🥶')
            print('▷ 12. Перевести слово 🤩')
            print('▷ 13. О боте 🤯')
            print('▷ 14. Сокращения ссылок 🤩')
            print('▷ 15. Wikipedia 😑')
            b = input('Что выберешь?')
            b = int(b)

            # Passwords
            if b == 1:
                adjective = random.choice(adjectives)
                noun = random.choice(nouns)
                number = random.randrange(0, 10000)
                special_char = random.choice(string.punctuation)
                password = adjective + noun + str(number) + special_char
                print('Новый пароль: %s' % password)
                time.sleep(1)

            # Mega Obby
            if b == 2:
                webbrowser.open("https://www.roblox.com/games/7788218519/MEGA-OBBY")

            # Youtube
            if b == 3:
                webbrowser.open("https://www.youtube.com/")

            #
            if b == 4:
                webbrowser.open('https://learn.algoritmika.org/laboratory?filter=projects&projectId=20044238')

            #
            if b == 5:
                time_user = int(input("Введите кол-во секунд: "))
                comment = str(input("Введите комментарий: "))
                for q in range(time_user):
                    time.sleep(1)
                    i += 1
                    print("Прошло секунд:", i)
                    if (i % 60) == 0:
                        ii += 1
                        print("Прошло минут:", ii)
                    if (i % 3600) == 0:
                        iii += 1
                        print("Прошло часов:", iii)

                print("Время окончено!")
                print("Ваш комментарий:", comment)
                time.sleep(1)

            #
            if b == 6:
                air = input("Сколько у вас $")
                print("Можно купить:", int(int(air) * 71.62 // 18999), "Наушник(ов) Airpods pro")
                time.sleep(1)
            if b == 7:
                def check_guess(guess, answer):
                    global score
                    still_guessing = True
                    attempt = 0
                    while still_guessing and attempt < 3:
                        if guess.lower() == answer.lower():
                            print('Ответ верный!')
                            score = score + 1
                            still_guessing = False
                        else:
                            if attempt < 2:
                                guess = input('Попробуйте еще раз!')
                            attempt = attempt + 1

                    if attempt == 3:
                        print('Правильный ответ:' + answer)


                score = 0
                print('Тест: Животные🦁')
                guess1 = input('Какой медведь живет за полярным кругом? ')
                check_guess(guess1, 'белый медведь')
                guess2 = input('Какое сухопутное животное самое быстрое? ')
                check_guess(guess2, 'гепард')
                guess3 = input('Какое животное самое большое? ')
                check_guess(guess3, 'синий кит')

                print('Вы набрали очков: ' + str(score) + ' из 3')
                time.sleep(2)
            if b == 8:
                feed1 = float(input('Введите первое число!'))
                feed2 = float(input('Введите второе число!'))
                print('При сложении:', feed1 + feed2)
                print('При вычитании:', feed1 - feed2)
                print('При умножении:', feed1 * feed2)
                print('При дилении:', feed1 / feed2)
                time.sleep(1)
            if b == 9:
                feedback = input('Что ты хочешь искать в интернете?')
                webbrowser.open('https://google.ru/search?q=' + feedback)
            if b == 10:
                feedback1 = input('Что ты хочешь искать на маркетплейсах?')
                webbrowser.open('https://market.yandex.ru/search?text=' + feedback1)
                webbrowser.open('https://www.e-katalog.ru/ek-list.php?search_=' + feedback1)
                webbrowser.open('https://www.ozon.ru/search/?from_global=true&text=' + feedback1)
                webbrowser.open('https://www.wildberries.ru/catalog/0/search.aspx?search=' + feedback1)
            if b == 11:
                feedback2 = input('В каком городе вы живете?')
                webbrowser.open('https://www.accuweather.com/ru/search-locations?query=' + feedback2)
            if b == 12:
                apl = input('Какое слово ты хочешь перевести?')
                webbrowser.open('https://translate.google.com/?hl=ru&sl=ru&tl=en&text=' + apl)
            if b == 13:
                print(
                    'Бот Василий это продвинутый Python бот созданный на платформе алгоритмики. Его создал я Саша, мне 10 лет и я учусь в 4 классе. Сейчас ты находишься в 13 версии бота Василия.')
            if b == 14:
                abra = input('Какую ссылку вы хотите сократить?')
                print("Сокращенная ссылка - ", s.tinyurl.short(abra))
                time.sleep(1)
            if b == 15:
                wikipedia.set_lang('ru')
                hg = input('Что ты хочешь искать на википедии?(Пиши строго на английском языке!)')
                print(wikipedia.summary(hg))
            if b > 15:
                print('Такой программы еще нет😒! Попробуй еще раз!👌')
                time.sleep(1)
#eng

if a.lower() == 'eng':
    print("Hello! Welcome to the beta version of the Python bot Vasily! 👍")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("🔥UPDATE: Added Animal Test and Calculator! 😎")

    time.sleep(2)
    print("But before you start, go through the login! ✌️️")
    time.sleep(2)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    reg_a = input("What's your name?")
    reg_b = input("How old are you?")
    reg_b = int(reg_b)

    if reg_b > 18:
        print("You are already an adult, this bot was created for children from 1 to 18 years old. Try again! 😡")
    if reg_b <= 18:
        print("Ok, let's continue!😁, " + reg_a)
        time.sleep(1)
        print('Here what I can do:')
        time.sleep(0.5)
        while True:
            print('▷ 1. Password generator 🥸')
            print('▷ 2. MEGA OBBY 🤪')
            print('▷ 3. YouTube 🙂')
            print('▷ 4. Dont get stuck 😳')
            print('▷ 5. Timer 🤔')
            print('▷ 6. AirPods Pro 😑')
            print('▷ 7. Test animals 🐯(BETA)')
            print('▷ 8. Calculator 😏')
            print('▷ 9. Search the internet 💥')
            print('▷ 10. Search well-known marketplaces 😎')
            print('▷ 11. What is the weather in your city? 🥶')
            print('▷ 12. Translate word 🤩')
            print('▷ 13. About the bot 🤯')
            print('▷ 14. Link abbreviations 🤩')
            print('▷ 15. Wikipedia 😑')
            b = input('What do you pick?')
            b = int(b)

            # Passwords
            if b == 1:
                adjective = random.choice(adjectives)
                noun = random.choice(nouns)
                number = random.randrange(0, 10000)
                special_char = random.choice(string.punctuation)
                password = adjective + noun + str(number) + special_char
                print('New password: %s' % password)
                time.sleep(1)

            # Mega Obby
            if b == 2:
                webbrowser.open("https://www.roblox.com/games/7788218519/MEGA-OBBY")

            # Youtube
            if b == 3:
                webbrowser.open("https://www.youtube.com/")

            #
            if b == 4:
                webbrowser.open('https://learn.algoritmika.org/laboratory?filter=projects&projectId=20044238')

            #
            if b == 5:
                time_user = int(input("Enter the number of seconds: "))
                comment = str(input("Enter a comment: "))
                for q in range(time_user):
                    time.sleep(1)
                    i += 1
                    print("Seconds elapsed", i)
                    if (i % 60) == 0:
                        ii += 1
                        print("Minutes passed:", ii)
                    if (i % 3600) == 0:
                        iii += 1
                        print("Hours passed:", iii)

                print("Time is up!")
                print("Your comment:", comment)
                time.sleep(1)

            #
            if b == 6:
                air = input("How much $ do you have")
                print("Available for purchase:", int(int(air) * 71.62 // 18999), "earphone(s) Airpods pro")
                time.sleep(1)
            if b == 7:
                def check_guess(guess, answer):
                    global score
                    still_guessing = True
                    attempt = 0
                    while still_guessing and attempt < 3:
                        if guess.lower() == answer.lower():
                            print('The answer is correct!')
                            score = score + 1
                            still_guessing = False
                        else:
                            if attempt < 2:
                                guess = input('Try again!')
                            attempt = attempt + 1

                    if attempt == 3:
                        print('Correct answer:' + answer)


                score = 0
                print('Test: Animals🦁')
                guess1 = input('Which bear lives in the Arctic Circle? ')
                check_guess(guess1, 'polar bear')
                guess2 = input('Which land animal is the fastest? ')
                check_guess(guess2, 'cheetah')
                guess3 = input('Which animal is the largest? ')
                check_guess(guess3, 'blue whale')

                print('You scored points: ' + str(score) + ' из 3')
                time.sleep(2)
            if b == 8:
                feed1 = float(input('Enter the first number!'))
                feed2 = float(input('Enter the second number!'))
                print('On addition:', feed1 + feed2)
                print('When subtracting:', feed1 - feed2)
                print('When multiplying:', feed1 * feed2)
                print('At dilution:', feed1 / feed2)
                time.sleep(1)
            if b == 9:
                feedback = input('What do you want to search the internet?')
                webbrowser.open('https://google.ru/search?q=' + feedback)
            if b == 10:
                feedback1 = input('What do you want to look for on marketplaces?')
                webbrowser.open('https://market.yandex.ru/search?text=' + feedback1)
                webbrowser.open('https://www.e-katalog.ru/ek-list.php?search_=' + feedback1)
                webbrowser.open('https://www.ozon.ru/search/?from_global=true&text=' + feedback1)
                webbrowser.open('https://www.wildberries.ru/catalog/0/search.aspx?search=' + feedback1)
            if b == 11:
                feedback2 = input('What city do you live in?')
                webbrowser.open('https://www.accuweather.com/ru/search-locations?query=' + feedback2)
            if b == 12:
                apl = input('What word do you want to translate?')
                webbrowser.open('https://translate.google.com/?hl=ru&sl=ru&tl=en&text=' + apl)
            if b == 13:
                print('Bot Vasily is an advanced Python bot built on an algorithmic platform. It was created by me Sasha, I am 10 years old and I am in 4th grade. Now you are in version 15 of Vasily bot.')
            if b == 14:
                abra = input('Which link do you want to shorten?')
                print("Abbreviated link -", s.tinyurl.short(abra))
                time.sleep(1)
            if b == 15:
                hg = input('What do you want to search for on Wikipedia? (Write strictly in English!)')
                print(wikipedia.summary(hg))
            if b > 15:
                print('There is no such program yet😒! Try again! 👌')
                time.sleep(1)