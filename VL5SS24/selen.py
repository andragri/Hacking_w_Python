from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service(executable_path="./chromedriver")

driver = webdriver.Chrome(service=s)
website = "http://127.0.0.1:5000/login"
driver.get(website)

title = ""

passwords = ["tes", "sss", "ssfsdfs", "dsfg", "pass"]


for password in passwords:
    print("Testing this password: ", password)

    res = driver.find_elements(By.CLASS_NAME, "form-control")

    assert(len(res) == 2) #weil login , pass

    res[0].clear()
    res[0].send_keys("Andra")
    time.sleep(2)
    res[1].clear()
    res[1].send_keys(password)

    button = driver.find_elements(By.CLASS_NAME, "btn")
    assert(len(button) == 1) #unit testing 
    button[0].click()

    print(driver.title)
    if driver.title != "Login":
        print(f"Password is {password}")
        break

    time.sleep(2)
driver.quit()