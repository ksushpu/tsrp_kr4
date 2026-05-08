# Контрольная работа №4

## Установка и запуск

```bash
# Установка зависимостей
pip install -r requirements.txt

# Копирование .env
cp .env.example .env

# Запуск приложения
uvicorn app.main:app --reload