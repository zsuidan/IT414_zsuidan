from PIL import Image
from PIL import ExifTags
from PIL import ImageFont
from PIL import ImageDraw

my_image = Image.open("images/mountain_scene.jpg")

print(my_image.size)

#Pull metadata from image and print it out in a dictionary
exif_data = {}
for key, value in my_image._getexif().items():
    if key in ExifTags.TAGS:
        exif_data[ExifTags.TAGS[key]] = value

#print(exif_data)

#Insert text into image
draw_text = ImageDraw.Draw(my_image)
font = ImageFont.truetype("fonts/Syne-Regular.otf", 24)

draw_text.text((25,50), "A Mountain", (204, 51, 153), font)
my_image.save("images/sample-output.jpg")