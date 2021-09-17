# импортирование библиотек
import speech_recognition as sr
import os
import sys
import webbrowser
import random
import pyttsx3
from tkinter import *
import pandas as pd
from fuzzywuzzy import fuzz
import time
from datetime import datetime
from colorama import *

# Глобальные переменные
text = '' # Весь текст
r = sr.Recognizer() # Микрофон на устройсте, который слушает речь
engine = pyttsx3.init(); # Движок
adr = '' # Google браузер
i = 0 # для счетчика
task_number = 0


def speak(words):
    print(words)
    os.system("say " + words)


# Словарь приветствия Марго
name_voice = ['марго', 'маргорита', 'рита', 'ритка', 'маргунка', 'подруга' ,'не могла бы ты', 'пожалуйста', 'сделай услугу', 'покажи ка','покажи ']
# Словарь возможных команд (должно быть много пока без ИИ)
command = ['привет','здорова','выключи компьютер','выключи комп','включи youtube','открой браузер','открой google','открой список команд','какие команды ты знаешь','открой vk','открой instagram','открой stackoverflow','покажи погоду','какая сейчас погода','покажи погоду на завтра','очисти файл','очисти файл статистики','покажи статистику','покажи файл со статистикой','покажи файл статистики','покажи стату','какие планы','пока','до встречи','еще увидимся','до скорого','хорошего дня','хорошего вечера']

# Раздел функций с описанием команд Марго(Почитайте про Append и как работает библиотека pandas [53 строка pd.DataFrame] !!!!! )

# История запросов
def history():
    z = {}
    arr = {}
    arr2 = {}
    arr3 = {}
    arr4 = {}
    file = open('history.txt', 'r', encoding = 'UTF-8')
    case = file.readlines()
    for i in range(len(case)):
        line = str(case[i].replace('\n','').strip())
        arr.dict(line)
    file.close()
    for i in range(len(arr)):
        x = arr[i]
        if x in z:
            z[x] += 1
        if not(x in z):
            b = {x : 1}
            z.update(b)
        if not(x in arr2):
            arr2.append(x)
    for i in arr2:
        arr3.append(z[i])
    for i in range(1, len(arr3)+1):
        arr4.append(str(i)+') ')
    list = pd.DataFrame({
        'command' : arr2,
        'count' : arr3
    }, index = arr4)
    list.index.name = '№'
    print(list)

# Планы на проект Марго 1.0
def plane():
    global engine
    plane = '''Привет, я ваш голосовой помощник. Иногда я торможу, потому что я еще в разработке. В будующем я планирую быть конкурентом и возможно ассистентом вашего умного дома. Начиная от вашей технике, заканчивая вашим автомобилем и бытовой техникой. Пока еще у меня не было нормальных тестов, так что не ругайтесь, я все еще учусь.'''
    engine.say(plane)

# Очистка файла со статистикой
def clear_static():
    global engine
    file = open('history.txt', 'w', encoding= 'UTF-8') # "w" - Запись - Открывает файл для записи, создает файл, если он не существует
    file.close()
    engine.say('Ваш файл со статистикой очищен!')

# Добавляем запросы в статистику
def write_file(op):
    file = open('history.txt', 'a', encoding= 'UTF-8') # 'a' - Добавить - Открывает файл для добавления, создает файл, если он не существует
    if op != '':
        file.write(op+'\n')
    file.close()

# Проверка на самый подходящий запрос функций(Почитайте про ratio и fuzzywuzzy)
def check(qwe):
    global command, i, write_file
    answer = ''
    for i in range(len(command)):
        case = fuzz.ratio(qwe,command[i])
        if (case > 50) & (case > i):
            answer = command[i]
            i = case
    if (answer != 'пока') & (answer != 'привет'):
        write_file(answer)
    return(str(answer))

# Работаем по поискам веб-сайтов, пускай пока будет Google
def web_browser():
    global adr
    webbrowser.open('https://www.google.com'.format(adr))

# Проверка на поиск в интернете
def check_browser_searching():
    global text, wifi_name, write_file
    global adr
    global web_browser
    if 'найди' in text:
        write_file('найди')
        adr = text.replace('найди','').strip()
        text = text.replace(adr,'').strip()
        check_browser_searching()
        text = ''
    elif 'найти' in text:
        write_file('найти')
        adr = text.replace('найти','').strip()
        text = text.replace(adr,'').strip()
        check_browser_searching()
        text = ''
    adr = ''

# Избавляемся от наших ключевых слов
def clear_keywords():
    global text, name_voice
    for i in name_voice:
        text = text.replace(i,'').strip()
        text = text.replace('  ',' ').strip()

