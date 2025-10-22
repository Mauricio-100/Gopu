import requests

def run():
    r = requests.get("https://gopuos.onrender.com/status.json")
    data = r.json()
    print("🧠 Introspection GopuOS")
    print(f"CPU: {data['cpu']} | RAM: {data['ram']} | GPU: {data['gpu']}")
    print("Modules:", ", ".join(data["modules"]))
