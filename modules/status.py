import requests

def run():
    try:
        r = requests.get("https://gopuos.onrender.com/status.json")
        data = r.json()
        print("🧠 Introspection GopuOS")
        print(f"CPU: {data['cpu']} | RAM: {data['ram']} | GPU: {data['gpu']}")
        print("Modules:", ", ".join(data["modules"]))
    except Exception as e:
        print("❌ Erreur de connexion au backend:", e)
