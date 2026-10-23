
import json
from pathlib import Path
from datetime import datetime

folder = Path("assets")

foto = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"}
video = {".mp4", ".webm", ".mov", ".m4v"}

kenangan = []

for file in sorted(folder.iterdir()):
    if not file.is_file():
        continue

    ext = file.suffix.lower()

    if ext in foto:
        tipe = "photo"
    elif ext in video:
        tipe = "video"
    else:
        continue

    kenangan.append({
        "id": file.name,
        "title": file.stem,
        "description": "",
        "file_url": f"assets/{file.name}",
        "media_type": tipe,
        "created_at": datetime.fromtimestamp(
            file.stat().st_mtime
        ).isoformat()
    })

Path("assets-list.json").write_text(
    json.dumps(kenangan, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print(f"Berhasil! {len(kenangan)} foto/video ditemukan.")
print("Daftar tersimpan di assets-list.json")
