# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 04:04:13 2022

@author: Zo3bi
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from glob import glob
import csv
from datetime import datetime



now = datetime.now() 
date_time = now.strftime("%Y%m%d%H%M%S")

driver = webdriver.Chrome('E:/My project/Python/chromedriver.exe')

folder_path = 'E:\My project\Python\Dataset1'
urls = glob(folder_path + "/*.html")

file_name = "methods - " + date_time
with open("results/"+ file_name +'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Class", "Methods"])

    occurrence_dict = {}
    occurrence_loc_dict = {}
    for page_url in urls:
        driver.get(page_url)
        class_title = driver.title    
        try:
            z = driver.find_elements(By.XPATH,"//section[@class='method-summary']//a[@class='member-name-link']")
           
            for x in z:
                writer.writerow([class_title, x.text])
                if(x.text not in occurrence_dict.keys()):
                    occurrence_dict.update({ x.text : 1 })
                    occurrence_loc_dict.update({ x.text : class_title })
                else:
                   occ = occurrence_dict.get(x.text)
                   occurrence_dict.update({x.text : occ + 1})
                   
                   occ_loc = occurrence_loc_dict.get(x.text)
                   occurrence_loc_dict.update({ x.text : occ_loc + "," + class_title })
                    
                print(class_title, x.text)
            
        except Exception as e :
            print (e)
            print(class_title + "failed")
            pass
        
        writer.writerow([])
        
    writer.writerow(["Method", "# of occurrence"])
    for x in occurrence_dict.keys():
        writer.writerow([x, occurrence_dict.get(x)])

    for k in occurrence_loc_dict.keys():
        writer.writerow([k, occurrence_loc_dict.get(k)])

driver.close()
    





