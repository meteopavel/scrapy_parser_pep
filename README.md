# Асинхронный парсер PEP 
Парсер документов PEP на базе фреймворка Scrapy.

## Основные используемые инструменты
* Python 3.11.5
* Scrapy 2.5.1

## Развёртывание проекта на локальном компьютере
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:meteopavel/scrapy_parser_pep.git
```
Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv
linux: source env/bin/activate
windows: source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

## Использование
```python
scrapy crawl pep
```
Команда запустит асинхронный парсинг документов PEP. Результаты будут сохранены в двух файлах в папке results. Файл pep_ДатаВремя.csv будет содержать номера, названия и статусы всех PEP. Файл  status_summary_ДатаВремя.csv будет содержать сводную информацию о количестве статусов. 

## Автор
[Павел Найденов](https://github.com/meteopavel)