from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from datetime import date
import pandas as pd

#Write the path where you downloaded chrome driver
path = "chromedriver_win32"
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# File path consists of web page links
file_path = "cs210_data.txt"

# Read the contents of the file
with open(file_path, "r") as file:
    products = file.readlines()

# Strip any leading/trailing whitespace characters from each line and create the list
product_links = [line.strip() for line in products]

# Array for storing the corrupted links
bozuk_linkler = []

# Arrays for storing data
Product_Name = []
Current_Date = date.today()
Current_Price = []
Old_Date = []
Old_Price = []
Category = []


for product_link in product_links:
    driver.get(product_link)
    time.sleep(2)

    ### Extract Product Category ###
    try: 
        category_link = product_link.replace("https://www.akakce.com/", "")
        productCategory = category_link[0:category_link.find("/")]
        print("Product Category: ", productCategory)
    
        try:
            fiyatDegisimiButton = driver.find_element(By.XPATH, '//div[@class="graph_w"]')
            fiyatDegisimiButton.click()
            time.sleep(1)

            try:
                oneYearButton = driver.find_element(By.XPATH, '//span[@id="oneYear"]')
                oneYearButton.click()

                ### Extract Product Name ###
                try:
                    productName = driver.find_element(By.XPATH, "//b[@id='priceTitle']").text.strip()
                    productName = productName[0:productName.find(" son")]
                    print("Product Name: ", productName)
                
                    ### Extract Current Price ###
                    try:
                        canvas = driver.find_element(By.XPATH, "//div[@class='canvas_v8_w m1_v8']")
                        current_price = canvas.find_element(By.XPATH, "./p").find_element(By.XPATH, "./span[3]").find_element(By.XPATH, "./span").text.strip()
                        current_price = current_price.split(",")[0].replace(".", "")
                        print("Current Price: ", current_price)

                        try: 
                            litte_button = driver.find_element(By.XPATH, '//div[@id="tooltip"]')
                            achains = ActionChains(driver)
                            achains.move_to_element(litte_button).drag_and_drop_by_offset(litte_button,-483,0).perform()

                            ### Extract Earlier Price and Date ###
                            try:
                                one_year_ago_details = driver.find_element(By.XPATH, "//span[@class='tp']").text.strip()
                                split_data = one_year_ago_details.split("\n")
                                earlier_date = split_data[0].replace(".", "/")
                                earlier_price = split_data[1].split(",")[0].replace(".", "")
                                print("Earlier date: ", earlier_date)
                                print("Earlier price: ", earlier_price)

                                ### All successfully extracted, now write them to the array ###
                                Old_Date.append(earlier_date)
                                Old_Price.append(earlier_price)
                                Current_Price.append(current_price)
                                Product_Name.append(productName)
                                Category.append(productCategory)

                            except:
                                bozuk_linkler.append(product_link)
                                print("Error Extracting Earlier Price and Date!!: ", product_link)
                        except:
                            bozuk_linkler.append(product_link)
                            print("Error Dragging the Little Button!!: ", product_link)
                    except:
                        bozuk_linkler.append(product_link)
                        print("Error Extracting Current Price!!: ", product_link)
                except:
                    bozuk_linkler.append(product_link)
                    print("Error Extracting Product Name!!:", product_link)
            except:
                bozuk_linkler.append(product_link)
                print("Error clicking the oneYearButton!!:", product_link)
        except:
            bozuk_linkler.append(product_link)
            print("Error clicking the fiyatDegisimiButton!!:", product_link)
    except:
        bozuk_linkler.append(product_link)
        print("Error Extracting Product Category!!")

    print("------------------------------------")

## DATA IS READY, STORE THEM IN A CSV FILE ###
df = pd.DataFrame({
    'Product Name' : Product_Name,
    'Current Date' : Current_Date,
    'Current Price': Current_Price,
    'Old Date' : Old_Date,
    'Old Price' : Old_Price,
    'Category' : Category
})
df.to_csv('products_akakce.csv', encoding='utf-8-sig')

## STORE THE PROBLEMATIC LINKS IN A CSV FILE AS WELL TO BE REMOVED LATER ###
df_2 = pd.DataFrame({
    'bozuk linlker' : bozuk_linkler
})
df_2.to_csv('bozuk_linkler.csv', encoding='utf-8-sig')

driver.quit()