# Приветствие 
def hello_margo():
    global engine
    hello = ['Привет, я ваш голосовой помощник. Иногда я торможу. Я еще в разработке. Ну что приступим?','Привет','Я рада вас снова слышать','Приветствую мой повелитель','Вечер в хату','Привет, чем могу быть полезна?','Да, я вас слушаю','Чем могу помочь?']
    z = random.choices(hello)
    engine.say(z)

# Выход из программы
def exit():
    global engine
    gb = ['хорошо, до новых встреч, пока','хорошо, до встечи','всего наилучшего','Была рада вам помочь','всегда к вашим услугам, Марго','до новых встреч мой господин']
    engine.say(random.choices(gb))
    engine.runAndWait();
    engine.stop();
    os.system('clear') # ИЛИ clear
    exit(0)

# Показ набор команд голосового ассистента
def list_cmd():
    my_commands = ['привет','выключи компьютер','включи youtube','открой браузер','какая сейчас погода','покажи файл статистик','переведи']
    for i in my_commands:
        print(i)
    time.sleep(2)

# Открываем браузер
def browser():
    webbrowser.open('https://www.google.com')

# Открываем Ютуб
def youtube():
    webbrowser.open('https://www.youtube.com')

# Оправляем ПК спать
def shutdown():
    global exit
    os.system('shutdown \s \f \t 15')
    exit()

# Погода
def weather():
    webbrowser.open('https://yandex.ru/pogoda')

# Открываем Vk
def vk():
    webbrowser.open('https://www.vk.com')

# Открываем Instagram
def instagram():
    webbrowser.open('https://www.instagram.com')

# Открываем StackOverflow
def stackover():
    webbrowser.open('https://ru.stackoverflow.com/')

# Перевод слов и текста
'''def translete():
    global text, ind
    ind = 0
    var = [' ка','переведи пожалуйста','перевод','переводить','переведи']
    for i in var:
        if (i in text)&(ind == 0):
            word = text
            word = word.replace('переведи','').strip()
            word = word.replace('перевести','').strip()
            word = word.replace('перевод','').strip()
            word = word.replace('переведи ка','').strip()
            word = word.replace('переведи пожалуйста','').strip()
            word = word.replace('слова','').strip()
            word = word.replace('слово','').strip()
            webbrowser.open('https://translate.yandex.ru/'.format(word))
            ind = 1
            text = ''
'''

cmds = {
    'Привет' : hello_margo,                  'здорова' : hello_margo,                 'выключи компьютер' : shutdown,
    'выключи комп' : shutdown,               'включи youtube' : youtube,              'открой браузер' : web_browser,
    'открой google' : web_browser,           'открой список команд' : list_cmd,       'какие команды ты знаешь' : list_cmd,
    'открой vk' : vk,                        'открой instagram' : instagram,          'открой stackoverflow' : stackover,
    'покажи погоду' : weather,               'какая сейчас погода' : weather,         'покажи погоду на завтра' : weather,
    'очисти файл' : clear_static,            'очисти файл статистики' : clear_static, 'покажи статистику' : clear_static,
    'покажи файл со статистикой' : history,  'покажи файл статистики' : history,      'покажи стату' : history,
    ''' 'переведи' : translete,                  'переведи пожалуйста' : translete,'''       'какие планы' : plane,
    'пока' : exit,                           'до встречи' : exit,                     'еще увидимся' : exit,
    'до скорого' : exit,                     'хорошего дня' : exit,                   'хорошего вечера' : exit,
    'добрый день' : hello_margo,             'добрый вечер' : hello_margo,            'привет марго' : hello_margo,
}


# распознавание речи
def talk():
    global text, clear_keywords
    text = ''
    with sr.Microphone() as source:
        print('Я вас слушаю: ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=3)
        try:
            text = (r.recognize_google(audio, language="ru-RU")).lower()
        except(sr.UnknownValueError):
            pass
        except(TypeError):
            pass
        except (sr.UnknownValueError):
            speak("Я вас не поняла")
        os.system('clear')
        #lb['text'] = text # Это для окна приложения в будущем через tkinter
        clear_keywords()

# Поехали
def cmd_start():
    global cmds, engine, check, check_browser_searching, task_number, text #ld
    check_browser_searching()
    text = check(text)
    print(text)
    check_browser_searching()
    if (text in cmds):
        if (text != 'привет')&(text != 'пока')&(text != 'открой список команд'):
            case = ['Секундочку','Сейчас','Вот ваш результат','Выполняю',]
            engine.say(random.choices(case))
        cmds[text]()
    elif text == '':
        pass
    task_number += 1
    if (task_number % 10 == 0):
        engine.say('Что-нибудь еще?')
        engine.runAndWait()
        engine.stop()

# Основной бесконечный цикл
def main():
    global text, talk, cmd_start, i
    try:
        talk()
        if text != '':
            cmd_start()
            i = 0
    except(UnboundLocalError):
        pass
    except(TypeError):
        pass

while True:
    main()