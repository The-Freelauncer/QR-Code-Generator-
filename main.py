import qrcode
import time

# -------------------- Fancy Banner --------------------
print("\n" + "█" * 60)
print("█" + " " * 58 + "█")
print("█   🔳🔲🔳   QR CODE GENERATOR TOOL   🔳🔲🔳   █")
print("█" + " " * 58 + "█")
print("█" * 60 + "\n")

# -------------------- User Input --------------------
url = input("🌐 Enter a Text or URL ➜ ").strip()

print("\n⏳ Generating QR Code...")
time.sleep(1)

img = qrcode.make(url)

# -------------------- Filename Options --------------------
print("\n" + "─" * 60)
print("📁 FILE SAVE OPTIONS")
print("─" * 60)
print("  [1] ▶ Save with Default Filename  (QRcode.png)")
print("  [2] ▶ Save with Custom Filename")
print("─" * 60)

try:
    n = int(input("🧠 Enter your choice ➜ "))

    if n == 1:
        print("\n💾 Saving QR Code...")
        time.sleep(1)
        img.save("QRcode.png")

        print("\n" + "✓" * 60)
        print("✅ QR CODE GENERATED SUCCESSFULLY!")
        print("📂 File Name : QRcode.png")
        print("📍 Saved In  : Current Directory")
        print("✓" * 60)

    elif n == 2:
        filename = input("\n✏️  Enter custom filename (without extension) ➜ ").strip()

        print("\n💾 Saving QR Code...")
        time.sleep(1)
        img.save(filename + ".png")

        print("\n" + "✓" * 60)
        print("✅ QR CODE GENERATED SUCCESSFULLY!")
        print(f"📂 File Name : {filename}.png")
        print("📍 Saved In  : Current Directory")
        print("✓" * 60)

    else:
        print("\n" + "!" * 60)
        print("❌ INVALID INPUT DETECTED!")
        print("⚠️  Please choose only 1 or 2.")
        print("!" * 60)

except ValueError:
    print("\n" + "!" * 60)
    print("❌ INPUT ERROR!")
    print("⚠️  Please enter numeric values only (1 or 2).")
    print("!" * 60)

# -------------------- Footer --------------------
print("\n" + "█" * 60)
print("✨ Thank you for using QR Code Generator ✨")
print("🔐 Fast • Simple • Reliable")
print("█" * 60 + "\n")
