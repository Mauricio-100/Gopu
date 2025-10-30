import socket
import requests

def run(args=None):
    host = "upload.pypi.org"
    print(f"🔍 Résolution DNS pour {host}...")
    try:
        ip = socket.gethostbyname(host)
        print(f"✅ DNS OK: {host} → {ip}")
    except Exception as e:
        print(f"❌ DNS échec: {e}")
        return

    print("🌐 Test HTTP HEAD...")
    try:
        res = requests.head(f"https://{host}", timeout=5)
        print(f"✅ HTTP OK: {res.status_code}")
    except Exception as e:
        print(f"❌ HTTP échec: {e}")
