import models as m
from psycopg import errors

# --- TRIP ---
def trip_list():
    for r in m.trip_list():
        print(r)

def trip_add():
    try:
        t = input("Назва: ")
        d = input("Опис: ")
        c = input("Код країни: ").upper()
        p = float(input("Ціна: "))
        m.trip_add(t, d, c, p)
        print("[OK] Додано")
    except Exception as e:
        print("[ERR]", e)

def trip_delete():
    try:
        i = int(input("ID для видалення: "))
        try:
            m.trip_delete(i)
            print("[OK] Видалено")
        except errors.ForeignKeyViolation as fk:
            print("[ERR] Неможливо видалити: є залежні booking.")
            for r in m.bookings_by_trip(i):
                print("   ", r)
    except Exception as e:
        print("[ERR]", e)

# --- CLIENT ---
def client_list():
    for r in m.client_list():
        print(r)

def client_add():
    try:
        n = input("ПІБ: ")
        e = input("Email: ")
        p = input("Телефон: ")
        d = input("Дата народження (YYYY-MM-DD): ")
        m.client_add(n, e, p, d)
        print("[OK] Додано")
    except Exception as e:
        print("[ERR]", e)

def client_delete():
    try:
        i = int(input("ID для видалення: "))
        try:
            m.client_delete(i)
            print("[OK] Видалено")
        except errors.ForeignKeyViolation as fk:
            print("[ERR] Неможливо видалити: є залежні booking.")
            for r in m.bookings_by_client(i):
                print("   ", r)
    except Exception as e:
        print("[ERR]", e)

# --- PAYMENT ---
def payment_list():
    for r in m.payment_list():
        print(r)

def payment_add():
    try:
        b = int(input("booking_id (має існувати): "))
        a = float(input("Сума: "))
        mth = input("Метод: ")
        d = float(input("Знижка: "))
        try:
            m.payment_add(b, a, mth, d)
            print("[OK] Додано")
        except errors.ForeignKeyViolation:
            print("[ERR] Немає такого booking_id — вставка неможлива.")
    except Exception as e:
        print("[ERR]", e)

def payment_delete():
    try:
        b = int(input("booking_id для видалення: "))
        m.payment_delete(b)
        print("[OK] Видалено")
    except Exception as e:
        print("[ERR]", e)
