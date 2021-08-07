# BETA ВЕРСИЯ ГОЛОСОВОГО ПОМОЩНИКА МАРГО V 1.0

# импортирование библиотек
import speech_recognition as sr
import os
import sys
import webbrowser

def talk(words):
    print(words)
    os.system("say " + words)

talk("Привет, я ваш голосовой помощник. Иногда я торможу, потому что я еще в разработке. Ну что приступим?")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        tz = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали " + tz)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        tz = command()

    return tz

def makeSomething(tz):
    if 'открой google' in tz:
        talk("Секундочку")
        url_0 = 'https://www.google.com'
        webbrowser.open(url_0)
    elif 'открой яндекс' in tz:
        talk("Секундочку")
        url_1 = 'https://yandex.ru/'
        webbrowser.open(url_1)
    elif 'как тебя зовут' in tz:
        talk("Меня зовут Марго")
    elif 'что ты умеешь делать' in tz:
        talk("Пока я могу назвать свое имя и открывать веб-сайты")
    elif 'марго' in tz:
        talk("Я вас слушаю, говорите")
    elif 'спасибо стоп' in tz:
        talk("Хорошо, до новых встреч, пока")
        sys.exit()

while True:
    makeSomething(command())