import requests

def run(args):
    if "--generate" in args:
        r = requests.post("https://gopuos.onrender.com/token/generate", json={
            "role": "inference",
            "modules": ["inference", "status"]
        })
        print("🔐 Token généré:", r.json()["token"])
    elif "--verify" in args:
        idx = args.index("--verify")
        token = args[idx + 1] if len(args) > idx + 1 else ""
        r = requests.post("https://gopuos.onrender.com/token/verify", json={"token": token})
        print("🔍 Vérification:", r.json())
    else:
        print("Usage: gopu token --generate | --verify TOKEN")
