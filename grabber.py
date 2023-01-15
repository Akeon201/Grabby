import os
import requests
from bs4 import BeautifulSoup

# Specify the url of the website to scrape
url = input("Please enter a website: ")

# Specify the file type to search for
file_type =input("Please enter a filetype: ")

# Specify the name of the folder to save files in
folder_name = input("Please enter a folder name: ")

# create the folder if it doesn't already exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# send a request to the website
try:
    response = requests.get(url)
    # parse the html content
    soup = BeautifulSoup(response.content, 'html.parser')

    # find all of the links on the webpage
    links = soup.find_all('a')

    # iterate over the links and download the ones that end with the specified file type
    for link in links:
        href = link.get('href')
        if href and href.endswith(file_type):
            file_url = url + href
            # send a request to download the file
            try:
                r = requests.get(file_url)
                with open(folder_name + '/' + href.split('/')[-1], 'wb') as f:
                    f.write(r.content)
                print(f'Successfully downloaded {href.split("/")[-1]}')
            except requests.exceptions.RequestException as e:
                print(f'Error downloading file {href.split("/")[-1]}: {e}')
    print('Finished downloading files.')

except requests.exceptions.RequestException as e:
    print(f'Error connecting to {url}: {e}')
