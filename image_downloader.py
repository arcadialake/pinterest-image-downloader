#! python 3
#  Downloads all images from search in photo sharing site

import requests
import os
import bs4
import re

url = input('Enter the url of the board you would like to download: ')  # starting url
filename = str(input('Enter the filename you would like the board downloaded into: '))
print('The folder will be stored in the same directory you ran the program from')
os.makedirs(filename, exist_ok=True)  # Store images in the named directory

#  Download the page with the images
print('Downloading images...')
res = requests.get(url)
res.raise_for_status()

#  Find the url of the images
soup = bs4.BeautifulSoup(res.text, 'html.parser')
parent = soup.find(id="initial-state")

src_regex = re.compile(r'https://\w\.pinimg\.com/\w+/\w+/\w+/\w+/\w+\.\w+')
mo = src_regex.findall(str(parent))

#  Download images
for image_url in mo:
    res = requests.get(image_url)
    res.raise_for_status()

    image_file = open(os.path.join(filename, os.path.basename(image_url)), 'wb')

    for images in res.iter_content(100000):
        image_file.write(images)
    image_file.close()

print('Download complete')
