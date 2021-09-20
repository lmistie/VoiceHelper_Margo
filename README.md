<div align="center">

![Foto](https://github.com/lmistie/VoiceHelper_Margo/blob/main/src/Margo.gif)
</div>

* [Логика проекта](#Project)
* [Команды для Марго](#Commands) 
* [Встречи](#Meetings) 
* [Code review](#Code_review) 
* [Библиотеки](#Libraries)


<h2 align="center"><font size="8px">Логика проекта <a name="Project"></a></font></h2>
В итоге должен получиться масштабный голосовой помощник на всех устройствах(начиная с телефона и ПК заканчивая бытовой техникой для управления домом)

![Foto](https://github.com/lmistie/VoiceHelper_Margo/blob/main/src/scheme.jpeg)

<p align="center"><font size="3px"> Пока весь проект написан с помощью:</font></p>
<div align="center">

![Python](https://img.shields.io/badge/-Python-000000?style=flat-square&logo=python&logoWidth=20)
![Vscode](https://img.shields.io/badge/-VScode-000000?style=flat-square&logo=VisualStudioCode&logoWidth=20&logoColor=blue)
![Vim](https://img.shields.io/badge/-Vim-000000?style=flat-square&logo=vim&logoWidth=20&logoColor=green)
![Notepad++](https://img.shields.io/badge/-Notepad++-000000?style=flat-square&logo=Notepad%2b%2b&logoWidth=20&logoColor=green)
![JetBrains](https://img.shields.io/badge/-JetBrains-000000?style=flat-square&logo=JetBrains&logoWidth=20&logoColor=green)
![iTerm2](https://img.shields.io/badge/-iTerm2-000000?style=flat-square&logo=iTerm2&logoWidth=20)
![PowerShell](https://img.shields.io/badge/-PowerShell-000000?style=flat-square&logo=PowerShell&logoWidth=20)
</div>
<!--<p align="center"><font size="3px">Дальше планируется добавление других языков программирования</font></p>-->

<h5 align="center"><font size="3px">Описание умений и команд голосового помощника Марго<a name="Commands"></a></font></h5>

<div align="center">

| Команды | Работаспасобность |
|:------------:|:------------:|
| Привет | ❌ |
| Пока | ✅ |
| Выключи комп | ✅ |
| Открой Google | ✅ |
| Открой Vkontakte | ✅ |
| Открой Instagram | ✅ |
| Включи YouTube | ✅ |
| Покажи погоду | ✅ |
| Очисти историю| ❌ |
| Покажи файл со статистикой | ❌ |
| Переведи слово | ✅  |
| Открой список команд | ❌ |
| Какие планы | ❌ |
</div>
<br>
<p align="center"><font size="3px">Этапы развития встречи 15.08.21</font></p><a name="Meetings"></a>
<div align="center">

| № | Задачи |
|:---:|:------------:|
| 1️⃣ | Пишем в любом удобном редакторе и под любое ОС |
| 2️⃣ | Придерживаемся станарта PEP 8 по коду в проекте |
| 3️⃣ | Новые фичи добавляем тегами или в новую ветку проекта | 
| 4️⃣ | Первостепенная задача: <br>❗ Правильное распознавание речи голосовым помощником<br>❗ Правильная обработка речи и преобразование речи в запрос |
</div>
<br>
</font></p>

<p align="center">Code review (ММ) от 20.09.2021</p>
 
-  1. Требуется логирование ошибок: @lmistie При каждом запуске создавать в папке logs файл именуемый текущей датой и временем В файл писать все exception, ошибки и логи для удобства дебага/разработки По хорошему создавать два файла, в одном все логи, в другом только errors/exceptions 
-  2. Переделать функцию чтения истории файлов, на данный момент функция неправильно работает с массивами/словарями. На мой взгляд сложная конструкция. Возможно историю запроса нужно писать в csv файл, в котором следующий формат "timestamp";"phrase" @lmistie 
-  3. Подтюнить распознавание речи, на данный момент работает с переменным успехом. @den_mko 
-  4. Попробовать вынести все возможные фразы в отдельный файл(сейчас в коде), например в формате json @lmistie 
-  5. Попробовать собрать venv. Протестировать либы, на виндах и никсах (возможен ли одинаковый venv для различных платформ). Перед запуском питонячего скрипта, необходимо активировать venv: ./venv/scripts/activate @lmistie @den_mko 
-  6. Для ускорения процесса разработки дальнейшего функционала обработки, предлагаю сделать возможность текстового ввода или ввода из файла, чтобы не привязываться только к голосу с кривым, на данный момент, распознаванием
<br>

<p align="center"><font size="3px">Описание библеотек и их назначения</font></p><a name="Libraries"></a>

| Описание библеотек: | Работа в offline-режиме | Требуемые зависимости |
|:-------:|:----------------:|:---------------:|
| Распознавать и синтезировать речь: | ✅ | [pip install PyAudio](https://pypi.org/project/PyAudio/)<br>[pip install pyttsx3](https://pypi.org/project/pyttsx3/)<br>[pip install SpeechRecognition](https://pypi.org/project/SpeechRecognition/)<br>[pip install vosk](https://pypi.org/project/vosk/)|
| Сообщать о прогнозе погоды в любой точке мира: | ❌ | [pip install pyowm](https://pypi.org/project/pyowm/) (OpenWeatherMap) |
| Производить поисковый запрос в поисковой системе Google (а также открывать сами результаты данного запроса) | ❌ | [pip install google](https://pypi.org/project/google/)|
| Производить поисковый запрос видео в системе YouTube | ❌ | Пока нет решения |
| Выполнять поиск определения в Wikipedia c дальнейшим прочтением первых двух предложений | ❌ | [pip install wikipedia-api](https://pypi.org/project/Wikipedia-API/)|
| Переводить фразы с изучаемого языка на родной язык пользователя и наоборот | ❌ | [pip install googletrans](https://pypi.org/project/googletrans/)<br> (Google Translate)|
| Искать человека по имени и фамилии в социальных сетях | ❌ | Пока нет решения |
| «Подбрасывать монетку» | ✅ | Пока нет решения |
| Здороваться и прощаться (после прощания работа приложения завершается) | ✅ | Пока нет решения |
| Менять настройки языка распознавания и синтеза речи на ходу | ✅ | Пока нет решения |