# Using Python 3.6.8
from PIL import Image

'''
Resize image keeping aspect ratio
'''
print("Resize image keeping aspect ratio")
print("-" * 50)
img = Image.open('image.jpg')
width, height = img.size
new_width = 1200
if new_width > width:
    print("augmenting, this can cause blur effect")
else:
    print("reducing, this will keep inital resolution")
width_ratio = new_width / width
new_height = int(height * width_ratio)
dimensions = f"{new_width}x{new_height}"
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save(f"{dimensions}_keepingAR.jpg")
print()


'''
Resize image breaking aspect ratio
'''
print("Resize image breaking aspect ratio")
print("-" * 50)
img = Image.open('image.jpg')
# width, height = img.size
new_width = 1200
new_height = 1200
dimensions = f"{new_width}x{new_height}"
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save(f"{dimensions}_breakingAR.jpg")
print()


'''
Crop image from top 0 and left 0
'''
print("Crop image from top 0 and left 0")
print("-" * 50)
img = Image.open('image.jpg')
width, height = img.size
new_width = 1500
new_height = 1500
left = 0
top = 0
right = new_width
bottom = new_height
dimensions = f"{new_width}x{new_height}"
img = img.crop((left, top, right, bottom))  # Not ANTIALIAS!
img.save(f"{dimensions}_cropped.jpg")
print()


'''
Crop image from center
'''
print("Crop image from center")
print("-" * 50)
img = Image.open('image.jpg')
width, height = img.size
new_width = 1500
new_height = 1500
left = (width - new_width) / 2
top = (height - new_height) / 2
right = (width + new_width) / 2
bottom = (height + new_height) / 2
dimensions = f"{new_width}x{new_height}"
img = img.crop((left, top, right, bottom))  # Not ANTIALIAS!
img.save(f"{dimensions}_cropped_center.jpg")
print()
