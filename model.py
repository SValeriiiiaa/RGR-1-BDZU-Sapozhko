from db import get_cursor


class Model:
    def trip_list(self):
        with get_cursor() as cur:
            cur.execute("SELECT * FROM trip ORDER BY id")
            return cur.fetchall()

    def trip_add(self, title, description, country, price):
        with get_cursor() as cur:
            cur.execute(
                "INSERT INTO trip(title, description, country_code, price) "
                "VALUES (%s, %s, %s, %s)",
                (title, description, country, price),
            )

    def trip_delete(self, id_):
        with get_cursor() as cur:
            cur.execute("DELETE FROM trip WHERE id = %s", (id_,))

    def bookings_by_trip(self, trip_id):
        with get_cursor() as cur:
            cur.execute(
                "SELECT id, client_id, trip_id, date, status "
                "FROM booking WHERE trip_id = %s",
                (trip_id,),
            )
            return cur.fetchall()

    def client_list(self):
        with get_cursor() as cur:
            cur.execute("SELECT * FROM client ORDER BY id")
            return cur.fetchall()

    def client_add(self, name, email, phone, dob):
        with get_cursor() as cur:
            cur.execute(
                "INSERT INTO client(full_name, email, phone_number, date_of_birth) "
                "VALUES (%s, %s, %s, %s)",
                (name, email, phone, dob),
            )

    def client_delete(self, id_):
        with get_cursor() as cur:
            cur.execute("DELETE FROM client WHERE id = %s", (id_,))

    def bookings_by_client(self, client_id):
        with get_cursor() as cur:
            cur.execute(
                "SELECT id, client_id, trip_id, date, status "
                "FROM booking WHERE client_id = %s",
                (client_id,),
            )
            return cur.fetchall()

    def payment_list(self):
        with get_cursor() as cur:
            cur.execute(
                "SELECT booking_id, amount, method, discount "
                "FROM payment ORDER BY booking_id"
            )
            return cur.fetchall()

    def payment_add(self, booking_id, amount, method, discount):
        with get_cursor() as cur:
            cur.execute("SELECT 1 FROM booking WHERE id = %s", (booking_id,))
            if cur.fetchone() is None:
                raise ValueError(f"Бронювання з id={booking_id} не існує.")

            cur.execute(
                "INSERT INTO payment(booking_id, amount, method, discount) "
                "VALUES (%s, %s, %s, %s)",
                (booking_id, amount, method, discount),
            )

    def payment_delete(self, booking_id):
        with get_cursor() as cur:
            cur.execute("DELETE FROM payment WHERE booking_id = %s", (booking_id,))
