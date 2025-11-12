import controllers as c

def main():
    while True:
        print("""
1) TRIP    1-додати 2-видалити 3-список
2) CLIENT  1-додати 2-видалити 3-список
3) PAYMENT 1-додати 2-видалити 3-список
0) Вихід
""")
        x = input("Меню: ").strip()
        if x == "1":
            y = input("TRIP> ").strip()
            if y == "1": c.trip_add()
            elif y == "2": c.trip_delete()
            elif y == "3": c.trip_list()
        elif x == "2":
            y = input("CLIENT> ").strip()
            if y == "1": c.client_add()
            elif y == "2": c.client_delete()
            elif y == "3": c.client_list()
        elif x == "3":
            y = input("PAYMENT> ").strip()
            if y == "1": c.payment_add()
            elif y == "2": c.payment_delete()
            elif y == "3": c.payment_list()
        elif x == "0":
            break
        else:
            print("Невірно.")

if __name__ == "__main__":
    main()
