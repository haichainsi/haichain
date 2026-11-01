import os
import shutil
from PIL import Image, ImageOps

SOURCE_IMAGE_PATH = r"C:/Users/Surface/.gemini/antigravity/brain/63572c29-9e0f-42cf-9782-9260a498810d/.user_uploaded/media_1793549014251_55ed2ed6.png"

def generate_icons():
    print(f"Loading source image from: {SOURCE_IMAGE_PATH}")
    src = Image.open(SOURCE_IMAGE_PATH).convert("RGBA")
    print(f"Source size: {src.size}, mode: {src.mode}")

    # Directories to output
    target_dirs = [
        "assets",
        "app/assets"
    ]
    for d in target_dirs:
        os.makedirs(d, exist_ok=True)

    # 1. Base High-Res 1024x1024 master
    master_1024 = src.copy()

    # 2. Resized variants (standard / "any" purpose)
    img_512 = src.resize((512, 512), Image.Resampling.LANCZOS)
    img_192 = src.resize((192, 192), Image.Resampling.LANCZOS)
    img_180 = src.resize((180, 180), Image.Resampling.LANCZOS)
    img_64  = src.resize((64, 64), Image.Resampling.LANCZOS)
    img_48  = src.resize((48, 48), Image.Resampling.LANCZOS)
    img_32  = src.resize((32, 32), Image.Resampling.LANCZOS)
    img_16  = src.resize((16, 16), Image.Resampling.LANCZOS)

    # 3. Maskable variants (for Chrome PWA & Android adaptive icons)
    # Background #09090b with the symbol perfectly fitted in the 80% safe zone
    maskable_canvas_1024 = Image.new("RGBA", (1024, 1024), (9, 9, 11, 255))
    # Scale down squircle slightly (88%) to ensure safe zone compliance
    scaled_squircle = src.resize((int(1024 * 0.88), int(1024 * 0.88)), Image.Resampling.LANCZOS)
    offset = ((1024 - scaled_squircle.width) // 2, (1024 - scaled_squircle.height) // 2)
    maskable_canvas_1024.alpha_composite(scaled_squircle, offset)

    maskable_512 = maskable_canvas_1024.resize((512, 512), Image.Resampling.LANCZOS)
    maskable_192 = maskable_canvas_1024.resize((192, 192), Image.Resampling.LANCZOS)

    # 4. Save Favicon ICO (Multi-size 16, 32, 48, 64)
    # For ICO, we create images for each resolution
    ico_images = [img_16, img_32, img_48, img_64]
    
    # Save files to Root
    img_512.save("favicon.png", "PNG", optimize=True)
    img_180.save("apple-touch-icon.png", "PNG", optimize=True)
    img_180.save("apple-touch-icon-precomposed.png", "PNG", optimize=True)
    src.save("favicon.ico", format="ICO", sizes=[(16,16), (32,32), (48,48), (64,64)])

    # Save to Root / Assets
    files_to_save_in_assets = [
        ("favicon.ico", lambda p: src.save(p, format="ICO", sizes=[(16,16), (32,32), (48,48), (64,64)])),
        ("favicon-16x16.png", lambda p: img_16.save(p, "PNG", optimize=True)),
        ("favicon-32x32.png", lambda p: img_32.save(p, "PNG", optimize=True)),
        ("favicon-48x48.png", lambda p: img_48.save(p, "PNG", optimize=True)),
        ("apple-touch-icon.png", lambda p: img_180.save(p, "PNG", optimize=True)),
        ("icon-192.png", lambda p: img_192.save(p, "PNG", optimize=True)),
        ("icon-512.png", lambda p: img_512.save(p, "PNG", optimize=True)),
        ("icon-maskable-192.png", lambda p: maskable_192.save(p, "PNG", optimize=True)),
        ("icon-maskable-512.png", lambda p: maskable_512.save(p, "PNG", optimize=True)),
        ("icon.png", lambda p: master_1024.save(p, "PNG", optimize=True)),
        ("haisi-icon.png", lambda p: master_1024.save(p, "PNG", optimize=True)),
        ("haisi-token.png", lambda p: master_1024.save(p, "PNG", optimize=True)),
        ("haichain-icon.png", lambda p: master_1024.save(p, "PNG", optimize=True)),
        ("haichain-icon-white.png", lambda p: img_512.save(p, "PNG", optimize=True)),
    ]

    for filename, saver in files_to_save_in_assets:
        saver(os.path.join("assets", filename))
        print(f"Generated assets/{filename}")

    # Mirror to app/ and app/assets/
    shutil.copy2("favicon.ico", "app/favicon.ico")
    shutil.copy2("favicon.png", "app/favicon.png")
    shutil.copy2("apple-touch-icon.png", "app/apple-touch-icon.png")
    shutil.copy2("apple-touch-icon-precomposed.png", "app/apple-touch-icon-precomposed.png")
    print("Copied root favicon and apple-touch-icon to app/")

    for filename, _ in files_to_save_in_assets:
        shutil.copy2(os.path.join("assets", filename), os.path.join("app", "assets", filename))
        print(f"Mirrored to app/assets/{filename}")

    print("\n[SUCCESS] All Web, Favicon, Web3 Wallet, HAISI Solana Token, and Chrome PWA icons generated successfully!")

if __name__ == "__main__":
    generate_icons()
