import subprocess
import socket

def run(args=None):
    def check_dns(host):
        try:
            ip = socket.gethostbyname(host)
            print(f"✅ DNS OK: {host} → {ip}")
            return True
        except Exception as e:
            print(f"❌ DNS échec: {host} → {e}")
            return False

    print("📦 GopuOS — Publication PyPI")

    if check_dns("upload.pypi.org"):
        print("🚀 Upload vers PyPI...")
        cmd = "python3 -m twine upload dist/*"
    else:
        print("🔁 Fallback vers TestPyPI...")
        cmd = "python3 -m twine upload --repository testpypi dist/*"

    try:
        subprocess.run(cmd, shell=True, check=True)
        print("✅ Publication réussie")
    except subprocess.CalledProcessError as e:
        print("❌ Échec de publication:", e)
