<div align="center">

* [Проект](#Project)
* [Команды](#Commands) 
* [Встречи](#Meetings) 
* [Code review](#Code_review) 
* [Библиотеки](#Libraries)
</div>
<div align="center">

![Foto](https://github.com/lmistie/VoiceHelper_Margo/blob/main/src/logo.gif)
</div>

<h2 align="center"><font size="8px">Голосовой помощник</font></h2>


### Суть проекта <a name="Project"></a>
В итоге должен получиться масштабный голосовой помощник на всех устройствах(начиная с телефона и ПК заканчивая бытовой техникой для управления домом)
![Foto](https://github.com/lmistie/VoiceHelper_Margo/blob/main/src/scheme.jpeg)

<p align="center"><font size="3px"> Пока весь проект написан на</font></p>
<div align="center">

![Python](https://img.shields.io/badge/-python-000000?style=flat-square&logo=python&logoColor=violet&logoWidth=20)
</div>
<p align="center"><font size="3px">Дальше планируется добавление других языков программирования</font></p><a name="Commands"></a>

<h5 align="center"><font size="3px">Описание умений и команд голосового помощника Марго</font></h5>

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