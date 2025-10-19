

![Logo Gopu](./assets/logo.svg)
# 🧠 Gopu — OS agentique terminal-native
![Linux](https://img.shields.io/badge/Platform-Linux-only-green?logo=linux)
![Ubuntu](https://img.shields.io/badge/Distro-Ubuntu%2022.04-orange?logo=ubuntu)
![Agentic](https://img.shields.io/badge/Kernel-Agentic%20LLM-blueviolet?logo=codeforces)
![LLM](https://img.shields.io/badge/LLM-T5--small-lightgrey?logo=openai)
![npm](https://img.shields.io/npm/v/gopu?color=red&logo=npm)
![Secure](https://img.shields.io/badge/Security-Sandboxed%20VM2-critical?logo=vercel)
![Terminal](https://img.shields.io/badge/Interface-Terminal--native-222222?logo=gnubash)


**Gopu** est un système d’exploitation modulaire, intelligent et exclusivement Linux, conçu pour les environnements de terminal comme Termux, Ubuntu, Replit, et autres distributions Linux. Il est piloté par un modèle LLM local (`t5-small`) qui agit comme noyau agentique : il contrôle, optimise et fait évoluer tous les modules.

Gopu n’est pas un assistant. C’est un **cerveau de production**, conçu pour orchestrer des flux, simuler des architectures, et paralléliser des calculs dans un environnement sécurisé et introspectif.

---

## ⚙️ Fonctionnalités principales

- 🧠 **Contrôleur LLM intégré** — Modèle `t5-small` avec accès total à tous les modules
- 💻 **Exclusivement Linux** — Refus automatique sur Windows/macOS
- 🔗 **Architecture modulaire** — GPU, CPU, VM, émulateurs, monitoring, simulation hardware
- 🔁 **Orchestration intelligente** — Chaine les modules GPU → CPU → VM → Émulateur
- 📊 **Profilage des performances** — CPU, GPU, mémoire, temps d’exécution
- 🌐 **Multilingue** — Interprétation et affichage en plusieurs langues
- 🔒 **Exécution sécurisée** — Sandbox VM2, vérification stricte de l’environnement

---

## 📁 Structure du projet



gopu/ ├── src/ │   ├── index.js              # Point d’entrée CLI │   ├── orchestrator.js       # Orchestration des modules │   ├── agent/ │   │   └── llm.js            # Modèle LLM (t5-small) avec rôle et accès │   ├── modules/ │   │   ├── gpu.js            # Calcul GPU (gpu.js, tfjs-node-gpu) │   │   ├── cpu.js            # Parallélisme CPU (piscina, threads.js) │   │   ├── emulator.js       # Émulation (riscv, arm, x86, etc.) │   │   ├── vm.js             # Machines virtuelles (vm2, virtual-machine) │   ├── utils/ │   │   ├── logger.js         # Affichage stylisé (chalk) │   │   ├── profiler.js       # Analyse des performances ├── package.json              # Dépendances et configuration npm ├── README.md                 # Documentation ├── logo.svg                  # Logo Gopu ├── .github/ │   └── workflow/ │       └── ci.yml            # Pipeline CI/CD


---

## 🚀 Installation

```bash
npm install -g gopu
```

---

🧠 Commandes CLI

Commande	Description
--help	Affiche la liste des commandes	
--debug	Informations système, user_id, distribution	
--version	Affiche la version actuelle	
cpu	Lance la simulation CPU	
gpu	Lance le calcul GPU	
emulate	Lance l’émulateur (RISC-V, ARM, etc.)	
vm	Lance une machine virtuelle	
--strict	Refuse les environnements non-Linux	
--lang [xx]	Affichage multilingue	
--chain	Orchestration intelligente des modules	
--profile	Analyse des performances	
--extend	Création dynamique de modules	


---

🧠 Rôle du modèle LLM

Le modèle t5-small agit comme noyau intelligent de Gopu. Il :

• Interprète les intentions utilisateur
• Route vers les bons modules
• Optimise les flux d’exécution
• Propose des améliorations
• Crée de nouveaux modules
• Évolue Gopu de manière autonome


---

🛡️ Sécurité Linux-only

Gopu refuse toute exécution sur macOS ou Windows. Exemple :

😣 Désolé, Gopu n'est pas encore disponible pour macOS
🔒 Environnement détecté : macOS (Ceose-Macbook)


---

🧪 Exemple d’exécution

✅ GopuOS booted on localhost
🔍 user_id:31032:linux_i6083
🧬 Distro: Ubuntu 22.04.3 LTS


---

🧠 Créé par Ceose

Gopu est l’incarnation de la vision de Ceose : un OS vivant, intelligent, modulaire, et introspectif. Chaque module est extensible, chaque commande est agentique, chaque exécution est optimisée.

---

📄 Licence

Licence MIT — ouvert à l’évolution, réservé aux environnements Linux.
