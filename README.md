

<img width="1024" height="1024" alt="IMG_6736" src="https://github.com/user-attachments/assets/ab342bd6-bc26-43ca-be25-0ceafdd6b45b" />
# 🧠 Gopu — OS agentique terminal-native

![Ubuntu](https://img.shields.io/badge/Distro-Ubuntu%2022.04-orange?logo=ubuntu)
![Agentic](https://img.shields.io/badge/Kernel-Agentic%20LLM-blueviolet?logo=codeforces)
![LLM](https://img.shields.io/badge/LLM-T5--small-lightgrey?logo=openai)
![npm](https://img.shields.io/npm/v/gopu?color=red&logo=npm)
![Secure](https://img.shields.io/badge/Security-Sandboxed%20VM2-critical?logo=vercel)
![Terminal](https://img.shields.io/badge/Interface-Terminal--native-222222?logo=gnubash)
# ⚡ GopuOS — Agentic CLI

**GopuOS** est un terminal agentique minimaliste, écrit en Python pur (stdlib only), conçu pour orchestrer vos déploiements, gérer vos dépôts GitHub et interagir avec un backend d’inférence Hugging Face.

---

## ✨ Caractéristiques

- 🌀 **Zéro dépendance externe** : uniquement la bibliothèque standard Python (`configparser`, `subprocess`, `json`).
- 🔑 **Gestion de tokens GitHub** via `gopu.conf.ini`.
- 🚀 **Déploiement automatisé** sur VPS (SSH + Docker).
- 🤖 **Inference API** : dialogue avec votre agent Gopu via Hugging Face Spaces.
- 📦 **Commandes Git intégrées** : clone, push, pull, branch, checkout, config.

---


## ⚙️ Installation

Depuis PyPI :

```bash
pip install gopu
```

Depuis les sources :
```
git clone https://github.com/Mauricio-100/Gopu.git
cd gopuos-agent
pip install -e .
```

---

🖥️ Utilisation
```
gopu
```

Affiche l’aide :

.... GopuOS CLI ... Agent Terminal ....
Usage:
  gopu status
  gopu infer "prompt"
  gopu token --generate
  gopu token --verify TOKEN
  gopu db --test
  gopu deploy ...
  gopu ssh ...
  gopu github ...


Exemple : Inference

gopu infer "Bonjour Gopu, qui es-tu ?"


Exemple : GitHub avec token

gopu github clone
gopu github push


(le token est lu automatiquement depuis [github] token dans gopu.conf.ini)

Exemple : Déploiement

gopu deploy


---

🔧 Configuration

Fichier gopu.conf.ini :
```
[vps]
host = vps.gopuos.net
user = gopu
port = 22

[repo]
url = https://github.com/ceose/gopuos-agent.git
branch = main

[github]
token = ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

🛠️ Développement

Construire et publier :

python3 -m build
python3 -m twine upload dist/*


---

📜 Licence

MIT — libre à vous de forker, modifier et contribuer.

---

🌌 Vision

GopuOS n’est pas qu’un simple CLI.
C’est un agent terminal : un compagnon minimaliste, introspectif et extensible, pensé pour évoluer avec vos besoins.
Chaque commande est un module agentique que vous pouvez enrichir, refactoriser et styliser.
