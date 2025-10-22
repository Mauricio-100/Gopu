import os

def run(args):
    if "--connect" in args:
        idx = args.index("--connect")
        host = args[idx + 1] if len(args) > idx + 1 else ""
        user = "gopu"
        print(f"🔐 Connexion SSH à {user}@{host}")
        os.system(f"ssh {user}@{host}")
    else:
        print("Usage: gopu ssh --connect HOST")
