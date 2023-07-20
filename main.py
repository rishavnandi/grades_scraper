import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="D:\projects\grades_scraper\chromedriver.exe")

driver = webdriver.Chrome(service=service)

URL = "https://www.your-university-website.com/"

# Navigate to the result website
driver.get(URL)
driver.maximize_window()

# Create an empty list to store the data
data = []

# Input registration numbers in the specified range
for reg_no in range(2101020000, 2101021000):
    try:
        reg_no_input = driver.find_element(By.ID, "regn_no")
        reg_no_input.clear()
        reg_no_input.send_keys(str(reg_no))
        reg_no_input.send_keys(Keys.ENTER)

        # Scrape student name and SGPA
        student_name = driver.find_element(By.XPATH, "//li[2]")
        student_name = student_name.text[13:]
        student_name = student_name.strip()
        sgpa = driver.find_element(By.XPATH, "//span[b[contains(text(), 'SGPA:')]]")
        sgpa = sgpa.text[5:]
        sgpa = sgpa.strip()

        # Print the student's registration number, name and SGPA
        print(f"Registration Number: {reg_no}, Name: {student_name}, SGPA: {sgpa}")

        # Append the data to the list
        data.append({
            'Registration Number': reg_no,
            'Name': student_name,
            'SGPA': sgpa
        })
    except:
        # Handle the case when a student with the registration number does not exist
        print(f"Error for registration number: {reg_no}")

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('student_results.csv', index=False)