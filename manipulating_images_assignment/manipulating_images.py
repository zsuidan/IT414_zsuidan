from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from bs4 import BeautifulSoup
import requests
import os
import zipfile
import shutil

#Deletes images directory if it exists and creates new one
if os.path.exists('images'):
    shutil.rmtree('images')
os.makedirs('images')

#Makes a request to the webpage containing the images
url = "https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week10/WI20-Assignment/employees/index.php?ModPagespeed=off"
request = requests.get(url)
request.raise_for_status()

employee_soup = BeautifulSoup(request.text, 'html.parser')

#Pulls logo from webpage
logo_image = employee_soup.find('img')
logo_url = 'https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week10/WI20-Assignment/employees/' + logo_image.get('src')
request = requests.get(logo_url)

#Splits the src text to get the file name by itself
split_logo_src = logo_image.get('src').split('/')
logo_filename = split_logo_src[1]

#Writes logo image to images folder
with open('images/' + logo_filename, "wb") as image_file:
    for chunk in request.iter_content(100000):
            image_file.write(chunk)

#Pulls employee names and titles from webpage then sorts them alphabetically
employee_list = []
employee_data = employee_soup.select('h5')

for employee in employee_data:
    employee_list.append(employee.getText())

employee_list.sort()

#Pulls employee images from webpage 
employee_images = employee_soup.findAll('img', {"class": ["card-img-top"]})

for image in employee_images:
    #Finds url of the employee image and makes a request
    image_url = 'https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week10/WI20-Assignment/employees/' + image.get('src')
    request = requests.get(image_url)

    #Splits the src text to get the file name by itself
    split_src = image.get('src').split('/')
    employee_image_filename = split_src[1]

    #Writes employee image to the images folder
    with open('images/' + employee_image_filename, "wb") as image_file:
        for chunk in request.iter_content(100000):
            image_file.write(chunk)

#Opens logo file and resizes it to half
logo_img = Image.open('images/' + logo_filename)
logoWidth, logoHeight = logo_img.size
half_size_logo = logo_img.resize((int(logoWidth / 2), int(logoHeight / 2)))

#Creates new directory for altered images
os.makedirs('images/output_images', exist_ok=True)

#Loops through each employee image in the images directory and adds a logo and employee name/title
employee_count = 0

for filename in os.listdir('images'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_filename:
        continue

    my_image = Image.open('images/' + filename)

    #Inserts the logo into the image
    my_image.paste(half_size_logo, (175, 450), half_size_logo)
    my_image.save(os.path.join('images/output_images/', filename))

    #Preparing to insert text into the image
    draw_text = ImageDraw.Draw(my_image)
    font = ImageFont.truetype("fonts/Syne-Regular.otf", 24)

    #Splits the name and title into separate strings
    employee_info = employee_list[employee_count].split(', ')

    #Inserts employee name into the image
    draw_text.text((30,390), employee_info[0], (0, 0, 0), font)

    #Inserts employee title into the image
    draw_text.text((40,420), employee_info[1], (0, 0, 0), font)

    my_image.save(os.path.join('images/output_images/', filename))

    employee_count += 1

#Places altered images into a zip file
imageZip = zipfile.ZipFile('images/output_images.zip', 'w')
os.chdir('images/output_images')
for filename in os.listdir('.'):
    imageZip.write(filename, compress_type=zipfile.ZIP_DEFLATED)
imageZip.close()