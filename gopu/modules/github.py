import subprocess

def run(args):
    if not args:
        print("📦 GopuOS Git Agent — commandes disponibles :")
        print("  gopu github clone REPO_URL")
        print("  gopu github init")
        print("  gopu github status")
        print("  gopu github add FILE")
        print("  gopu github commit -m 'message'")
        print("  gopu github push")
        print("  gopu github pull")
        print("  gopu github branch [name]")
        print("  gopu github checkout BRANCH")
        print("  gopu github log")
        print("  gopu github config --name NAME --email EMAIL")
        print("  gopu github remote [add name url]")
        return

    cmd = args[0]

    if cmd == "clone" and len(args) > 1:
        subprocess.run(f"git clone {args[1]}", shell=True)

    elif cmd == "init":
        subprocess.run("git init", shell=True)

    elif cmd == "status":
        subprocess.run("git status", shell=True)

    elif cmd == "add" and len(args) > 1:
        subprocess.run(f"git add {args[1]}", shell=True)

    elif cmd == "commit" and "-m" in args:
        idx = args.index("-m")
        message = args[idx + 1] if len(args) > idx + 1 else "update"
        subprocess.run(f"git commit -m \"{message}\"", shell=True)

    elif cmd == "push":
        subprocess.run("git push", shell=True)

    elif cmd == "pull":
        subprocess.run("git pull", shell=True)

    elif cmd == "branch":
        if len(args) > 1:
            subprocess.run(f"git branch {args[1]}", shell=True)
        else:
            subprocess.run("git branch", shell=True)

    elif cmd == "checkout" and len(args) > 1:
        subprocess.run(f"git checkout {args[1]}", shell=True)

    elif cmd == "log":
        subprocess.run("git log --oneline --graph --decorate", shell=True)

    elif cmd == "config":
        if "--name" in args:
            name = args[args.index("--name") + 1]
            subprocess.run(f"git config --global user.name \"{name}\"", shell=True)
        if "--email" in args:
            email = args[args.index("--email") + 1]
            subprocess.run(f"git config --global user.email \"{email}\"", shell=True)

    elif cmd == "remote":
        if len(args) > 2 and args[1] == "add":
            subprocess.run(f"git remote add {args[2]} {args[3]}", shell=True)
        else:
            subprocess.run("git remote -v", shell=True)

    else:
        print(f"❌ Commande inconnue: {' '.join(args)}")
