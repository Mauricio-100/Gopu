import requests

def run(prompt):
    try:
        r = requests.post("https://gopuos.onrender.com/inference", json={"prompt": prompt})
        data = r.json()
        print("🧠 Réponse agentique:")
        print(data["response"])
    except Exception as e:
        print("❌ Erreur d’inférence:", e)
