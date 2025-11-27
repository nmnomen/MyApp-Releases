import hashlib
import os
import json
from datetime import datetime

def generate_checksums():
    checksums = {
        "generated": datetime.now().isoformat(),
        "files": {}
    }

    apk_path = "android/latest/app.apk"
    if os.path.exists(apk_path):
        with open(apk_path, 'rb') as f:
            apk_hash = hashlib.sha256(f.read()).hexdigest()
            checksums["files"]["android"] = {
                "filename": os.path.basename(apk_path),
                "sha256": apk_hash,
                "size": os.path.getsize(apk_path)
            }

    exe_path = "windows/latest/app.exe"
    if os.path.exists(exe_path):
        with open(exe_path, 'rb') as f:
            exe_hash = hashlib.sha256(f.read()).hexdigest()
            checksums["files"]["windows"] = {
                "filename": os.path.basename(exe_path),
                "sha256": exe_hash,
                "size": os.path.getsize(exe_path)
            }

    with open("checksums.json", "w") as f:
        json.dump(checksums, f, indent=2)

    with open("checksums.txt", "w") as f:
        f.write("Checksums generated: {}\n\n".format(checksums["generated"]))
        for platform, info in checksums["files"].items():
            f.write("{} ({})\n".format(info["filename"], platform))
            f.write("SHA256: {}\n".format(info["sha256"]))
            f.write("Size: {} bytes\n\n".format(info["size"]))

if __name__ == "__main__":
    generate_checksums()
