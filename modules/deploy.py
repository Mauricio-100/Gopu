import yaml
import subprocess
import os

def run(args):
    try:
        with open("/usr/bin/gopu/gopu.conf.yml", "r") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        print("❌ Impossible de lire gopu.conf.yml:", e)
        return

    host = config["vps"]["host"]
    user = config["vps"]["user"]
    port = config["vps"]["port"]
    repo = config["repo"]["url"]
    branch = config["repo"]["branch"]

    print(f"🚀 Déploiement sur {user}@{host}:{port}")
    ssh_cmd = f"ssh {user}@{host} -p {port}"
    clone_cmd = f"{ssh_cmd} 'git clone -b {branch} {repo} ~/gopuos && cd ~/gopuos && docker build -t gopuos . && docker run -d -p 8080:8080 gopuos'"

    try:
        subprocess.run(clone_cmd, shell=True, check=True)
        print("✅ Déploiement terminé")
    except subprocess.CalledProcessError as e:
        print("❌ Échec du déploiement:", e)
