import cv2
import numpy as np
from datetime import datetime

INPUT = "input_marked.png"
OUTPUT = "input_marked_visible.png"
LOGFILE = "watermark_log.txt"

print("🔍 Dekodiere...")

img = cv2.imread(INPUT)
if img is None:
    raise Exception("Bild konnte nicht geladen werden!")

h, w, _ = img.shape
f = img.astype(np.float32)

green = f[:, :, 1]
blue  = f[:, :, 2]
diff  = green - blue

bits = []

# *** GLEICHER MARKERBEREICH WIE ENCODER ***
for row in range(0, min(150, h), 5):
    for col in range(0, w, 8):
        bits.append("1" if diff[row, col] > 0 else "0")

# -----------------------
# Bits → Text
# -----------------------
bitstring = "".join(bits)
decoded = ""

for i in range(0, len(bitstring), 8):
    byte = bitstring[i:i+8]
    if len(byte) < 8:
        break
    ch = chr(int(byte, 2))
    decoded += ch
    if decoded.endswith("<END>"):
        decoded = decoded.replace("<END>", "")
        break

# -----------------------
# Payload parsen
# -----------------------
payload = {}
for p in decoded.split("|"):
    if ":" in p:
        k, v = p.split(":", 1)
        payload[k] = v

print("📜 Payload:")
print(payload)

# -----------------------
# LOGFILE SCHREIBEN (APPEND!)
# -----------------------
with open(LOGFILE, "a", encoding="utf-8") as f_log:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = timestamp

    for k, v in payload.items():
        line += f" | {k}: {v}"

    f_log.write(line + "\n")

print(f"📝 Log hinzugefügt: {LOGFILE}")

# -----------------------
# TEXT OVERLAY INS BILD
# -----------------------
overlay = img.copy()
y = 35

for k, v in payload.items():
    cv2.putText(
        overlay,
        f"{k}: {v}",
        (10, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )
    y += 28

cv2.imwrite(OUTPUT, overlay)
print("💾 Bild gespeichert als:", OUTPUT)

print("🎉 Fertig – Bild markiert + Log aktualisiert!")
