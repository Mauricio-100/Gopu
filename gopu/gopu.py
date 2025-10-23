#!/usr/bin/env python3
import sys
from modules import status, infer, token, db, deploy, ssh, github

def main():
    args = sys.argv[1:]
    if not args:
        print("🔧 GopuOS CLI — Agent Terminal")
        print("Usage:")
        print("  gopu status               → Introspection CPU/GPU/modules")
        print("  gopu infer \"prompt\"       → Envoie un prompt à l’IA")
        print("  gopu token --generate     → Crée un token gp_...")
        print("  gopu token --verify TOKEN → Vérifie un token")
        print("  gopu db --test            → Teste la base MySQL")
        print("  gopu deploy ...           → Déploie un VPS ou conteneur")
        print("  gopu ssh ...              → Connexion distante")
        print("  gopu github ...           → Commit/push GitHub")
        return

    cmd = args[0]
    if cmd == "status":
        status.run()
    elif cmd == "infer":
        infer.run(args[1])
    elif cmd == "token":
        token.run(args[1:])
    elif cmd == "db":
        db.run(args[1:])
    elif cmd == "deploy":
        deploy.run(args[1:])
    elif cmd == "ssh":
        ssh.run(args[1:])
    elif cmd == "github":
        github.run(args[1:])
    else:
        print(f"❌ Commande inconnue: {cmd}")

if __name__ == "__main__":
    main()
