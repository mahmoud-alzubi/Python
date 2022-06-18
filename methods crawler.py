# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 04:04:13 2022

@author: Zo3bi
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from glob import glob
import csv

driver = webdriver.Chrome('E:/My project/Python/chromedriver.exe')

folder_path = 'E:/My project/Workspace/BatBat-Project JavaDoc/doc/al/tonikolaba/gamestate'
urls = glob(folder_path + "/*.html")

file_name = "methods"
with open(file_name+'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Class", "Methods"])

    for page_url in urls:
        driver.get(page_url)
        class_title = driver.title    
        try:
            z = driver.find_elements(By.XPATH,"//section[@class='method-summary']//a[@class='member-name-link']")
           
            for x in z:
                writer.writerow([class_title, x.text])
                print(class_title, x.text)
            
        
        except Exception:
            print(class_title + "failed")
            pass
        
        writer.writerow([])

driver.close()
    
       




