from PIL import Image

im = Image.open("scripts/crop_bottom.png")
w, h = im.size
# crop right side of toolbar
toolbar_right = im.crop((int(w * 0.5), int(h * 0.4), w, int(h * 0.95)))
toolbar_right.save("scripts/toolbar_right.png")
print("Saved toolbar_right.png", toolbar_right.size)
