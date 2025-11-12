from db import get_cursor

# --- TRIP ---
def trip_list():
    with get_cursor() as cur:
        cur.execute("SELECT * FROM trip ORDER BY id")
        return cur.fetchall()

def trip_add(title, description, country, price):
    with get_cursor() as cur:
        cur.execute("INSERT INTO trip(title,description,country_code,price) VALUES(%s,%s,%s,%s)",
                    (title, description, country, price))

def trip_delete(id_):
    with get_cursor() as cur:
        cur.execute("DELETE FROM trip WHERE id=%s", (id_,))

# --- CLIENT ---
def client_list():
    with get_cursor() as cur:
        cur.execute("SELECT * FROM client ORDER BY id")
        return cur.fetchall()

def client_add(name, email, phone, dob):
    with get_cursor() as cur:
        cur.execute("INSERT INTO client(full_name,email,phone_number,date_of_birth) VALUES(%s,%s,%s,%s)",
                    (name, email, phone, dob))

def client_delete(id_):
    with get_cursor() as cur:
        cur.execute("DELETE FROM client WHERE id=%s", (id_,))

# --- PAYMENT ---
def payment_list():
    with get_cursor() as cur:
        cur.execute("SELECT booking_id, amount, method, discount FROM payment ORDER BY booking_id")
        return cur.fetchall()

def payment_add(booking_id, amount, method, discount):
    from psycopg import errors

    try:
        with get_cursor() as cur:
            # Перевірка: чи існує такий booking_id
            cur.execute("SELECT 1 FROM booking WHERE id = %s", (booking_id,))
            if cur.fetchone() is None:
                print(f"[ERR] Помилка: бронювання з id={booking_id} не існує.")
                return

            # Якщо існує — додаємо платіж
            cur.execute("""
                INSERT INTO payment(booking_id, amount, method, discount)
                VALUES (%s, %s, %s, %s)
            """, (booking_id, amount, method, discount))
            print("[OK] Платіж успішно додано.")

    except errors.ForeignKeyViolation:
        print(f"[ERR] Неможливо додати платіж — бронювання з id={booking_id} відсутнє.")
    except Exception as e:
        print("[ERR]", e)


def payment_delete(booking_id):
    with get_cursor() as cur:
        cur.execute("DELETE FROM payment WHERE booking_id=%s", (booking_id,))

# --- допоміжні ---
def bookings_by_trip(trip_id):
    with get_cursor() as cur:
        cur.execute("SELECT id, client_id, trip_id, date, status FROM booking WHERE trip_id=%s", (trip_id,))
        return cur.fetchall()

def bookings_by_client(client_id):
    with get_cursor() as cur:
        cur.execute("SELECT id, client_id, trip_id, date, status FROM booking WHERE client_id=%s", (client_id,))
        return cur.fetchall()
