import subprocess
import sys
from app.database import engine, SessionLocal
from app.models import Product

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Ошибки:", result.stderr)
    return result.returncode == 0

def init_alembic():
    print("=== Инициализация Alembic ===")
    if run_command("alembic init migrations"):
        print("Alembic инициализирован. Замените migrations/env.py на наш код.")
    else:
        print("Возможно, migrations уже существует.")

def generate_initial_migration():
    print("=== Генерация начальной миграции ===")
    run_command('alembic revision --autogenerate -m "Initial: create products table"')

def apply_migrations():
    print("=== Применение миграций ===")
    run_command("alembic upgrade head")

def add_test_data():
    print("=== Добавление тестовых данных ===")
    db = SessionLocal()
    products = [
        Product(title="Ноутбук", price=99999.99, count=10, description="Игровой ноутбук"),
        Product(title="Мышь", price=2999.99, count=50, description="Беспроводная мышь")
    ]
    db.add_all(products)
    db.commit()
    db.close()
    print("Добавлено 2 продукта")

def generate_description_migration():
    print("=== Генерация миграции для description ===")
    run_command('alembic revision --autogenerate -m "Add description field"')

def verify():
    print("=== Проверка ===")
    db = SessionLocal()
    products = db.query(Product).all()
    print(f"Продуктов в БД: {len(products)}")
    for p in products:
        print(f"  {p.id}: {p.title} - {p.description}")
    db.close()

if __name__ == "__main__":
    commands = {
        "init": init_alembic,
        "generate": generate_initial_migration,
        "migrate": apply_migrations,
        "add-data": add_test_data,
        "generate-desc": generate_description_migration,
        "verify": verify,
        "full": lambda: [
            generate_initial_migration(),
            apply_migrations(),
            add_test_data(),
            generate_description_migration(),
            apply_migrations(),
            verify()
        ]
    }
    
    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("Использование: python task_9_1.py [команда]")
        for cmd in commands:
            print(f"  {cmd}")
    else:
        commands[sys.argv[1]]()