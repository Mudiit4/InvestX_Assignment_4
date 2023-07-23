from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path='D:\chromedriver_win32\chromedriver.exe')

driver.get("https://opstra.definedge.com")
time.sleep(3)

driver.find_element_by_xpath('//*[@id="app"]/div[2]/nav/div/div[4]/button/div').click()
time.sleep(1)

email = driver.find_element_by_xpath('//*[@id="username"]')
pw = driver.find_element_by_xpath('//*[@id="password"]')

time.sleep(2)

email.send_keys('YOUR_EMAIL')
pw.send_keys('YOUR_PASSWORD')
driver.find_element_by_xpath('//*[@id="kc-login"]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="app"]/div[8]/nav/div/div[3]/a[2]/div').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[1]/div[1]').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[1]/div[7]/button/div').click()
time.sleep(3)
table_element = driver.find_element_by_css_selector('table')
table_html = table_element.get_attribute('outerHTML')
from bs4 import BeautifulSoup

soup = BeautifulSoup(table_html, 'html.parser')
data_list = []

# Find all table rows (tr elements) in the table
rows = soup.find_all('tr')
import csv
for row in rows:
    # Find all cells (td elements) in each row
    cells = row.find_all(['td', 'th'])

    # Extract data from each cell and add it to the data_list as a row
    row_data = [cell.get_text(strip=True) for cell in cells]
    data_list.append(row_data)

# Save the data_list to a CSV file
csv_file_path = '28DEC2023.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data_list)

print(f"Data saved to {csv_file_path}.")