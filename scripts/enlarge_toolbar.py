from PIL import Image

im = Image.open('scripts/toolbar_right.png')
# resize 4x so we can inspect easily
im_large = im.resize((im.width * 4, im.height * 4), Image.Resampling.NEAREST)
im_large.save('scripts/toolbar_enlarged.png')
print('Saved toolbar_enlarged.png')
