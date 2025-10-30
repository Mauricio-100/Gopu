import subprocess
import os
import configparser

def run(args):
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "..", "..", "gopu.conf.ini")

    try:
        config.read(config_path)
        host = config["vps"]["host"]
        user = config["vps"]["user"]
        port = config["vps"]["port"]
        repo = config["repo"]["url"]
        branch = config["repo"]["branch"]
    except Exception as e:
        print("❌ Impossible de lire gopu.conf.ini:", e)
        return

    print(f"🚀 Déploiement sur {user}@{host}:{port}")
    ssh_cmd = f"ssh {user}@{host} -p {port}"
    clone_cmd = (
        f"{ssh_cmd} 'git clone -b {branch} {repo} ~/gopuos "
        f"&& cd ~/gopuos "
        f"&& docker build -t gopuos . "
        f"&& docker run -d -p 8080:8080 gopuos'"
    )

    try:
        subprocess.run(clone_cmd, shell=True, check=True)
        print("✅ Déploiement terminé")
    except subprocess.CalledProcessError as e:
        print("❌ Échec du déploiement:", e)
