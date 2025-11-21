import cv2
import numpy as np
import hashlib
from datetime import datetime

INPUT = "input.png"
OUTPUT = "input_marked.png"

PAYLOAD = {
    "id": "LEON signed",
    "creator": "leon",
    "date": str(datetime.now()),
    "device_uid": "MAC-DEVICE-1234-5678",
}

# Hash hinzufügen SynthID
with open(INPUT, "rb") as f:
    PAYLOAD["hash"] = hashlib.sha256(f.read()).hexdigest()

# Payload vorbereiten
payload_str = "|".join([f"{k}:{v}" for k, v in PAYLOAD.items()]) + "<END>"
bits = "".join(format(ord(c), "08b") for c in payload_str)

print("ℹ️ Bits total:", len(bits))

# Bild laden
img = cv2.imread(INPUT)
if img is None:
    raise Exception("Bild konnte nicht geladen werden!")

h, w, _ = img.shape
f = img.astype(np.float32)

strength = 3.0
bit_i = 0

# *** NUR EIN KLEINES BEREICH (oben links, 150px hoch) ***
for row in range(0, min(150, h), 5):
    for col in range(0, w, 8):  # nur jeder 8. Pixel = kleines Muster
        if bit_i >= len(bits):
            break

        bit = bits[bit_i]
        bit_i += 1

        if bit == "1":
            f[row, col, 1] += strength
        else:
            f[row, col, 2] += strength

# Speichern
marked = np.clip(f, 0, 255).astype(np.uint8)
cv2.imwrite(OUTPUT, marked)

print("✅ Fertig – gespeichert als:", OUTPUT)
