## Модуль avgtemp содержит единственную функцию avg_year_city, которая вычисляет среднюю температуру за конкретныйгод в конкретном городе, используя данные из csv формата

## Создание виртуального окружения и его активация 
    
> python3 -m venv .venv

Linux:

> source .venv/bin/activate

Windows:

> .venv\Scripts\activate.bat

## Установка зависимостей

> pip install --editable ".[dev]"

## Запуск утилит

> isort projectname/ 

> black projectname/

> ruff projectname/

> mypy projectname/

## Запуск тестов 

> pytest tests/

