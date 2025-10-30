import subprocess
import configparser
import os
import shlex

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CONF_PATH = os.path.join(BASE_DIR, "gopu.conf.ini")

conf = configparser.ConfigParser()
conf.read(CONF_PATH)

REPO_URL = conf.get("repo", "url", fallback=None)
REPO_BRANCH = conf.get("repo", "branch", fallback="main")
GITHUB_TOKEN = conf.get("github", "token", fallback=None)

def run_cmd(cmd: str):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Commande échouée: {cmd}\n{e}")

def inject_token(url: str) -> str:
    if not url or not url.startswith("https://"):
        return url
    if GITHUB_TOKEN:
        return url.replace("https://", f"https://{GITHUB_TOKEN}@")
    return url

def set_remote_with_token(remote_name: str = "origin"):
    if not GITHUB_TOKEN:
        return
    try:
        res = subprocess.run(
            ["git", "remote", "get-url", remote_name],
            check=True, capture_output=True, text=True
        )
        current_url = res.stdout.strip()
    except subprocess.CalledProcessError:
        if REPO_URL:
            url_with_token = inject_token(REPO_URL)
            run_cmd(f"git remote add {shlex.quote(remote_name)} {shlex.quote(url_with_token)}")
        return
    url_with_token = inject_token(current_url)
    if url_with_token != current_url:
        run_cmd(f"git remote set-url {shlex.quote(remote_name)} {shlex.quote(url_with_token)}")

def usage():
    print("📦 GopuOS Git Agent — commandes disponibles :")
    print("  gopu github clone [REPO_URL]")
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
    print("  gopu github remote [add name url] | [set-url name url] | [show]")

def run(args):
    if not args:
        usage()
        return

    cmd = args[0]

    if cmd == "clone":
        url = args[1] if len(args) > 1 else REPO_URL
        if not url:
            print("❌ Aucun REPO_URL fourni ni trouvé dans gopu.conf.ini")
            return
        url = inject_token(url)
        run_cmd(f"git clone -b {shlex.quote(REPO_BRANCH)} {shlex.quote(url)}")

    elif cmd == "init":
        run_cmd("git init")

    elif cmd == "status":
        run_cmd("git status")

    elif cmd == "add":
        if len(args) > 1:
            run_cmd(f"git add {shlex.quote(args[1])}")
        else:
            print("❌ Spécifie un fichier: gopu github add FILE")

    elif cmd == "commit":
        if "-m" in args:
            idx = args.index("-m")
            message = args[idx + 1] if len(args) > idx + 1 else "update"
            run_cmd(f'git commit -m {shlex.quote(message)}')
        else:
            print("❌ Utilise: gopu github commit -m 'message'")

    elif cmd == "push":
        set_remote_with_token()
        run_cmd("git push")

    elif cmd == "pull":
        set_remote_with_token()
        run_cmd("git pull")

    elif cmd == "branch":
        if len(args) > 1:
            run_cmd(f"git branch {shlex.quote(args[1])}")
        else:
            run_cmd("git branch")

    elif cmd == "checkout":
        if len(args) > 1:
            run_cmd(f"git checkout {shlex.quote(args[1])}")
        else:
            print("❌ Spécifie une branche: gopu github checkout BRANCH")

    elif cmd == "log":
        run_cmd("git log --oneline --graph --decorate")

    elif cmd == "config":
        if "--name" in args:
            name = args[args.index("--name") + 1]
            run_cmd(f'git config --global user.name {shlex.quote(name)}')
        if "--email" in args:
            email = args[args.index("--email") + 1]
            run_cmd(f'git config --global user.email {shlex.quote(email
