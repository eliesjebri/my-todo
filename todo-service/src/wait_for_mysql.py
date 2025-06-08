import time, socket

while True:
    try:
        s = socket.create_connection(("mysql", 3306), timeout=2)
        print("✅ MySQL est prêt !")
        break
    except Exception:
        print("🕒 En attente de MySQL...")
        time.sleep(2)
