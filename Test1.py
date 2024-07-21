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

# Скачивает в загрузки файл
driver = webdriver.Chrome()
driver.get(URL)
sleep(15)
dowanload = driver.find_element(By.ID,'uc-download-link')
sleep(13)
dowanload.click()
sleep(15)
driver.close()

#Находит файл в загрузках
downloads_path = str(Path.home() / "Downloads")
files = os.listdir(downloads_path)
file_type = r"\*crdownload"
files = glob.glob(downloads_path + file_type)
max_file = max(files, key=os.path.getctime)
os.rename(max_file, RegFileName)

# Перемещаем файл к игре
RegNewFileName = shutil.move(RegFileName, GooseFileWay)
os.system('"E:\SteamLibrary\steamapps\common\Goose Goose Duck\settings1.reg"')
sleep(30)
os.system('"E:\SteamLibrary\steamapps\common\Goose Goose Duck\Goose Goose Duck.exe"')
os.system(GooseFileWay+'\Goose Goose Duck.exe')
#os.remove(RegNewFileName)
