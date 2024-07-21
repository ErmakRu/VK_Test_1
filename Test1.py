from time import sleep
import urllib.request
import shutil
import os
from selenium.webdriver.common.by import By
import wget
from selenium import webdriver
import webbrowser
from pathlib import Path
import glob

URL = 'https://drive.usercontent.google.com/u/0/uc?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download'
RegFileName = "settings1.reg"
GooseFileWay = 'E:\SteamLibrary\steamapps\common\Goose Goose Duck'

# Load in windows dowanload
driver = webdriver.Chrome()
driver.get(URL)
sleep(7)
dowanload = driver.find_element(By.ID,'uc-download-link')
sleep(5)
dowanload.click()
sleep(7)
driver.close()

# Find in Dowanload file
downloads_path = str(Path.home() / "Downloads")
files = os.listdir(downloads_path)
file_type = r"\*crdownload"
files = glob.glob(downloads_path + file_type)
max_file = max(files, key=os.path.getctime)
os.rename(max_file, RegFileName)

# Move file,open file and game
RegNewFileName = shutil.move(RegFileName, GooseFileWay)
os.system('"'+GooseFileWay+'\settings1.reg'+'"')
os.system('"'+GooseFileWay+'\Goose Goose Duck.exe'+'"')
