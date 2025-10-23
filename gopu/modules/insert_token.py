#!/usr/bin/env python3
import secrets
import sys

def run(args=None):
    """
    Gestion des tokens GopuOS :
      --generate         → génère un nouveau token
      --verify <token>   → vérifie un token existant
    """
    if args is None:
        args = sys.argv[1:]

    if not args:
        print("🔐 Usage: gopu token --generate | --verify <token>")
        return

    if "--generate" in args:
        token = f"gp_dev_{secrets.token_hex(16)}"
        print(f"✅ Nouveau token généré : {token}")
        return

    if "--verify" in args:
        try:
            idx = args.index("--verify")
            token = args[idx + 1]
        except (ValueError, IndexError):
            print("❌ Aucun token fourni pour vérification")
            return

        if token.startswith("gp_") and len(token) > 10:
            print(f"🔍 Vérification du token : {token} → ✅ Valide")
        else:
            print(f"🔍 Vérification du token : {token} → ❌ Invalide")
        return

    print("❌ Option inconnue. Utilise --generate ou --verify <token>")
