from PIL import Image

im = Image.open("scripts/top_right.png")
colors = im.getcolors(maxcolors=10000)
print(f"Unique colors in top_right: {len(colors)}")
# print some colors
bright_pixels = [c for c in colors if sum(c[1][:3]) > 300]
print(f"Bright pixels count: {len(bright_pixels)}")
for p in bright_pixels[:10]:
    print(p)
