from PIL import Image

im = Image.open("scripts/crop_top.png")
w, h = im.size
# crop right side of top
top_right = im.crop((int(w * 0.7), 0, w, int(h * 0.4)))
top_right.save("scripts/top_right.png")
print("Saved top_right.png", top_right.size)
