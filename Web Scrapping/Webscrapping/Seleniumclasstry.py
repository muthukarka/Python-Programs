
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
from pathlib import Path

element_list = []

options = webdriver.ChromeOptions()

#to run in headless mode
#options.add_argument('--headless')
ser = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=ser,options=options)
for page in range(1, 3, 1):

    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
    driver.get(page_url)
    title = driver.find_elements(By.CLASS_NAME, "title")
    price = driver.find_elements(By.CLASS_NAME, "price")
    description = driver.find_elements(By.CLASS_NAME, "description")
    rating = driver.find_elements(By.CLASS_NAME, "ratings")
data = []
myfile = Path('test-output.csv')
with open(myfile, 'w') as csv_file_output:
   writer = csv.writer(csv_file_output)
   count = 0
   for i in range(len(title)):
       element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])
       writer.writerow(element_list)
       print("Data", element_list)
print("Script Completed")


#closing the driver
driver.close()
