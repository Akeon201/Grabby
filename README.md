# Grabby

  This project is named Grabby. It is a web scraping tool that allows the user to specify a website and a file type to search for. It downloads all the files of that type on the website to a specified folder. The user can input the website, file type and folder name they want to use. It uses the python library requests and BeautifulSoup to send requests to the website and parse the HTML content. The program will then search for all the links on the webpage and download the files that end with the specified file type. It also prints out if the program ran successfully or if there was an error.

# Instructions

1. Make sure you have python installed in your system.
2. Install the packages requests and bs4 using pip by running 'pip install requests bs4' in the command line.
3. Open the command line and navigate to the directory where the file is saved.
4. Run the script by typing 'python filename.py' in the command line
5. The script will prompt you to enter a website, filetype and a folder name.
6. After entering the required details, the script will create a folder with the given folder name(if it doesn't exist) and will download the files of the specified filetype from the given website and save them in the created folder.
