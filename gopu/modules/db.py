import requests

def run(args):
    if "--test" in args:
        try:
            r = requests.get("https://gopuos.onrender.com/db-test")
            print("🗄️ Test MySQL:", r.json()["mysql_time"])
        except Exception as e:
            print("❌ Erreur MySQL:", e)
    else:
        print("Usage: gopu db --test")
