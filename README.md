MP3-Analysis
-----
Автор: Чернышев Игорь

-----
Описание
-----
Данное приложение разбирает внутреннее строение mp3-файла и выдает аудио-теги

Запуск
-----
```python mp3_main.py```

Возможности
--
* Разбор тегов id3v1 (содержатся в конце файла, имеют фиксированную длину)
* Разбор тегов id3v2 (содержатся в начале файла, имеют динамическую длину)
* Воспроизведение аудио

Команды консольного интерфейса
--
* ```parse_id3v1``` - получить id3v1 теги
* ```parse_id3v2``` - получить id3v2 теги
* ```play``` - воспроизвести (информация о плеере ниже)
* ```choose_file``` - смена трека

Плеер
--
* При запуске плеера аудио сразу начинает воспроизводиться
* ```pause``` - приостановить воспроизведение
* ```unpause``` - продолжить воспроизведение
* ```volume``` - изменить громкость (значения от 0 до 1 включительно)
* ```set_pos``` - изменить позицию воспроизведения
