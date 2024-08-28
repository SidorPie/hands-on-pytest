# Запуск автотестов Page Object
## Начало работы
### Настройка виртуального окружения

Windows:
   - cd hands-on-pytest
   - python -m venv selenium_env
   - selenium_env/bin/activate.bat
     
Linux:
   - cd hands-on-pytest
   - python3 -m venv selenium_env
   - source selenium_env/bin/activate

### Установка зависимостей:

   pip install -r requirements.txt

### Запуск тестов:
`pytest -v --tb=line --language=en test_main_page.py`