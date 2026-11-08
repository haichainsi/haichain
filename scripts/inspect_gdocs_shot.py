from PIL import Image

im = Image.open("scripts/gdocs_screenshot.png")
print("Size:", im.size)

# Crop the top 150px
w, h = im.size
crop_top = im.crop((0, 0, w, 150))
crop_top.save("scripts/gdocs_top.png")

# Crop top-right corner (last 100px width, first 100px height)
crop_tr = im.crop((w - 100, 0, w, 100))
crop_tr.save("scripts/gdocs_tr.png")

print("Saved gdocs_top.png and gdocs_tr.png")
