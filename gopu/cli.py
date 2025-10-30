#!/usr/bin/env python3
import sys
from gopu.modules import status, infer, token, db, deploy, ssh, github

def main():
    args = sys.argv[1:]
    if not args:
        print(".... GopuOS CLI ... Agent Terminal ....")
        print("Usage:")
        print("  gopu status               ... Infos système")
        print("  gopu infer \"prompt\"       ... Interroger Gopu")
        print("  gopu token --generate     ... Créer un token")
        print("  gopu token --verify TOKEN ... Vérifier un token")
        print("  gopu db --test            ... Tester la DB")
        print("  gopu deploy ...           ... Déployer sur VPS")
        print("  gopu ssh ...              ... Connexion SSH")
        print("  gopu github ...           ... Commandes GitHub")
        return

    cmd = args[0]
    if cmd == "status":
        status.run()
    elif cmd == "infer":
        infer.run(args[1] if len(args) > 1 else "")
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
        print(f"... Commande inconnue: {cmd}")

if __name__ == "__main__":
    main()
