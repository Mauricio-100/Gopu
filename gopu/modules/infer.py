import requests

BACKEND_URL = "https://Mauricio-100-agent-ai.hf.space/infer"

def run(prompt: str):
    if not prompt:
        print("[Erreur] Aucun prompt fourni")
        return

    payload = {
        "input": prompt,
        "system_prompt": "Tu es Gopu, un agent loyal de Mauricio.",
        "temperature": 0.7,
        "max_new_tokens": 150,
        "top_p": 0.9
    }

    try:
        res = requests.post(BACKEND_URL, json=payload)
        if res.status_code == 200:
            data = res.json()
            print("\n⚡ Réponse Gopu:\n")
            print(data.get("generated_text", res.text))
        else:
            print(f"[Erreur {res.status_code}] {res.text}")
    except Exception as e:
        print(f"[Exception] {e}")
